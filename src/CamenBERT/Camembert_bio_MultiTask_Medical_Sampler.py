import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
# 核心改动：导入 Camembert 模型和分词器
from transformers import AutoModel, AutoTokenizer, get_linear_schedule_with_warmup
from torch.optim import AdamW
from sklearn.metrics import accuracy_score, f1_score
import json
import pandas as pd
import os
from collections import Counter

# ====================================================================
# 1. Dataset 类 (为方便采样，增加返回所有标签的方法)
# ====================================================================

class DatasetMultiTache(Dataset):
    def __init__(self, chemin_fichier, tokenizer, max_longueur):
        self.donnees = self._charger_donnees(chemin_fichier)
        self.tokenizer = tokenizer
        self.max_longueur = max_longueur

        # Mappage des étiquettes vers des IDs
        self.etiquettes_intention = {'recherche_information': 0, 'partage_experience': 1, 'fonction_phatique': 2}
        self.etiquettes_objet_medical = {'symptome': 0, 'traitement': 1, 'diagnostique': 2, 'NA_CATEGORY': 3}
        self.etiquettes_sentiment = {'positif': 0, 'negatif': 1, 'non': 2, 'RARE_CLASS': 3}

    def _charger_donnees(self, chemin_fichier):
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            return [json.loads(line) for line in f]

    def __len__(self):
        return len(self.donnees)

    def __getitem__(self, index):
        item = self.donnees[index]
        texte = str(item['texte'])
        
        # Récupérer les étiquettes pour chaque tâche
        intention = self.etiquettes_intention[item['intention']]
        objet_medical = self.etiquettes_objet_medical[item['objet_medical']]
        sentiment = self.etiquettes_sentiment[item['sentiment']]

        # Tokeniser le texte
        encodage = self.tokenizer.encode_plus(
            texte,
            add_special_tokens=True,
            max_length=self.max_longueur,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encodage['input_ids'].flatten(),
            'attention_mask': encodage['attention_mask'].flatten(),
            'labels_intention': torch.tensor(intention, dtype=torch.long),
            'labels_objet_medical': torch.tensor(objet_medical, dtype=torch.long),
            'labels_sentiment': torch.tensor(sentiment, dtype=torch.long)
        }

    def get_all_labels(self, label_type):
        """返回指定任务的所有标签列表，用于计算采样权重。"""
        if label_type == 'intention':
            return [self.etiquettes_intention[d['intention']] for d in self.donnees]
        elif label_type == 'objet_medical':
            return [self.etiquettes_objet_medical[d['objet_medical']] for d in self.donnees]
        elif label_type == 'sentiment':
            return [self.etiquettes_sentiment[d['sentiment']] for d in self.donnees]
        else:
            raise ValueError("Invalid label_type. Choose from 'intention', 'objet_medical', 'sentiment'.")

# ====================================================================
# 2. 多任务模型 (使用 AutoModel)
# ====================================================================

class MedicalMultiTache(nn.Module):
    def __init__(self, nom_modele_pre_entraine, num_intention, num_objet_medical, num_sentiment):
        super(MedicalMultiTache, self).__init__()
        
        # 使用 AutoModel 自动加载任何 BERT-like 模型
        self.model = AutoModel.from_pretrained(nom_modele_pre_entraine)
        
        # 独立的分类头
        self.classifieur_intention = nn.Linear(self.model.config.hidden_size, num_intention)
        self.classifieur_objet_medical = nn.Linear(self.model.config.hidden_size, num_objet_medical)
        self.classifieur_sentiment = nn.Linear(self.model.config.hidden_size, num_sentiment)
        
    def forward(self, input_ids, attention_mask):
        # 通过预训练模型编码器
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        
        # 使用池化输出 (通常是 [CLS] token 的表示)
        pooled_output = outputs.pooler_output
        
        # 独立分类
        logits_intention = self.classifieur_intention(pooled_output)
        logits_objet_medical = self.classifieur_objet_medical(pooled_output)
        logits_sentiment = self.classifieur_sentiment(pooled_output)
        
        return logits_intention, logits_objet_medical, logits_sentiment

# ====================================================================
# 3. 训练和评估函数 (保持不变)
# ====================================================================

