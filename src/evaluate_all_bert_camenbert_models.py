import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import BertModel, BertTokenizer, CamembertModel, CamembertTokenizer, AutoModel, AutoTokenizer
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support
import json
import pandas as pd
import os
from collections import defaultdict

# ====================================================================
# 1. PATH CONFIGURATION
# ====================================================================

BASE_DIR = "/Users/liuyingzi/Downloads/intention-detection/intention-detection-health-forum"
MODEL_DIR = BASE_DIR
DATA_DIR = os.path.join(BASE_DIR, "data", "dataset")
RESULTS_DIR = os.path.join(BASE_DIR, "results_MTL")

if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

# ====================================================================
# 2. Dataset, Model and Helper Functions
# ====================================================================

class DatasetMultiTache(Dataset):
    def __init__(self, chemin_fichier, tokenizer, max_longueur):
        self.donnees = self._charger_donnees(chemin_fichier)
        self.tokenizer = tokenizer
        self.max_longueur = max_longueur
        # 核心修正：匹配你训练脚本中的标签映射
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
        
        # 使用 .get() 方法安全地获取标签，并提供默认值
        intention = self.etiquettes_intention.get(item['intention'], self.etiquettes_intention['fonction_phatique'])
        objet_medical = self.etiquettes_objet_medical.get(item['objet_medical'], self.etiquettes_objet_medical['NA_CATEGORY'])
        sentiment = self.etiquettes_sentiment.get(item['sentiment'], self.etiquettes_sentiment['non'])

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

class MultiTaskModel(nn.Module):
    def __init__(self, model_name, num_intention, num_objet_medical, num_sentiment):
        super(MultiTaskModel, self).__init__()
        if "camembert" in model_name.lower():
            self.encoder = AutoModel.from_pretrained(model_name)
        else:
            self.encoder = AutoModel.from_pretrained(model_name)
            
        self.classifieur_intention = nn.Linear(self.encoder.config.hidden_size, num_intention)
        self.classifieur_objet_medical = nn.Linear(self.encoder.config.hidden_size, num_objet_medical)
        self.classifieur_sentiment = nn.Linear(self.encoder.config.hidden_size, num_sentiment)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        logits_intention = self.classifieur_intention(pooled_output)
        logits_objet_medical = self.classifieur_objet_medical(pooled_output)
        logits_sentiment = self.classifieur_sentiment(pooled_output)
        return logits_intention, logits_objet_medical, logits_sentiment

def get_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(model_name)

def evaluer_modele(modele, chargeur_donnees, appareil, tache_nom, labels_map):
    modele.eval()
    predictions, labels_reels = [], []
    with torch.no_grad():
        for batch in chargeur_donnees:
            input_ids = batch['input_ids'].to(appareil)
            attention_mask = batch['attention_mask'].to(appareil)
            
            if tache_nom == 'intention':
                logits = modele(input_ids, attention_mask)[0]
                labels = batch['labels_intention'].to(appareil)
            elif tache_nom == 'objet_medical':
                logits = modele(input_ids, attention_mask)[1]
                labels = batch['labels_objet_medical'].to(appareil)
            elif tache_nom == 'sentiment':
                logits = modele(input_ids, attention_mask)[2]
                labels = batch['labels_sentiment'].to(appareil)
            else:
                raise ValueError("Invalid task name")
                
            predictions.extend(torch.argmax(logits, dim=1).cpu().numpy())
            labels_reels.extend(labels.cpu().numpy())
            
    f1_macro = f1_score(labels_reels, predictions, average='macro', zero_division=0)
    acc = accuracy_score(labels_reels, predictions)

    unique_labels = sorted(list(set(labels_reels)))
    
    precision_all, recall_all, f1_all, _ = precision_recall_fscore_support(labels_reels, predictions, labels=unique_labels, average=None, zero_division=0)

    per_label_metrics = defaultdict(lambda: {'Precision': 0.0, 'Recall': 0.0, 'F1-Score': 0.0})
    
    all_labels_list = sorted(labels_map.items(), key=lambda item: item[1])

    for i, label_value in enumerate(unique_labels):
        label_name = next(item[0] for item in all_labels_list if item[1] == label_value)
        per_label_metrics[label_name] = {
            'Precision': precision_all[i],
            'Recall': recall_all[i],
            'F1-Score': f1_all[i]
        }
        
    return {'f1_macro': f1_macro, 'accuracy': acc, 'per_label_metrics': per_label_metrics}

