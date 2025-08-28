import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import BertModel, BertTokenizer, get_linear_schedule_with_warmup
from torch.optim import AdamW
from sklearn.metrics import accuracy_score, f1_score
import json
import pandas as pd
import os
import torch.nn.functional as F
from collections import Counter

# ====================================================================
# 1. Dataset 类 (未更改)
# ====================================================================

class DatasetMultiTache(Dataset):
    def __init__(self, chemin_fichier, tokenizer, max_longueur):
        self.donnees = self._charger_donnees(chemin_fichier)
        self.tokenizer = tokenizer
        self.max_longueur = max_longueur

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
        
        intention = self.etiquettes_intention[item['intention']]
        objet_medical = self.etiquettes_objet_medical[item['objet_medical']]
        sentiment = self.etiquettes_sentiment[item['sentiment']]

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

# ====================================================================
# 2. 多任务模型 (未更改)
# ====================================================================

class BERT_MedicalMultiTache(nn.Module):
    def __init__(self, nom_modele_pre_entraine, num_intention, num_objet_medical, num_sentiment):
        super(BERT_MedicalMultiTache, self).__init__()
        
        self.bert = BertModel.from_pretrained(nom_modele_pre_entraine)
        
        self.classifieur_intention = nn.Linear(self.bert.config.hidden_size, num_intention)
        self.classifieur_objet_medical = nn.Linear(self.bert.config.hidden_size, num_objet_medical)
        self.classifieur_sentiment = nn.Linear(self.bert.config.hidden_size, num_sentiment)
        
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        
        logits_intention = self.classifieur_intention(pooled_output)
        logits_objet_medical = self.classifieur_objet_medical(pooled_output)
        logits_sentiment = self.classifieur_sentiment(pooled_output)
        
        return logits_intention, logits_objet_medical, logits_sentiment

# ====================================================================
# 3. 训练和评估函数 (未更改)
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
# 4. 数据转换函数 (未更改)
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
# 5. 主程序 (已修改 - 应用于 Intention)
# ====================================================================

if __name__ == '__main__':
    NOM_MODELE_BERT = 'bert-base-multilingual-cased'
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
    tokenizer = BertTokenizer.from_pretrained(NOM_MODELE_BERT)

    dataset_train = DatasetMultiTache(CHEMIN_JSONL_TRAIN, tokenizer, MAX_LONGUEUR)
    dataset_valid = DatasetMultiTache(CHEMIN_JSONL_VALID, tokenizer, MAX_LONGUEUR)
    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)

    # --- 关键改动：使用 WeightedRandomSampler 应用于 Intention 任务 ---
    print("\n--- 正在计算意图分类的类别权重用于过采样 ---")
    intention_labels = [item['intention'] for item in dataset_train.donnees]
    class_counts = Counter(intention_labels)
    num_samples = len(intention_labels)
    
    # 为每个样本计算权重 (与类别频率成反比)
    weights = [num_samples / class_counts[label] for label in intention_labels]
    
    # 初始化 WeightedRandomSampler
    sampler = WeightedRandomSampler(
        weights, 
        num_samples=num_samples, # 确保每个 epoch 的样本总数不变
        replacement=True # 允许重复采样
    )

    # 在 DataLoader 中使用 sampler 并禁用 shuffle
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

    print("\n--- 实验模式: WeightedRandomSampler (Intention) + 损失加和 ---")
    modele = BERT_MedicalMultiTache(NOM_MODELE_BERT, num_intention, num_objet_medical, num_sentiment).to(appareil)
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

    chemin_sauvegarde_modele = 'BERT_MedicalMultiTache_sampler_intention.pth'
    torch.save(modele.state_dict(), chemin_sauvegarde_modele)
    print(f"\n模型已保存为 {chemin_sauvegarde_modele}")