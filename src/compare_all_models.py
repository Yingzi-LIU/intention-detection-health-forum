import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import BertModel, BertTokenizer
from sklearn.metrics import accuracy_score, f1_score
import json
import pandas as pd
import os

# ====================================================================
# 1. 模型和数据类
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
        df = df.rename(columns={'Sentences': 'texte', 'niveau1': 'intention', 'niveau2': 'objet_medical', 'niveau3': 'sentiment'})
        colonnes_requises = ['texte', 'intention', 'objet_medical', 'sentiment']
        if not all(col in df.columns for col in colonnes_requises):
            raise ValueError(f"CSV 文件不包含所有必需的列.")
        with open(chemin_jsonl, 'w', encoding='utf-8') as f:
            for _, row in df.iterrows():
                dictionnaire_donnees = {'texte': row['texte'], 'intention': row['intention'], 'objet_medical': row['objet_medical'], 'sentiment': row['sentiment']}
                f.write(json.dumps(dictionnaire_donnees, ensure_ascii=False) + '\n')
        print(f"成功将 {chemin_csv} 转换为 {chemin_jsonl}.")
    except Exception as e:
        print(f"转换过程中发生错误: {e}")
        exit()

# ====================================================================
# 2. 主程序
# ====================================================================

if __name__ == '__main__':
    # 定义所有要比较的模型
    modeles_a_comparer = {
        '原始模型 (损失加和)': 'BERT_MedicalMultiTache.pth',
        'Focal Loss 模型': 'BERT_MedicalMultiTache_focal.pth',
        '过采样模型': 'BERT_MedicalMultiTache_sampler.pth'
    }
    
    # 配置信息
    NOM_MODELE_BERT = 'bert-base-multilingual-cased'
    MAX_LONGUEUR = 128
    TAILLE_DE_LOT = 16
    CHEMIN_CSV_TEST = 'data/dataset/test_dataset.csv'
    CHEMIN_JSONL_TEST = 'data/dataset/test_dataset.jsonl'
    
    # 准备测试数据
    verifier_et_convertir_donnees(CHEMIN_JSONL_TEST, CHEMIN_CSV_TEST)
    appareil = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = BertTokenizer.from_pretrained(NOM_MODELE_BERT)
    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)
    chargeur_donnees_test = DataLoader(dataset_test, batch_size=TAILLE_DE_LOT, shuffle=False)

    num_intention = len(dataset_test.etiquettes_intention)
    num_objet_medical = len(dataset_test.etiquettes_objet_medical)
    num_sentiment = len(dataset_test.etiquettes_sentiment)

    # 依次评估每个模型并存储结果
    resultats_comparaison = {}
    for nom_modele, chemin_fichier in modeles_a_comparer.items():
        print(f"\n--- 正在评估: {nom_modele} ---")
        modele = BERT_MedicalMultiTache(NOM_MODELE_BERT, num_intention, num_objet_medical, num_sentiment).to(appareil)
        try:
            modele.load_state_dict(torch.load(chemin_fichier, map_location=appareil))
            metriques = evaluer(modele, chargeur_donnees_test, appareil)
            resultats_comparaison[nom_modele] = metriques
            print(f"评估完成. Acc_Sentiment={metriques['acc_sentiment']:.4f}, F1_Sentiment={metriques['f1_sentiment']:.4f}")
        except FileNotFoundError:
            print(f"错误: 找不到文件 {chemin_fichier}. 跳过该模型.")
    
    # 打印最终对比表格
    print("\n" + "="*120)
    print(" " * 45 + "多模型性能对比结果")
    print("="*120)
    
    entete_tableau = "{:<25} | {:<25} | {:<25} | {:<25}".format("任务", "原始模型 (F1 / Acc)", "Focal Loss 模型 (F1 / Acc)", "过采样模型 (F1 / Acc)")
    ligne_separateur = "-"*120
    
    print(entete_tableau)
    print(ligne_separateur)
    
    for tache in ['intention', 'objet_medical', 'sentiment']:
        f1_original = resultats_comparaison['原始模型 (损失加和)'][f'f1_{tache}']
        acc_original = resultats_comparaison['原始模型 (损失加和)'][f'acc_{tache}']
        f1_focal = resultats_comparaison['Focal Loss 模型'][f'f1_{tache}']
        acc_focal = resultats_comparaison['Focal Loss 模型'][f'acc_{tache}']
        f1_sampler = resultats_comparaison['过采样模型'][f'f1_{tache}']
        acc_sampler = resultats_comparaison['过采样模型'][f'acc_{tache}']
        
        print("{:<25} | F1={:.4f} / Acc={:.4f} | F1={:.4f} / Acc={:.4f} | F1={:.4f} / Acc={:.4f}".format(
            f"{tache.capitalize()}",
            f1_original, acc_original,
            f1_focal, acc_focal,
            f1_sampler, acc_sampler
        ))
    
    print("="*120)