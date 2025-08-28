import json
import random
import os
import pandas as pd
from collections import Counter
from transformers import pipeline

# 你的关键词字典
keyword_dict = {'overall_intent': { 'recherche d\'information': ['question', 'savoir', 'quelqu’un', 'aider', 'renseignement', 'explication', 'avis', 'conseil', 'expérience (chez les autres)', 'information', 'réponse', 'témoignage', 'qui a déjà', 'est-ce que', 'comment'], 'partage d\'expérience': ['moi', 'j’ai', 'vécu', 'mon cas', 'personnellement', 'ça m’est arrivé', 'depuis', 'après', 'je souffre', 'quand j’ai', 'pour ma part', 'autrefois', 'chez moi', 'je raconte', 'expérience'], 'fonction phatique': ['bonjour', 'salut', 'merci', 'courage', 'bisous', 'bonne journée', 'à bientôt', 'tiens', 'coucou', 'au revoir', 'bonne chance', 'prends soin', 'je pense à toi', 'bravo', 'félicitations'] }, 'medical_object': { 'symptome': ['douleur', 'fièvre', 'toux', 'fatigue', 'nausée', 'vomissement', 'mal de tête', 'vertige', 'saignement', 'diarrhée', 'essoufflement', 'crampe', 'frisson', 'démangeaison', 'inflammation'], 'traitement': ['médicament', 'antibiotique', 'comprimé', 'injection', 'ordonnance', 'opération', 'chirurgie', 'perfusion', 'thérapie', 'séance', 'pommade', 'crème', 'gélule', 'traitement', 'protocole'], 'diagnostique': ['médecin', 'rendez-vous', 'examen', 'analyse', 'prise de sang', 'radio', 'IRM', 'scanner', 'consultation', 'diagnostic', 'spécialiste', 'test', 'résultat', 'donnée', 'explication', 'bilan', 'contrôle'], 'NA_CATEGORY': ['bonjour', 'salut', 'merci', 'courage', 'bisous', 'bonne journée', 'à bientôt', 'tiens', 'coucou', 'au revoir', 'bonne chance', 'prends soin', 'je pense à toi', 'bravo', 'félicitations'] }, 'emotion': { 'positif': ['amélioration', 'guérison', 'efficace', 'solution', 'soulagement', 'espoir', 'bon', 'normal', 'rassuré', 'progrès', 'confiance', 'réussite', 'stable', 'bien', 'positif', 'joie', 'bravo', 'félicitations', 'merci'], 'negatif': ['douleur', 'pire', 'rechute', 'inefficace', 'aggravation', 'souffrance', 'inquiétant', 'mauvais', 'problème', 'compliqué', 'peur', 'triste', 'inquiétude', 'négatif', 'désespoir', 'angoisse', 'stress', 'honte', 'colère', 'déception', 'culpabilité'], 'non': ['neutre', 'bonsoir', 'bonjour', 'merci', 'cordialement', 'accord', 'rapport', 'statistique', 'description', 'message', 'donnée', 'explication', 'résultat', 'réponse', 'conseils']}}

def load_data(file_path):
    """Loads data from a .jsonl file."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def save_data(data, file_path):
    """Saves data to a .jsonl file."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    print(f"Dataset saved to {file_path}")

def oversample_minority_classes(data, task_keys, oversample_ratio=1.0):
    """General function to oversample minority classes for multiple tasks."""
    augmented_data = data.copy()
    for task_key in task_keys:
        task_labels = [item[task_key] for item in augmented_data]
        label_counts = Counter(task_labels)
        majority_count = max(label_counts.values())
        
        new_samples = []
        for label, count in label_counts.items():
            if count < majority_count:
                num_copies = int((majority_count / count - 1) * oversample_ratio)
                minority_samples = [item for item in augmented_data if item[task_key] == label]
                new_samples.extend(random.choices(minority_samples, k=len(minority_samples) * num_copies))
        augmented_data.extend(new_samples)
    return augmented_data

