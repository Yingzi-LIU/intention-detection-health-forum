import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import BertModel, BertTokenizer
from sklearn.metrics import accuracy_score, f1_score
import json
import pandas as pd
import os

# ====================================================================
# 1. 用于评估的必要类和函数
# ====================================================================

# 重新定义模型类 (必须和训练时完全一致)
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

# 重新定义 Dataset 类
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

# 评估函数
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

# 数据转换函数
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
    # 要比较的模型文件名
    CHEMIN_MODELE_ORIGINAL = 'BERT_MedicalMultiTache.pth'
    CHEMIN_MODELE_FOCAL = 'BERT_MedicalMultiTache_focal.pth'
    
    # 配置信息 (必须和训练时一致)
    NOM_MODELE_BERT = 'bert-base-multilingual-cased'
    MAX_LONGUEUR = 128
    TAILLE_DE_LOT = 16
    CHEMIN_CSV_TEST = 'data/dataset/test_dataset.csv'
    CHEMIN_JSONL_TEST = 'data/dataset/test_dataset.jsonl'
    
    verifier_et_convertir_donnees(CHEMIN_JSONL_TEST, CHEMIN_CSV_TEST)
    appareil = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = BertTokenizer.from_pretrained(NOM_MODELE_BERT)
    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)
    chargeur_donnees_test = DataLoader(dataset_test, batch_size=TAILLE_DE_LOT, shuffle=False)

    num_intention = len(dataset_test.etiquettes_intention)
    num_objet_medical = len(dataset_test.etiquettes_objet_medical)
    num_sentiment = len(dataset_test.etiquettes_sentiment)

    # 实例化并加载两个模型
    modele_original = BERT_MedicalMultiTache(NOM_MODELE_BERT, num_intention, num_objet_medical, num_sentiment).to(appareil)
    modele_focal = BERT_MedicalMultiTache(NOM_MODELE_BERT, num_intention, num_objet_medical, num_sentiment).to(appareil)

    try:
        modele_original.load_state_dict(torch.load(CHEMIN_MODELE_ORIGINAL, map_location=appareil))
        print(f"原始模型 ({CHEMIN_MODELE_ORIGINAL}) 加载成功.")
    except FileNotFoundError:
        print(f"错误: 找不到文件 {CHEMIN_MODELE_ORIGINAL}. 请检查文件路径和名称.")
        exit()
    try:
        modele_focal.load_state_dict(torch.load(CHEMIN_MODELE_FOCAL, map_location=appareil))
        print(f"Focal Loss 模型 ({CHEMIN_MODELE_FOCAL}) 加载成功.")
    except FileNotFoundError:
        print(f"错误: 找不到文件 {CHEMIN_MODELE_FOCAL}. 请检查文件路径和名称.")
        exit()
    
    # 在测试集上评估两个模型
    print("\n--- 正在评估原始模型(损失加和) ---")
    metriques_original = evaluer(modele_original, chargeur_donnees_test, appareil)

    print("\n--- 正在评估 Focal Loss 模型 ---")
    metriques_focal = evaluer(modele_focal, chargeur_donnees_test, appareil)

    # 打印对比结果
    print("\n" + "="*80)
    print(" " * 20 + "模型性能对比结果")
    print("="*80)
    
    entete_tableau = "{:<20} | {:<25} | {:<25}".format("任务", "原始模型 (F1 / Acc)", "Focal Loss 模型 (F1 / Acc)")
    ligne_separateur = "-"*80
    
    print(entete_tableau)
    print(ligne_separateur)
    
    print("{:<20} | F1={:.4f} / Acc={:.4f} | F1={:.4f} / Acc={:.4f}".format("意图 (Intention)", metriques_original['f1_intention'], metriques_original['acc_intention'], metriques_focal['f1_intention'], metriques_focal['acc_intention']))
    print("{:<20} | F1={:.4f} / Acc={:.4f} | F1={:.4f} / Acc={:.4f}".format("医学对象 (Medical Object)", metriques_original['f1_objet_medical'], metriques_original['acc_objet_medical'], metriques_focal['f1_objet_medical'], metriques_focal['acc_objet_medical']))
    print("{:<20} | F1={:.4f} / Acc={:.4f} | F1={:.4f} / Acc={:.4f}".format("情感 (Sentiment)", metriques_original['f1_sentiment'], metriques_original['acc_sentiment'], metriques_focal['f1_sentiment'], metriques_focal['acc_sentiment']))
    
    print("="*80)

print("\n脚本运行完毕。")