import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import json
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report
import time
import random
import argparse

# Load environment variables from .env file
load_dotenv()

# --- Parse command line arguments ---
parser = argparse.ArgumentParser(description='Process medical forum data with OpenAI API.')
parser.add_argument('--num_samples', type=int, default=None,
                    help='Number of test samples to process (default: all)')
parser.add_argument('--model_name', type=str, default='gpt-4o',
                    help='OpenAI model name to use (default: gpt-4o)')
args = parser.parse_args()

try:
    API_KEY = os.getenv('OPENAI_API_KEY') # Changed from GEMINI_API_KEY
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY not found in .env file.")
    
    client = OpenAI(api_key=API_KEY) # Initialize OpenAI client
except Exception as e:
    print(f"Erreur lors du chargement de la clé API : {e}")
    print("Veuillez vous assurer d'avoir un fichier .env dans le même répertoire avec votre clé API OpenAI nommée 'OPENAI_API_KEY'.")
    exit()

# --- 2. Configure OpenAI API ---
# Model is initialized via client, and model name is passed in args
model_name = args.model_name

# --- 3. Load dataset ---
test_file_path = 'data/dataset/test_dataset.csv'

try:
    test_df = pd.read_csv(test_file_path)
    print(f"Jeu de test chargé avec succès : {len(test_df)} données")
except FileNotFoundError:
    print("Veuillez vous assurer que le fichier 'test_dataset.csv' existe dans le chemin spécifié.")
    exit()

# Data preprocessing: handle NA_CATEGORY
def process_categories(df):
    return df

test_df = process_categories(test_df)

# --- 4. Load few-shot examples ---
try:
    few_shot_file_path = 'data/few_shot_examples.csv'
    few_shot_df = pd.read_csv(few_shot_file_path)
    few_shot_data = few_shot_df.to_dict('records')
    print(f"Few-shot examples download successful: {len(few_shot_data)} data")
except FileNotFoundError:
    print(f"please make sure 'few_shot_examples.csv' exist in '{few_shot_file_path}' .")
    exit()
except Exception as e:
    print(f"download example unsuccessful: {e}")
    exit()

# --- 5. Build Prompt Function ---
def create_few_shot_prompt(text_to_classify, few_shot_examples):
    """
    Builds a prompt based on few-shot examples.
    """
    few_shot_section = ""
    for ex in few_shot_examples:
        
        emotion_label = ex['niveau3']

        few_shot_section += f"""
    **(Exemple d'entrée):**
    "{ex['Sentences']}"

    **(Exemple de sortie):**
    ```json
    {{
        "intention_generale": "{ex['niveau1']}",
        "objet_medical": "{ex['niveau2']}",
        "emotion": "{emotion_label}"
    }}
    ```
    """

    prompt = f"""
    Vous êtes un assistant professionnel d'analyse de contenu de forum médical français. Vous devez analyser et classer les textes publiés par les utilisateurs sur un forum médical français.
    Veuillez classer le texte fourni selon les trois dimensions suivantes et afficher les résultats au format JSON :

    1.  **Niveau de l'intention générale** :
        * "recherche_information" (Recherche d'informations)
        * "partage_experience" (Partage d'expérience)
        * "fonction_phatique" (Salutations ou maintien de la communication)

    2.  **Niveau de l'objet médical** :
        * "symptome" (Symptôme)
        * "traitement" (Traitement)
        * "diagnostique" (Diagnostic)
        * "NA_CATEGORY" (Non pertinent) (Si le contenu du texte ne concerne pas un objet médical spécifique)

    3.  **Niveau émotionnel** :
        * "positif" (Positif)
        * "negatif" (Négatif)
        * "non" (Neutre)

    Veuillez vous assurer que la sortie est strictement au format JSON et contient les trois clés de niveau supérieur : `intention_generale`, `objet_medical`, `emotion`.
    Si une catégorie n'est pas applicable, veuillez la définir sur "NA_CATEGORY".

    ---
    **Few-Shot (Exemples Few-Shot):**
    {few_shot_section}
    ---
    **(Texte à classifier):**
    "{text_to_classify}"
    """
    return prompt

# --- 6. Classification inference for all test set data ---
predicted_niveau1 = []
predicted_niveau2 = []
predicted_niveau3 = []
actual_niveau1 = test_df['niveau1'].tolist()
actual_niveau2 = test_df['niveau2'].tolist()
actual_niveau3 = test_df['niveau3'].tolist() 

# get total samples
total_test_samples = len(test_df)

# If num_samples is specified, limit to that number
if args.num_samples is not None:
    total_test_samples = min(args.num_samples, total_test_samples)
    test_df = test_df.head(total_test_samples)
    print(f"\n--- Début de l'inférence de classification pour les {total_test_samples} premiers exemples du jeu de test ---")
else:
    print(f"\n--- Début de l'inférence de classification pour les {total_test_samples} exemples du jeu de test ---")

