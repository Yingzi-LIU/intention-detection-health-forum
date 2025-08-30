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
# 1. Dataset Class
# ====================================================================

class DatasetMultiTache(Dataset):
    def __init__(self, chemin_fichier, tokenizer, max_longueur):
        self.donnees = self._charger_donnees(chemin_fichier)
        self.tokenizer = tokenizer
        self.max_longueur = max_longueur

        # Label mapping to IDs
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
        
        # Retrieve labels for each task
        intention = self.etiquettes_intention[item['intention']]
        objet_medical = self.etiquettes_objet_medical[item['objet_medical']]
        sentiment = self.etiquettes_sentiment[item['sentiment']]

        # Tokenize the text
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
# 2. Multi-task Model
# ====================================================================

class BERT_MedicalMultiTache(nn.Module):
    def __init__(self, nom_modele_pre_entraine, num_intention, num_objet_medical, num_sentiment):
        super(BERT_MedicalMultiTache, self).__init__()
        
        # Shared encoder
        self.bert = BertModel.from_pretrained(nom_modele_pre_entraine)
        
        # Independent classification heads
        self.classifieur_intention = nn.Linear(self.bert.config.hidden_size, num_intention)
        self.classifieur_objet_medical = nn.Linear(self.bert.config.hidden_size, num_objet_medical)
        self.classifieur_sentiment = nn.Linear(self.bert.config.hidden_size, num_sentiment)
        
    def forward(self, input_ids, attention_mask):
        # Pass through BERT encoder
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        
        # Use the [CLS] token output as the sentence representation
        pooled_output = outputs.pooler_output
        
        # Independent classification for each task
        logits_intention = self.classifieur_intention(pooled_output)
        logits_objet_medical = self.classifieur_objet_medical(pooled_output)
        logits_sentiment = self.classifieur_sentiment(pooled_output)
        
        return logits_intention, logits_objet_medical, logits_sentiment

# ====================================================================
# 3. Training and Evaluation Functions
# ====================================================================

def entrainer(modele, chargeur_donnees, optimiseur, scheduler, fonction_perte, appareil):
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
        
        perte_intention = fonction_perte(logits_intention, labels_intention)
        perte_objet_medical = fonction_perte(logits_objet_medical, labels_objet_medical)
        perte_sentiment = fonction_perte(logits_sentiment, labels_sentiment)
        
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
            
            # Save predictions and true labels
            predictions_intention.extend(torch.argmax(logits_intention, dim=1).cpu().numpy())
            labels_reels_intention.extend(labels_intention.cpu().numpy())
            
            predictions_objet_medical.extend(torch.argmax(logits_objet_medical, dim=1).cpu().numpy())
            labels_reels_objet_medical.extend(labels_objet_medical.cpu().numpy())

            predictions_sentiment.extend(torch.argmax(logits_sentiment, dim=1).cpu().numpy())
            labels_reels_sentiment.extend(labels_sentiment.cpu().numpy())

    # Calculate evaluation metrics
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
# 4. CSV to JSONL Conversion Function
# ====================================================================

