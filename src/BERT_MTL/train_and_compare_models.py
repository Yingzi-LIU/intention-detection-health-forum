import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import BertModel, BertTokenizer, get_linear_schedule_with_warmup
from torch.optim import AdamW
from sklearn.metrics import accuracy_score, f1_score
import json
import pandas as pd
import os

# ====================================================================
# 1. Dataset, Model and Helper Functions
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
    f1_intention_macro = f1_score(labels_reels_intention, predictions_intention, average='macro', zero_division=0)
    acc_objet_medical = accuracy_score(labels_reels_objet_medical, predictions_objet_medical)
    f1_objet_medical_macro = f1_score(labels_reels_objet_medical, predictions_objet_medical, average='macro', zero_division=0)
    acc_sentiment = accuracy_score(labels_reels_sentiment, predictions_sentiment)
    f1_sentiment_macro = f1_score(labels_reels_sentiment, predictions_sentiment, average='macro', zero_division=0)
    
    return {
        'acc_intention': acc_intention, 'f1_intention_macro': f1_intention_macro,
        'acc_objet_medical': acc_objet_medical, 'f1_objet_medical_macro': f1_objet_medical_macro,
        'acc_sentiment': acc_sentiment, 'f1_sentiment_macro': f1_sentiment_macro
    }

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

def train_model(train_data_path, model_path, tokenizer, num_intention, num_objet_medical, num_sentiment, appareil, EPOQUES, TAILLE_DE_LOT, TAUX_APPRENTISSAGE):
    print(f"\n--- Training model on {train_data_path} ---")
    dataset_train = DatasetMultiTache(train_data_path, tokenizer, 128)
    chargeur_donnees_train = DataLoader(dataset_train, batch_size=TAILLE_DE_LOT, shuffle=True)
    
    modele = BERT_MedicalMultiTache('bert-base-multilingual-cased', num_intention, num_objet_medical, num_sentiment).to(appareil)
    optimiseur = AdamW(modele.parameters(), lr=TAUX_APPRENTISSAGE)
    total_etapes = len(chargeur_donnees_train) * EPOQUES
    scheduler = get_linear_schedule_with_warmup(optimiseur, num_warmup_steps=0, num_training_steps=total_etapes)
    fonction_perte = nn.CrossEntropyLoss()
    
    for epoque in range(EPOQUES):
        modele.train()
        perte_totale = 0
        for batch in chargeur_donnees_train:
            optimiseur.zero_grad()
            input_ids = batch['input_ids'].to(appareil)
            attention_mask = batch['attention_mask'].to(appareil)
            labels_intention = batch['labels_intention'].to(appareil)
            labels_objet_medical = batch['labels_objet_medical'].to(appareil)
            labels_sentiment = batch['labels_sentiment'].to(appareil)
            logits_intention, logits_objet_medical, logits_sentiment = modele(input_ids, attention_mask)
            perte = fonction_perte(logits_intention, labels_intention) + fonction_perte(logits_objet_medical, labels_objet_medical) + fonction_perte(logits_sentiment, labels_sentiment)
            perte.backward()
            torch.nn.utils.clip_grad_norm_(modele.parameters(), 1.0)
            optimiseur.step()
            scheduler.step()
            perte_totale += perte.item()
        print(f"Epoch {epoque + 1}/{EPOQUES}, Loss: {perte_totale / len(chargeur_donnees_train):.4f}")
    
    torch.save(modele.state_dict(), model_path)
    print(f"Model saved to {model_path}")

# ====================================================================
# 2. Main Program
# ====================================================================