# Iterate through test samples
for index, row in test_df.iterrows():
    text = row['Sentences']
    prompt = create_few_shot_prompt(text, few_shot_data)

    retries = 0
    max_retries = 5  # Maximum number of retries
    base_delay = 5   # Initial delay in seconds

    while retries < max_retries:
        try:
            response = client.chat.completions.create( # Changed to OpenAI chat completion
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a professional French medical forum content analysis assistant. You need to analyze and classify user texts posted on a French medical forum."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=200,
                response_format={"type": "json_object"} # Request JSON output
            )

            raw_output = response.choices[0].message.content.strip()
            classified_result = json.loads(raw_output)

            predicted_niveau1.append(classified_result.get('intention_generale', '未知'))
            predicted_niveau2.append(classified_result.get('objet_medical', '未知'))
            predicted_niveau3.append(classified_result.get('emotion', 'inconnu')) # Get from 'emotion' key

            # If successful, break out of the retry loop
            break

        except Exception as e:
            if "429" in str(e) or "Rate limit" in str(e): # Check for rate limit errors
                retries += 1
                wait_time = base_delay * (2 ** (retries - 1)) + random.uniform(0, 1) # Exponential backoff with jitter
                print(f"Erreur de quota (429) rencontrée lors du traitement du texte ID {row['ID']}. Tentative {retries}/{max_retries}, attente de {wait_time:.2f} secondes...")
                time.sleep(wait_time)
            else:
                # Other errors, no retry
                print(f"Échec du traitement du texte ID {row['ID']} : {e}")
                print(f"Sortie brute du modèle :\n{raw_output if 'raw_output' in locals() else 'Aucune réponse'}")
                predicted_niveau1.append('inconnu')
                predicted_niveau2.append('inconnu')
                predicted_niveau3.append('inconnu') # Add 'inconnu' on failure
                break # Break out of retry loop, process next sample
    else: # If all retries failed
        print(f"Le traitement du texte ID {row['ID']} a échoué après {max_retries} tentatives, cette entrée est ignorée.")
        predicted_niveau1.append('inconnu')
        predicted_niveau2.append('inconnu')
        predicted_niveau3.append('inconnu') # Add 'inconnu' on failure

    # Progress update every 10 samples
    if (index + 1) % 10 == 0 or (index + 1) == total_test_samples:
        print(f"{index + 1}/{total_test_samples} données traitées...")

print("\n--- Inférence de classification terminée ---")

# --- 7. Evaluate model performance (evaluate on all test set data) ---

# Note: The actual_niveauX lists no longer need slicing, as the predicted list now contains all data
actual_niveau1_full = actual_niveau1
actual_niveau2_full = actual_niveau2
actual_niveau3_full = actual_niveau3 # Changed to a single niveau3


def evaluate_category(actual_labels, predicted_labels, category_name):
    print(f"\n--- Évaluation : {category_name} ---")

    # Filter out 'inconnu' predictions, only evaluate successfully classified parts
    filtered_actual = []
    filtered_predicted = []
    for a, p in zip(actual_labels, predicted_labels):
        if p != 'inconnu':
            filtered_actual.append(a)
            filtered_predicted.append(p)

    if not filtered_actual:
        print(f"Aucune donnée classifiée avec succès pour évaluer {category_name}.")
        return

    # Get all possible labels to ensure completeness of the report.
    # Get all possible labels from the complete dataset to ensure completeness of the report.

    # For niveau1
    if category_name == "Niveau d'intention (Niveau 1)":
        # Only use underlined labels defined in the prompt
        all_possible_labels = ['fonction_phatique', 'partage_experience', 'recherche_information']

    # For niveau2
    elif category_name == "Niveau d'objet médical (Niveau 2)":
        # Only use specified labels
        all_possible_labels = ['symptome', 'traitement', 'diagnostique', 'NA_CATEGORY']

    # For niveau3 (emotion)
    elif category_name == "Niveau émotionnel (Niveau 3)":
        # Only use specified labels
        all_possible_labels = ['positif', 'negatif', 'non']
    else:
        all_possible_labels = sorted(list(set(filtered_actual + filtered_predicted))) # Fallback

    # Print classification report
    print(classification_report(filtered_actual, filtered_predicted, labels=all_possible_labels, zero_division=0))

    accuracy = accuracy_score(filtered_actual, filtered_predicted)
    print(f"Précision (Accuracy) : {accuracy:.4f}")


# Evaluate all data
evaluate_category(actual_niveau1_full, predicted_niveau1, "Niveau d'intention (Niveau 1)")
evaluate_category(actual_niveau2_full, predicted_niveau2, "Niveau d'objet médical (Niveau 2)")
evaluate_category(actual_niveau3_full, predicted_niveau3, "Niveau émotionnel (Niveau 3)")

print("\n--- Évaluation terminée ---")