def verifier_et_convertir_donnees(chemin_jsonl, chemin_csv):
    if os.path.exists(chemin_jsonl):
        return
    if not os.path.exists(chemin_csv):
        print(f"Error: CSV file not found at {chemin_csv}. Please check the path.")
        exit()
    try:
        df = pd.read_csv(chemin_csv)
        df = df.rename(columns={'Sentences': 'texte', 'niveau1': 'intention', 'niveau2': 'objet_medical', 'niveau3': 'sentiment'})
        with open(chemin_jsonl, 'w', encoding='utf-8') as f:
            for _, row in df.iterrows():
                dictionnaire_donnees = {'texte': row['texte'], 'intention': row['intention'], 'objet_medical': row['objet_medical'], 'sentiment': row['sentiment']}
                f.write(json.dumps(dictionnaire_donnees, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"Conversion failed: {e}")
        exit()

# ====================================================================
# 3. Main Program
# ====================================================================

if __name__ == '__main__':
    MAX_LONGUEUR = 128
    TAILLE_DE_LOT = 16
    
    CHEMIN_CSV_TEST = os.path.join(DATA_DIR, 'test_dataset.csv')
    CHEMIN_JSONL_TEST = os.path.join(DATA_DIR, 'test_dataset.jsonl')
    
    verifier_et_convertir_donnees(CHEMIN_JSONL_TEST, CHEMIN_CSV_TEST)
    
    appareil = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model_files = [f for f in os.listdir(MODEL_DIR) if f.endswith('.pth')]
    if not model_files:
        print(f"Error: No .pth model files found in {MODEL_DIR}. Please check the directory path and file extensions.")
        exit()

    all_results = defaultdict(dict)
    
    first_model_name_base = os.path.splitext(model_files[0])[0]
    
    if "camembert" in first_model_name_base.lower() or "camem" in first_model_name_base.lower():
        initial_encoder_name = "almanach/camembert-bio-base"
    else:
        initial_encoder_name = "bert-base-multilingual-cased"

    tokenizer = get_tokenizer(initial_encoder_name)

    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)
    num_intention = len(dataset_test.etiquettes_intention)
    num_objet_medical = len(dataset_test.etiquettes_objet_medical)
    num_sentiment = len(dataset_test.etiquettes_sentiment)
    
    chargeur_donnees_test = DataLoader(dataset_test, batch_size=TAILLE_DE_LOT, shuffle=False)

    for model_file in model_files:
        model_name_base = os.path.splitext(model_file)[0]
        
        print(f"\n--- Evaluating {model_file} ---")
        try:
            if "camembert" in model_name_base.lower() or "camem" in model_name_base.lower():
                current_encoder_name = "almanach/camembert-bio-base"
            else:
                current_encoder_name = "bert-base-multilingual-cased"

            current_tokenizer = get_tokenizer(current_encoder_name)

            dataset_test_current = DatasetMultiTache(CHEMIN_JSONL_TEST, current_tokenizer, MAX_LONGUEUR)
            chargeur_donnees_test_current = DataLoader(dataset_test_current, batch_size=TAILLE_DE_LOT, shuffle=False)
            
            modele = MultiTaskModel(current_encoder_name, num_intention, num_objet_medical, num_sentiment).to(appareil)
            
            original_state_dict = torch.load(os.path.join(MODEL_DIR, model_file), map_location=appareil)
            
            renamed_state_dict = {}
            for key, val in original_state_dict.items():
                if key.startswith('camembert.'):
                    renamed_key = key.replace('camembert.', 'encoder.')
                elif key.startswith('camemencoder.'):
                    renamed_key = key.replace('camemencoder.', 'encoder.')
                elif key.startswith('bert.'):
                    renamed_key = key.replace('bert.', 'encoder.')
                elif key.startswith('model.'):
                    renamed_key = key.replace('model.', 'encoder.')
                else:
                    renamed_key = key
                renamed_state_dict[renamed_key] = val
            
            modele.load_state_dict(renamed_state_dict, strict=False)
            
            results_intention = evaluer_modele(modele, chargeur_donnees_test_current, appareil, 'intention', dataset_test_current.etiquettes_intention)
            results_objet_medical = evaluer_modele(modele, chargeur_donnees_test_current, appareil, 'objet_medical', dataset_test_current.etiquettes_objet_medical)
            results_sentiment = evaluer_modele(modele, chargeur_donnees_test_current, appareil, 'sentiment', dataset_test_current.etiquettes_sentiment)

            all_results[model_name_base]['intention'] = results_intention
            all_results[model_name_base]['objet_medical'] = results_objet_medical
            all_results[model_name_base]['sentiment'] = results_sentiment
            
        except Exception as e:
            print(f"Error evaluating {model_file}: {e}")
            continue

    if not all_results:
        print("\nNo models were successfully evaluated. Please check your model files and their integrity.")
        exit()

    # --- 更改部分开始 ---
    output_json_path = os.path.join(RESULTS_DIR, 'evaluation_results.json')
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)
    print(f"\nAll evaluation results saved to {output_json_path}")

    # 将结果转换为DataFrame并保存为CSV
    csv_data = []
    for model_name, tasks in all_results.items():
        row_data = {"Model": model_name}
        for task_name, metrics in tasks.items():
            row_data[f"{task_name}_f1_macro"] = metrics["f1_macro"]
            row_data[f"{task_name}_accuracy"] = metrics["accuracy"]
        csv_data.append(row_data)

    df_results = pd.DataFrame(csv_data)
    output_csv_path = os.path.join(RESULTS_DIR, 'evaluation_results.csv')
    df_results.to_csv(output_csv_path, index=False)
    print(f"Evaluation results also saved to {output_csv_path}")
    # --- 更改部分结束 ---

    print("\n" + "="*120)
    print(" " * 40 + "最终评估结果")
    print("="*120)

    for task in ['intention', 'objet_medical', 'sentiment']:
        print(f"\n任务: {task.capitalize()}")
        print("-" * 120)
        
        header_macro = "{:<30} | {:<20} | {:<20}".format("模型", "F1 (宏平均)", "准确率")
        print(header_macro)
        print("-" * 120)
        for model_name, results in all_results.items():
            if task in results:
                line_macro = "{:<30} | {:<20.4f} | {:<20.4f}".format(
                    model_name,
                    results[task]['f1_macro'],
                    results[task]['accuracy']
                )
                print(line_macro)
        
        print("\n各类别指标:")
        print("-" * 120)
        
        if all_results:
            first_model_name = list(all_results.keys())[0]
            if task in all_results[first_model_name]:
                labels_list = sorted(list(all_results[first_model_name][task]['per_label_metrics'].keys()))
                
                header_labels = "{:<30} | {:<15} | {:<15} | {:<15}".format("模型", "类别", "F1-Score", "召回率")
                print(header_labels)
                print("-" * 120)
                
                for model_name, results in all_results.items():
                    if task in results:
                        is_first_line = True
                        for label in labels_list:
                            metrics = results[task]['per_label_metrics'].get(label, {'F1-Score': 0.0, 'Recall': 0.0})
                            if is_first_line:
                                line_labels = "{:<30} | {:<15} | {:<15.4f} | {:<15.4f}".format(
                                    model_name,
                                    label,
                                    metrics['F1-Score'],
                                    metrics['Recall']
                                )
                                is_first_line = False
                            else:
                                line_labels = "{:<30} | {:<15} | {:<15.4f} | {:<15.4f}".format(
                                    "",
                                    label,
                                    metrics['F1-Score'],
                                    metrics['Recall']
                                )
                            print(line_labels)
                        print("-" * 120)
    print("="*120)