def back_translate(text, translator_fr_en, translator_en_fr):
    """Performs back-translation: French -> English -> French."""
    try:
        translated_en = translator_fr_en(text, max_length=len(text) + 20)[0]['translation_text']
        translated_fr = translator_en_fr(translated_en, max_length=len(translated_en) + 20)[0]['translation_text']
        return translated_fr
    except Exception as e:
        print(f"Translation failed for text: {text[:30]}... Error: {e}")
        return None

def add_keywords(data_item, keyword_dict):
    """Adds keywords to a data item based on its labels."""
    texte = data_item['texte']
    augmented_text = texte
    
    if data_item['intention'] in keyword_dict['overall_intent']:
        keywords = ' '.join(keyword_dict['overall_intent'][data_item['intention']])
        augmented_text += f" [INTENT_KEYWORDS] {keywords}"
    if data_item['objet_medical'] in keyword_dict['medical_object']:
        keywords = ' '.join(keyword_dict['medical_object'][data_item['objet_medical']])
        augmented_text += f" [MEDICAL_KEYWORDS] {keywords}"
    if data_item['sentiment'] in keyword_dict['emotion']:
        keywords = ' '.join(keyword_dict['emotion'][data_item['sentiment']])
        augmented_text += f" [SENTIMENT_KEYWORDS] {keywords}"
        
    new_item = data_item.copy()
    new_item['texte'] = augmented_text
    return new_item

def main():
    original_data_path = 'data/dataset/train_dataset.jsonl'
    
    # Define output file paths
    oversample_output_path = 'data/dataset/train_dataset_sampler.jsonl'
    backtrans_output_path = 'data/dataset/train_dataset_backtrans.jsonl'
    keywords_output_path = 'data/dataset/train_dataset_keywords.jsonl'
    combined_output_path = 'data/dataset/train_dataset_combined.jsonl'
    
    original_data = load_data(original_data_path)
    if not original_data:
        return

    # --- 1. Generate Oversampling Dataset ---
    print("\n--- Generating oversampled dataset ---")
    oversampled_data = oversample_minority_classes(original_data, ['intention', 'objet_medical', 'sentiment'])
    save_data(oversampled_data, oversample_output_path)
    
    # --- 2. Generate Back-translation Dataset ---
    print("\n--- Generating back-translated dataset ---")
    translator_fr_en = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    translator_en_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    backtrans_data = []
    for item in random.sample(original_data, int(len(original_data) * 0.5)):
        translated_text = back_translate(item['texte'], translator_fr_en, translator_en_fr)
        if translated_text:
            new_item = item.copy()
            new_item['texte'] = translated_text
            backtrans_data.append(new_item)
    final_backtrans_data = original_data + backtrans_data
    save_data(final_backtrans_data, backtrans_output_path)

    # --- 3. Generate Keyword-Augmented Dataset ---
    print("\n--- Generating keyword-augmented dataset ---")
    keywords_data = [add_keywords(item, keyword_dict) for item in original_data]
    final_keywords_data = original_data + keywords_data
    save_data(final_keywords_data, keywords_output_path)

    # --- 4. Generate Combined Dataset ---
    print("\n--- Generating combined dataset ---")
    # Combine data from all methods.
    combined_data = oversample_minority_classes(original_data, ['intention', 'objet_medical', 'sentiment'])
    combined_backtrans = []
    for item in random.sample(combined_data, int(len(combined_data) * 0.3)):
        translated_text = back_translate(item['texte'], translator_fr_en, translator_en_fr)
        if translated_text:
            new_item = item.copy()
            new_item['texte'] = translated_text
            combined_backtrans.append(new_item)
    combined_keywords = [add_keywords(item, keyword_dict) for item in combined_data]
    
    final_combined_data = combined_data + combined_backtrans + combined_keywords
    unique_final_data = {json.dumps(d, sort_keys=True): d for d in final_combined_data}.values()
    save_data(list(unique_final_data), combined_output_path)
    
    print("\nAll augmented datasets have been prepared successfully.")

if __name__ == '__main__':
    main()