if __name__ == '__main__':
    # Define all experiments to run
    experiments = {
        'Baseline Model': {'train_data': 'data/dataset/train_dataset.jsonl', 'model_path': 'BERT_MedicalMultiTache.pth'},
        'Oversampling Model': {'train_data': 'data/dataset/train_dataset_sampler.jsonl', 'model_path': 'BERT_MedicalMultiTache_sampler.pth'},
        'Back-translation Model': {'train_data': 'data/dataset/train_dataset_backtrans.jsonl', 'model_path': 'BERT_MedicalMultiTache_backtrans.pth'},
        'Keyword Model': {'train_data': 'data/dataset/train_dataset_keywords.jsonl', 'model_path': 'BERT_MedicalMultiTache_keywords.pth'},
        'Combined Model': {'train_data': 'data/dataset/train_dataset_combined.jsonl', 'model_path': 'BERT_MedicalMultiTache_combined.pth'}
    }

    # configurations
    NOM_MODELE_BERT = 'bert-base-multilingual-cased'
    MAX_LONGUEUR = 128
    TAILLE_DE_LOT = 16
    EPOQUES = 3
    TAUX_APPRENTISSAGE = 2e-5

    CHEMIN_CSV_TRAIN = 'data/dataset/train_dataset.csv'
    CHEMIN_CSV_TEST = 'data/dataset/test_dataset.csv'
    CHEMIN_JSONL_TRAIN = 'data/dataset/train_dataset.jsonl'
    CHEMIN_JSONL_TEST = 'data/dataset/test_dataset.jsonl'
    
    verifier_et_convertir_donnees(CHEMIN_JSONL_TRAIN, CHEMIN_CSV_TRAIN)
    verifier_et_convertir_donnees(CHEMIN_JSONL_TEST, CHEMIN_CSV_TEST)
    
    appareil = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = BertTokenizer.from_pretrained(NOM_MODELE_BERT)
    
    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)
    chargeur_donnees_test = DataLoader(dataset_test, batch_size=TAILLE_DE_LOT, shuffle=False)
    num_intention = len(dataset_test.etiquettes_intention)
    num_objet_medical = len(dataset_test.etiquettes_objet_medical)
    num_sentiment = len(dataset_test.etiquettes_sentiment)

    # Train and save all models
    for exp_name, config in experiments.items():
        if os.path.exists(config['model_path']):
            print(f"\nModel {exp_name} already exists, skipping training.")
            continue
        train_model(config['train_data'], config['model_path'], tokenizer, num_intention, num_objet_medical, num_sentiment, appareil, EPOQUES, TAILLE_DE_LOT, TAUX_APPRENTISSAGE)

    # Evaluate all models and print comparison table
    resultats_comparaison = {}
    print("\n" + "="*80)
    print(" " * 25 + "Starting evaluation of all models")
    print("="*80)

    for exp_name, config in experiments.items():
        print(f"\n--- Evaluating: {exp_name} ---")
        modele = BERT_MedicalMultiTache(NOM_MODELE_BERT, num_intention, num_objet_medical, num_sentiment).to(appareil)
        try:
            modele.load_state_dict(torch.load(config['model_path'], map_location=appareil))
            metriques = evaluer(modele, chargeur_donnees_test, appareil)
            resultats_comparaison[exp_name] = metriques
            print("Evaluation complete.")
        except FileNotFoundError:
            print(f"Error: File {config['model_path']} not found. Skipping this model.")

    print("\n" + "="*160)
    print(" " * 65 + "Final Performance Comparison Results")
    print("="*160)
    
    model_names = list(resultats_comparaison.keys())
    
    for tache in ['intention', 'objet_medical', 'sentiment']:
        print(f"\nTask: {tache.capitalize()}")
        
        metrics_to_show = {
            'F1 (Macro)': f'f1_{tache}_macro',
            'Accuracy': f'acc_{tache}'
        }

        entete_macro = "{:<25} |".format("Metric")
        for name in model_names:
            entete_macro += f" {name:<25} |"
        print("-" * (25 + len(model_names) * 28))
        print(entete_macro)
        print("-" * (25 + len(model_names) * 28))
        
        for metric_display_name, metric_key in metrics_to_show.items():
            ligne_metrique = "{:<25} |".format(metric_display_name)
            for name in model_names:
                score = resultats_comparaison.get(name, {}).get(metric_key, 'N/A')
                ligne_metrique += f" {score:<25.4f} |" if isinstance(score, float) else f" {score:<25} |"
            print(ligne_metrique)

    print("="*160)