def verifier_et_convertir_donnees(chemin_jsonl, chemin_csv):
    """
    Checks if the .jsonl file exists. If not, converts it from the .csv file.
    """
    if os.path.exists(chemin_jsonl):
        print(f"File {chemin_jsonl} found, conversion skipped.")
        return

    print(f"File {chemin_jsonl} not found, converting from {chemin_csv}...")
    if not os.path.exists(chemin_csv):
        print(f"Error: File {chemin_csv} not found. Please check the path.")
        exit()
    
    # Ensure the output directory exists
    repertoire_sortie = os.path.dirname(chemin_jsonl)
    if repertoire_sortie and not os.path.exists(repertoire_sortie):
        os.makedirs(repertoire_sortie)

    try:
        df = pd.read_csv(chemin_csv)
        
        # Rename columns to match script expectations
        df = df.rename(columns={
            'Sentences': 'texte',
            'niveau1': 'intention',
            'niveau2': 'objet_medical',
            'niveau3': 'sentiment'
        })

        colonnes_requises = ['texte', 'intention', 'objet_medical', 'sentiment']
        if not all(col in df.columns for col in colonnes_requises):
            raise ValueError(f"The CSV file does not contain all required columns after renaming. Ensure the following columns are included: {colonnes_requises}")

        with open(chemin_jsonl, 'w', encoding='utf-8') as f:
            for _, row in df.iterrows():
                dictionnaire_donnees = {
                    'texte': row['texte'],
                    'intention': row['intention'],
                    'objet_medical': row['objet_medical'],
                    'sentiment': row['sentiment']
                }
                f.write(json.dumps(dictionnaire_donnees, ensure_ascii=False) + '\n')
        
        print(f"Successfully converted {chemin_csv} to {chemin_jsonl}.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        exit()

# ====================================================================
# 5. Main Program
# ====================================================================

if __name__ == '__main__':
    # Hyperparameters
    NOM_MODELE_BERT = 'bert-base-multilingual-cased' # Multilingual model for French texts
    MAX_LONGUEUR = 128
    TAILLE_DE_LOT = 16
    EPOQUES = 3
    TAUX_APPRENTISSAGE = 2e-5

    # Data file paths
    CHEMIN_CSV_TRAIN = 'data/dataset/train_dataset.csv'
    CHEMIN_CSV_VALID = 'data/dataset/validation_dataset.csv'
    CHEMIN_CSV_TEST = 'data/dataset/test_dataset.csv'
    
    CHEMIN_JSONL_TRAIN = 'data/dataset/train_dataset.jsonl'
    CHEMIN_JSONL_VALID = 'data/dataset/validation_dataset.jsonl'
    CHEMIN_JSONL_TEST = 'data/dataset/test_dataset.jsonl'
    
    # Check and convert data format
    verifier_et_convertir_donnees(CHEMIN_JSONL_TRAIN, CHEMIN_CSV_TRAIN)
    verifier_et_convertir_donnees(CHEMIN_JSONL_VALID, CHEMIN_CSV_VALID)
    verifier_et_convertir_donnees(CHEMIN_JSONL_TEST, CHEMIN_CSV_TEST)
    
    appareil = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Initialize tokenizer
    tokenizer = BertTokenizer.from_pretrained(NOM_MODELE_BERT)

    # Load datasets
    dataset_train = DatasetMultiTache(CHEMIN_JSONL_TRAIN, tokenizer, MAX_LONGUEUR)
    dataset_valid = DatasetMultiTache(CHEMIN_JSONL_VALID, tokenizer, MAX_LONGUEUR)
    dataset_test = DatasetMultiTache(CHEMIN_JSONL_TEST, tokenizer, MAX_LONGUEUR)

    # Create DataLoaders
    chargeur_donnees_train = DataLoader(dataset_train, batch_size=TAILLE_DE_LOT, shuffle=True)
    chargeur_donnees_valid = DataLoader(dataset_valid, batch_size=TAILLE_DE_LOT, shuffle=False)
    chargeur_donnees_test = DataLoader(dataset_test, batch_size=TAILLE_DE_LOT, shuffle=False)

    # Instantiate the model
    num_intention = len(dataset_train.etiquettes_intention)
    num_objet_medical = len(dataset_train.etiquettes_objet_medical)
    num_sentiment = len(dataset_train.etiquettes_sentiment)
    
    modele = BERT_MedicalMultiTache(NOM_MODELE_BERT, num_intention, num_objet_medical, num_sentiment).to(appareil)

    # Configure optimizer and learning rate scheduler
    optimiseur = AdamW(modele.parameters(), lr=TAUX_APPRENTISSAGE)
    total_etapes = len(chargeur_donnees_train) * EPOQUES
    scheduler = get_linear_schedule_with_warmup(
        optimiseur,
        num_warmup_steps=0,
        num_training_steps=total_etapes
    )
    
    # Loss function
    fonction_perte = nn.CrossEntropyLoss()

    # Start training loop
    for epoque in range(EPOQUES):
        print(f"Epoch {epoque + 1}/{EPOQUES}")
        perte_entrainement = entrainer(modele, chargeur_donnees_train, optimiseur, scheduler, fonction_perte, appareil)
        print(f"Training Loss: {perte_entrainement:.4f}")
        
        metriques_validation = evaluer(modele, chargeur_donnees_valid, appareil)
        print(f"Validation Metrics: Acc_Intention={metriques_validation['acc_intention']:.4f} F1={metriques_validation['f1_intention']:.4f} | "
              f"Acc_Objet_Medical={metriques_validation['acc_objet_medical']:.4f} F1={metriques_validation['f1_objet_medical']:.4f} | "
              f"Acc_Sentiment={metriques_validation['acc_sentiment']:.4f} F1={metriques_validation['f1_sentiment']:.4f}")

    # Evaluate the final model on the test set
    print("\n--- Evaluation on Test Set ---")
    metriques_test = evaluer(modele, chargeur_donnees_test, appareil)
    print(f"Test Metrics: Acc_Intention={metriques_test['acc_intention']:.4f} F1={metriques_test['f1_intention']:.4f} | "
          f"Acc_Objet_Medical={metriques_test['acc_objet_medical']:.4f} F1={metriques_test['f1_objet_medical']:.4f} | "
          f"Acc_Sentiment={metriques_test['acc_sentiment']:.4f} F1={metriques_test['f1_sentiment']:.4f}")

    # Save the model
    torch.save(modele.state_dict(), 'BERT_MedicalMultiTache.pth')
    print("Model saved as BERT_MedicalMultiTache.pth")