def entrainer(modele, chargeur_donnees, optimiseur, scheduler, fonction_pertes, appareil):
    modele.train()
    perte_totale = 0
    
    for batch in chargeur_donnees:
        input_ids = batch['input_ids'].to(appareil)
        attention_mask = batch['attention_mask'].to(appareil)
        labels_intention = batch['labels_intention'].to(appareil)
        labels_objet_medical = batch['labels_objet_medical'].to(appareil)
        labels_sentiment = batch['labels_sentiment'].to(appareil)
        
        optimiseur.zero_grad()
        
        logits_intention, logits_objet_medical, logits_sentiment = modele(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        
        perte_intention = fonction_pertes['intention'](logits_intention, labels_intention)
        perte_objet_medical = fonction_pertes['objet_medical'](logits_objet_medical, labels_objet_medical)
        perte_sentiment = fonction_pertes['sentiment'](logits_sentiment, labels_sentiment)
        
        perte_totale_batch = perte_intention + perte_objet_medical + perte_sentiment
        perte_totale_batch.backward()
        
        optimiseur.step()
        scheduler.step()
        
        perte_totale += perte_totale_batch.item()
    
    return perte_totale / len(chargeur_donnees)

def evaluer(modele, chargeur_donnees, appareil):
    modele.eval()
    
    predictions_intention, labels_reels_intention = [], []
    predictions_objet_medical, labels_reels_objet_medical = [], []
    predictions_sentiment, labels_reels_sentiment = [], []
    
    with torch.no_grad():
        for batch in chargeur_donnees:
            input_ids = batch['input_ids'].to(appareil)
            attention_mask = batch['attention_mask'].to(appareil)
            labels_intention = batch['labels_intention'].to(appareil)
            labels_objet_medical = batch['labels_objet_medical'].to(appareil)
            labels_sentiment = batch['labels_sentiment'].to(appareil)
            
            logits_intention, logits_objet_medical, logits_sentiment = modele(
                input_ids=input_ids,
                attention_mask=attention_mask
            )
            
            predictions_intention.extend(torch.argmax(logits_intention, dim=1).cpu().numpy())
            labels_reels_intention.extend(labels_intention.cpu().numpy())
            predictions_objet_medical.extend(torch.argmax(logits_objet_medical, dim=1).cpu().numpy())
            labels_reels_objet_medical.extend(labels_objet_medical.cpu().numpy())
            predictions_sentiment.extend(torch.argmax(logits_sentiment, dim=1).cpu().numpy())
            labels_reels_sentiment.extend(labels_sentiment.cpu().numpy())

    acc_intention = accuracy_score(labels_reels_intention, predictions_intention)
    f1_intention = f1_score(labels_reels_intention, predictions_intention, average='macro')
    acc_objet_medical = accuracy_score(labels_reels_objet_medical, predictions_objet_medical)
    f1_objet_medical = f1_score(labels_reels_objet_medical, predictions_objet_medical, average='macro')
    acc_sentiment = accuracy_score(labels_reels_sentiment, predictions_sentiment)
    f1_sentiment = f1_score(labels_reels_sentiment, predictions_sentiment, average='macro')
    
    return {
        'acc_intention': acc_intention, 'f1_intention': f1_intention,
        'acc_objet_medical': acc_objet_medical, 'f1_objet_medical': f1_objet_medical,
        'acc_sentiment': acc_sentiment, 'f1_sentiment': f1_sentiment
    }

# ====================================================================
# 4. 数据转换函数 (保持不变)
# ====================================================================

def verifier_et_convertir_donnees(chemin_jsonl, chemin_csv):
    if os.path.exists(chemin_jsonl):
        print(f"文件 {chemin_jsonl} 已找到, 跳过转换.")
        return

    print(f"文件 {chemin_jsonl} 未找到, 正在从 {chemin_csv} 进行转换...")
    if not os.path.exists(chemin_csv):
        print(f"错误: 文件 {chemin_csv} 不存在. 请检查路径.")
        exit()
    
    repertoire_sortie = os.path.dirname(chemin_jsonl)
    if repertoire_sortie and not os.path.exists(repertoire_sortie):
        os.makedirs(repertoire_sortie)

    try:
        df = pd.read_csv(chemin_csv)
        df = df.rename(columns={
            'Sentences': 'texte', 'niveau1': 'intention',
            'niveau2': 'objet_medical', 'niveau3': 'sentiment'
        })
        colonnes_requises = ['texte', 'intention', 'objet_medical', 'sentiment']
        if not all(col in df.columns for col in colonnes_requises):
            raise ValueError(f"CSV 文件不包含所有必需的列.")
        with open(chemin_jsonl, 'w', encoding='utf-8') as f:
            for _, row in df.iterrows():
                dictionnaire_donnees = {
                    'texte': row['texte'], 'intention': row['intention'],
                    'objet_medical': row['objet_medical'], 'sentiment': row['sentiment']
                }
                f.write(json.dumps(dictionnaire_donnees, ensure_ascii=False) + '\n')
        print(f"成功将 {chemin_csv} 转换为 {chemin_jsonl}.")
    except Exception as e:
        print(f"转换过程中发生错误: {e}")
        exit()

# ====================================================================
# 5. 主程序 (应用 Camembert-bio 并对 Objet Médical 采样)
# ====================================================================

if __name__ == '__main__':
    # 核心改动：使用领域特定模型
    NOM_MODELE_PRE_ENTRAINE = 'almanach/camembert-bio-base'
    MAX_LONGUEUR = 128
    TAILLE_DE_LOT = 16
    EPOQUES = 3
    TAUX_APPRENTISSAGE = 2e-5

    CHEMIN_CSV_TRAIN = 'data/dataset/train_dataset.csv'
    CHEMIN_CSV_VALID = 'data/dataset/validation_dataset.csv'
    CHEMIN_CSV_TEST = 'data/dataset/test_dataset.csv'
    CHEMIN_JSONL_TRAIN = 'data/dataset/train_dataset.jsonl'
    CHEMIN_JSONL_VALID = 'data/dataset/validation_dataset.jsonl'
    CHEMIN_JSONL_TEST = 'data/dataset/test_dataset.jsonl'
    
    verifier_et_convertir_donnees(CHEMIN_JSONL_TRAIN, CHEMIN_CSV_TRAIN)
    verifier_et_convertir_donnees(CHEMIN_JSONL_VALID, CHEMIN_CSV_VALID)
    verifier_et_convertir_donnees(CHEMIN_JSONL_TEST, CHEMIN_CSV_TEST)
    
    appareil = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 使用 AutoTokenizer 自动加载与模型匹配的分词器
    tokenizer = AutoTokenizer.from_pretrained(NOM_MODELE_PRE_ENTRAINE)

    dataset_train = DatasetMultiTache(CHEMIN_JSONL_TRAIN, tokenizer, MAX_LONGUEUR)
    dataset_valid = DatasetMultiTache(CHEMIN_JSONL_VALID, tokenizer, MAX_LONGUEUR)
    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)

    # --- 对 Objet Médical 任务应用 WeightedRandomSampler ---
    print("\n--- 正在计算医疗对象分类的类别权重用于过采样 ---")
    objet_medical_labels = dataset_train.get_all_labels('objet_medical')
    class_counts = Counter(objet_medical_labels)
    num_samples = len(objet_medical_labels)
    
    # 为每个样本计算权重 (与类别频率成反比)
    weights = [num_samples / class_counts[label] for label in objet_medical_labels]
    
    # 初始化 WeightedRandomSampler
    sampler = WeightedRandomSampler(
        weights, 
        num_samples=num_samples,
        replacement=True
    )

    chargeur_donnees_train = DataLoader(dataset_train, batch_size=TAILLE_DE_LOT, sampler=sampler)
    chargeur_donnees_valid = DataLoader(dataset_valid, batch_size=TAILLE_DE_LOT, shuffle=False)
    chargeur_donnees_test = DataLoader(dataset_test, batch_size=TAILLE_DE_LOT, shuffle=False)

    num_intention = len(dataset_train.etiquettes_intention)
    num_objet_medical = len(dataset_train.etiquettes_objet_medical)
    num_sentiment = len(dataset_train.etiquettes_sentiment)
    
    # 定义每项任务的损失函数
    fonction_pertes = {
        'intention': nn.CrossEntropyLoss(),
        'objet_medical': nn.CrossEntropyLoss(),
        'sentiment': nn.CrossEntropyLoss()
    }

    print("\n--- 实验模式: Camembert-bio + WeightedRandomSampler (Objet Médical) ---")
    modele = MedicalMultiTache(NOM_MODELE_PRE_ENTRAINE, num_intention, num_objet_medical, num_sentiment).to(appareil)
    optimiseur = AdamW(modele.parameters(), lr=TAUX_APPRENTISSAGE)
    total_etapes = len(chargeur_donnees_train) * EPOQUES
    scheduler = get_linear_schedule_with_warmup(optimiseur, num_warmup_steps=0, num_training_steps=total_etapes)

    for epoque in range(EPOQUES):
        print(f"Époque {epoque + 1}/{EPOQUES}")
        perte_entrainement = entrainer(modele, chargeur_donnees_train, optimiseur, scheduler, fonction_pertes, appareil)
        print(f"Perte d'entraînement: {perte_entrainement:.4f}")
        metriques_validation = evaluer(modele, chargeur_donnees_valid, appareil)
        print(f"Métriques de validation: Acc_Intention={metriques_validation['acc_intention']:.4f} F1={metriques_validation['f1_intention']:.4f} | "
              f"Acc_Objet_Medical={metriques_validation['acc_objet_medical']:.4f} F1={metriques_validation['f1_objet_medical']:.4f} | "
              f"Acc_Sentiment={metriques_validation['acc_sentiment']:.4f} F1={metriques_validation['f1_sentiment']:.4f}")
    
    print("\n--- 在最终测试集上评估 ---")
    metriques_test = evaluer(modele, chargeur_donnees_test, appareil)
    print(f"Métriques de test: Acc_Intention={metriques_test['acc_intention']:.4f} F1={metriques_test['f1_intention']:.4f} | "
          f"Acc_Objet_Medical={metriques_test['acc_objet_medical']:.4f} F1={metriques_test['f1_objet_medical']:.4f} | "
          f"Acc_Sentiment={metriques_test['acc_sentiment']:.4f} F1={metriques_test['f1_sentiment']:.4f}")

    chemin_sauvegarde_modele = 'Camembert-bio_MedicalMultiTache_sampler_objet_medical.pth'
    torch.save(modele.state_dict(), chemin_sauvegarde_modele)
    print(f"\n模型已保存为 {chemin_sauvegarde_modele}")