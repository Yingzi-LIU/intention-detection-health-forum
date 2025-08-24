import warnings
import sys
warnings.filterwarnings("ignore")
import numpy as np
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from preprocessing import load_data, preprocess_dataset, encode_labels, add_keyword_features, save_cleaned_data
from vectorizers import Word2VecVectorizer, FastTextVectorizer, BertVectorizer
from models import save_experiment_results, CLASSIFIERS

def run_experiment(X_train, y_train, X_val, y_val, label_names, vectorizers, vectorization_method=None):
    """
    Runs baseline experiments without keyword-based features.
    Allows selection of a specific vectorization method.
    """
    results = {}
    print("🔬 Démarrage des expériences...")

    methods_to_run = []
    if vectorization_method:
        if vectorization_method in vectorizers:
            methods_to_run.append(vectorization_method)
        else:
            print(f"⚠️ Méthode de vectorisation '{vectorization_method}' non reconnue. Exécution de toutes les méthodes disponibles.")
            methods_to_run = vectorizers.keys()
    else:
        methods_to_run = vectorizers.keys()

    for method_type in methods_to_run:
        if method_type == 'traditional':
            # 1. Traditional features (BoW, TF-IDF)
            for fe_name, fe_model in vectorizers['traditional'].items():
                print(f"\n  -> Vectorisation avec {fe_name}...")
                X_train_vec = fe_model.fit_transform(X_train)
                X_val_vec = fe_model.transform(X_val)
                
                for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
                    model_name = f"{fe_name}_{clf_name}"
                    print(f"    -> Test de {model_name}...")
                    
                    # Check for compatibility with MultinomialNB
                    if isinstance(clf_model, MultinomialNB) and np.any(X_train_vec.data < 0):
                        print(f"       ⚠️ Skipping {model_name} as its input contains negative values, which is incompatible with MultinomialNB.")
                        continue
                    
                    grid_search = GridSearchCV(clf_model, param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
                    try:
                        grid_search.fit(X_train_vec, y_train)
                        y_pred = grid_search.predict(X_val_vec)
                        report = classification_report(y_val, y_pred, labels=np.unique(y_pred), target_names=label_names, output_dict=True)
                        cm = confusion_matrix(y_val, y_pred)
                        f1_weighted = f1_score(y_val, y_pred, average='weighted')
                        accuracy = accuracy_score(y_val, y_pred)
                        
                        results[model_name] = {
                            'f1_weighted': f1_weighted, 'accuracy': accuracy,
                            'classification_report': report, 'confusion_matrix': cm.tolist(),
                            'best_params': grid_search.best_params_
                        }
                        print(f"       ✅ Terminé. F1 (Pondéré) : {f1_weighted:.4f}, Précision : {accuracy:.4f}")
                    except Exception as e:
                        print(f"       ❌ Erreur lors de l'entraînement/évaluation : {e}")
        
        elif method_type == 'embedding':
            # 2. Word embeddings
            for fe_name, fe_model in vectorizers['embedding'].items():
                print(f"\n  -> Vectorisation avec {fe_name}...")
                try:
                    X_train_vec = fe_model.fit_transform(X_train)
                    X_val_vec = fe_model.transform(X_val)
                    
                    for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
                        model_name = f"{fe_name}_{clf_name}"
                        print(f"    -> Test de {model_name}...")
                        
                        if clf_name == 'MultinomialNB':
                            print(f"       ⚠️ Skipping {model_name} as its input contains negative values.")
                            continue
                        
                        grid_search = GridSearchCV(clf_model, param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
                        grid_search.fit(X_train_vec, y_train)
                        y_pred = grid_search.predict(X_val_vec)
                        report = classification_report(y_val, y_pred, labels=np.unique(y_pred), target_names=label_names, output_dict=True)
                        cm = confusion_matrix(y_val, y_pred)
                        f1_weighted = f1_score(y_val, y_pred, average='weighted')
                        accuracy = accuracy_score(y_val, y_pred)
                        
                        results[model_name] = {
                            'f1_weighted': f1_weighted, 'accuracy': accuracy,
                            'classification_report': report, 'confusion_matrix': cm.tolist(),
                            'best_params': grid_search.best_params_
                        }
                        print(f"       ✅ Terminé. F1 (Pondéré) : {f1_weighted:.4f}, Précision : {accuracy:.4f}")
                except Exception as e:
                    print(f"       ❌ Erreur lors de l'entraînement/évaluation pour {fe_name} : {e}")

        elif method_type == 'bert':
            # 3. BERT embeddings
            if 'bert' in vectorizers:
                for fe_name, fe_model in vectorizers['bert'].items():
                    print(f"\n  -> Vectorisation avec {fe_name}...")
                    try:
                        X_train_vec = fe_model.transform(X_train)
                        X_val_vec = fe_model.transform(X_val)
                        
                        for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
                            model_name = f"{fe_name}_{clf_name}"
                            print(f"    -> Test de {model_name}...")
                            
                            if clf_name == 'MultinomialNB':
                                print(f"       ⚠️ Skipping {model_name} as its input contains negative values.")
                                continue
                                
                            grid_search = GridSearchCV(clf_model, param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
                            grid_search.fit(X_train_vec, y_train)
                            y_pred = grid_search.predict(X_val_vec)
                            report = classification_report(y_val, y_pred, labels=np.unique(y_pred), target_names=label_names, output_dict=True)
                            cm = confusion_matrix(y_val, y_pred)
                            f1_weighted = f1_score(y_val, y_pred, average='weighted')
                            accuracy = accuracy_score(y_val, y_pred)
                            
                            results[model_name] = {
                                'f1_weighted': f1_weighted, 'accuracy': accuracy,
                                'classification_report': report, 'confusion_matrix': cm.tolist(),
                                'best_params': grid_search.best_params_
                            }
                            print(f"       ✅ Terminé. F1 (Pondéré) : {f1_weighted:.4f}, Précision : {accuracy:.4f}")
                    except Exception as e:
                        print(f"       ❌ Erreur lors de l'entraînement/évaluation pour {fe_name} : {e}")
                        
    return results


def run_enhanced_traditional_experiments(X_train, y_train, X_val, y_val, label_names, vectorizers):
    """
    Runs enhanced experiments with traditional features (BoW, TF-IDF) and keywords.
    """
    results = {}
    print("\n🔬 Démarrage des expériences avec des caractéristiques traditionnelles et des mots-clés...")
    
    for fe_name, fe_model in vectorizers['traditional'].items():
        preprocessor = ColumnTransformer(
            transformers=[
                ('text_vectorizer', fe_model, 'Sentences_clean'),
            ],
            remainder='passthrough'
        )
        
        # Note: We don't use X_train_transformed directly for fitting the GridSearchCV pipeline
        # since it's already part of the pipeline.
        
        for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
            model_name = f"{fe_name}_{clf_name}_Enhanced"
            print(f"  -> Test de {model_name}...")
            
            if isinstance(clf_model, MultinomialNB):
                # The preprocessor output for BoW/TF-IDF might contain sparse matrices.
                # We need a way to check for negative values if it's not a sparse matrix.
                # Let's skip MultinomialNB with this pipeline for now, as it's complex to handle mixed data types.
                # This check can be refined if needed.
                print(f"     ⚠️ Skipping {model_name} due to potential negative feature values which are incompatible with MultinomialNB.")
                continue

            pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('classifier', clf_model)
            ])
            full_param_grid = {f'classifier__{key}': value for key, value in param_grid.items()}
            
            grid_search = GridSearchCV(pipeline, full_param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
            try:
                grid_search.fit(X_train, y_train)
                y_pred = grid_search.predict(X_val)
                f1_weighted = f1_score(y_val, y_pred, average='weighted')
                f1_macro = f1_score(y_val, y_pred, average='macro')
                f1_micro = f1_score(y_val, y_pred, average='micro')
                accuracy = accuracy_score(y_val, y_pred)
                report = classification_report(y_val, y_pred, target_names=label_names, output_dict=True)
                cm = confusion_matrix(y_val, y_pred)
                
                results[model_name] = {
                    'f1_weighted': f1_weighted, 'f1_macro': f1_macro, 'f1_micro': f1_micro,
                    'accuracy': accuracy, 'classification_report': report,
                    'confusion_matrix': cm.tolist(), # Convert ndarray to list here
                    'best_params': grid_search.best_params_
                }
                print(f"     ✅ Terminé. F1 (Pondéré) : {f1_weighted:.4f}, Précision : {accuracy:.4f}")
            except Exception as e:
                print(f"     ❌ Erreur lors de l'entraînement/évaluation : {e}")
    return results

def sort_results_by_f1(results):
    """
    Sorts the results dictionary by f1_weighted score in descending order.
    """
    return dict(sorted(results.items(), key=lambda item: item[1]['f1_weighted'], reverse=True))

def run_enhanced_embedding_experiments(X_train, y_train, X_val, y_val, label_name, label_names, label_encoders, vectorizers, keyword_dict):
    """
    Runs enhanced experiments with static word embeddings and keywords.
    """
    results = {}
    print("\n🔬 Démarrage des expériences avec des word embeddings statiques...")

    all_keywords = []
    if label_name in keyword_dict:
        for _, keywords in keyword_dict[label_name].items():
            all_keywords.extend(keywords)
    
    pseudo_sentence = ' '.join(all_keywords)

    for fe_name, fe_model in vectorizers['embedding'].items():
        try:
            X_train_enhanced = X_train.tolist() + [pseudo_sentence]
            y_train_enhanced = np.append(y_train, -1)
            
            X_train_vec = fe_model.fit_transform(pd.Series(X_train_enhanced))
            X_val_vec = fe_model.transform(pd.Series(X_val))
            
            for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
                model_name = f"{fe_name}_{clf_name}_Enhanced"
                print(f"  -> Test de {model_name}...")
                
                if clf_name == 'MultinomialNB':
                    print(f"     ⚠️ Skipping {model_name} as MultinomialNB cannot handle negative values.")
                    continue
                
                grid_search = GridSearchCV(clf_model, param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
                try:
                    grid_search.fit(X_train_vec, y_train_enhanced)
                    y_pred = grid_search.predict(X_val_vec)
                    f1_weighted = f1_score(y_val, y_pred, average='weighted')
                    f1_macro = f1_score(y_val, y_pred, average='macro')
                    f1_micro = f1_score(y_val, y_pred, average='micro')
                    accuracy = accuracy_score(y_val, y_pred)
                    report = classification_report(y_val, y_pred, labels=label_encoders[label_name].transform(label_names), target_names=label_names, output_dict=True)
                    cm = confusion_matrix(y_val, y_pred)
                    
                    results[model_name] = {
                        'f1_weighted': f1_weighted, 'f1_macro': f1_macro, 'f1_micro': f1_micro,
                        'accuracy': accuracy, 'classification_report': report,
                        'confusion_matrix': cm.tolist(),  # 这行将 ndarray 转换为列表
                        'best_params': grid_search.best_params_
                    }
                    print(f"     ✅ Terminé. F1 (Pondéré) : {f1_weighted:.4f}, Précision : {accuracy:.4f}")
                except Exception as e:
                    print(f"     ❌ Erreur lors de l'entraînement/évaluation pour {fe_name} : {e}")
                    if "inconsistent numbers of samples" in str(e):
                        print(f"     💡 Astuce : 检查 {fe_name} 的 X_train 和 y_train 的长度是否匹配。")
                    continue
        except Exception as e:
            print(f"     ❌ Erreur lors de l'entraînement/évaluation pour {fe_name} : {e}")
            if "inconsistent numbers of samples" in str(e):
                print(f"     💡 Astuce : 检查 {fe_name} 的 X_train 和 y_train 的长度是否匹配。")
            continue
    return results

def main(vectorization_method=None):
    BASE_PATH = 'data/dataset/'
    keyword_dict = {
        'overall_intent': {
            'recherche d\'information': ['question', 'savoir', 'quelqu’un', 'aider', 'renseignement', 'explication', 'avis', 'conseil', 'expérience (chez les autres)', 'information', 'réponse', 'témoignage', 'qui a déjà', 'est-ce que', 'comment'],
            'partage d\'expérience': ['moi', 'j’ai', 'vécu', 'mon cas', 'personnellement', 'ça m’est arrivé', 'depuis', 'après', 'je souffre', 'quand j’ai', 'pour ma part', 'autrefois', 'chez moi', 'je raconte', 'expérience'],
            'fonction phatique': ['bonjour', 'salut', 'merci', 'courage', 'bisous', 'bonne journée', 'à bientôt', 'tiens', 'coucou', 'au revoir', 'bonne chance', 'prends soin', 'je pense à toi', 'bravo', 'félicitations']
        },
        'medical_object': {
            'symptome': ['douleur', 'fièvre', 'toux', 'fatigue', 'nausée', 'vomissement', 'mal de tête', 'vertige', 'saignement', 'diarrhée', 'essoufflement', 'crampe', 'frisson', 'démangeaison', 'inflammation'],
            'traitement': ['médicament', 'antibiotique', 'comprimé', 'injection', 'ordonnance', 'opération', 'chirurgie', 'perfusion', 'thérapie', 'séance', 'pommade', 'crème', 'gélule', 'traitement', 'protocole'],
            'diagnostique': ['médecin', 'rendez-vous', 'examen', 'analyse', 'prise de sang', 'radio', 'IRM', 'scanner', 'consultation', 'diagnostic', 'spécialiste', 'test', 'résultat', 'donnée', 'explication', 'bilan', 'contrôle']
        },
        'emotion_existence': {
            'oui': ['peur', 'angoisse', 'stress', 'inquiétude', 'espoir', 'joie', 'soulagement', 'tristesse', 'douleur', 'confiance', 'honte', 'colère', 'déception', 'gratitude', 'culpabilité'],
            'non': ['neutre', 'fait', 'simple', 'information', 'constat', 'objectif', 'rapport', 'statistique', 'description', 'résultat', 'donnée', 'explication', 'détail', 'procédure', 'observation']
        },
        'emotion_polarity': {
            'positif': ['amélioration', 'guérison', 'efficace', 'solution', 'soulagement', 'espoir', 'bon', 'normal', 'rassuré', 'progrès', 'confiance', 'réussite', 'stable', 'bien', 'positif'],
            'négatif': ['douleur', 'pire', 'rechute', 'inefficace', 'aggravation', 'souffrance', 'inquiétant', 'mauvais', 'problème', 'compliqué', 'peur', 'triste', 'inquiétude', 'négatif', 'désespoir']
        }
    }
    label_col_map = {
        'overall_intent': 'niveau1',
        'medical_object': 'niveau2',
        'emotion_existence': 'niveau3_1',
        'emotion_polarity': 'niveau3_2'
    }

    train_df, val_df, test_df = load_data(BASE_PATH)
    if train_df is None: return
    
    train_df = preprocess_dataset(train_df, remove_stopwords=True)
    val_df = preprocess_dataset(val_df, remove_stopwords=True)
    test_df = preprocess_dataset(test_df, remove_stopwords=True)
    
    # 保存清洗后的数据
    save_cleaned_data(train_df, val_df, test_df, 'data/dataset_clean/')
    
    print("\n\n=============== DÉBUT DES EXPÉRIENCES DE BASE (SANS MOTS-CLÉS) ===============")
    for label_name, label_col in label_col_map.items():
        print(f"\n--- Tâche : {label_name} ---")
        temp_train_df, temp_val_df, temp_test_df, label_encoders = encode_labels(
            train_df.copy(), val_df.copy(), test_df.copy(), {label_name: label_col}
        )
        unique_labels = np.unique(np.concatenate([temp_train_df[label_col], temp_val_df[label_col]]))
        label_names_list = label_encoders[label_name].inverse_transform(unique_labels)
        X_train = temp_train_df['Sentences_clean'].astype(str)
        y_train = temp_train_df[label_col]
        X_val = temp_val_df['Sentences_clean'].astype(str)
        y_val = temp_val_df[label_col]
        
        vectorizers = {
            'traditional': {'BoW': CountVectorizer(), 'TF-IDF': TfidfVectorizer(), 'TF-IDF_ngram': TfidfVectorizer(ngram_range=(1, 2))},
            'embedding': {'Word2Vec': Word2VecVectorizer(), 'FastText': FastTextVectorizer()},
            'bert': {'Bert': BertVectorizer()}
        }
        
        results = run_experiment(X_train, y_train, X_val, y_val, label_names_list, vectorizers, vectorization_method)
        if results:
            sorted_results = sort_results_by_f1(results)
            save_experiment_results(sorted_results, label_names_list, f'results_baseline/{label_name}/')

    print("\n\n=============== DÉBUT DES EXPÉRIENCES AMÉLIORÉES (AVEC MOTS-CLÉS) ===============")
    train_df_enhanced = add_keyword_features(train_df.copy(), keyword_dict)
    val_df_enhanced = add_keyword_features(val_df.copy(), keyword_dict)
    test_df_enhanced = add_keyword_features(test_df.copy(), keyword_dict)
    
    for label_name, label_col in label_col_map.items():
        print(f"\n--- Tâche : {label_name} ---")
        temp_train_df, temp_val_df, _, label_encoders = encode_labels(
            train_df_enhanced.copy(), val_df_enhanced.copy(), test_df_enhanced.copy(), {label_name: label_col}
        )
        unique_labels = np.unique(np.concatenate([temp_train_df[label_col], temp_val_df[label_col]]))
        label_names_list = label_encoders[label_name].inverse_transform(unique_labels)
        
        keyword_cols = [col for col in temp_train_df.columns if col.startswith('keyword_')]
        X_train_traditional = temp_train_df[['Sentences_clean'] + keyword_cols]
        y_train = temp_train_df[label_col]
        X_val_traditional = temp_val_df[['Sentences_clean'] + keyword_cols]
        y_val = temp_val_df[label_col]
        
        vectorizers_traditional = {
            'traditional': {'BoW': CountVectorizer(), 'TF-IDF': TfidfVectorizer(), 'TF-IDF_ngram': TfidfVectorizer(ngram_range=(1, 2))},
        }

        results_trad = run_enhanced_traditional_experiments(X_train_traditional, y_train, X_val_traditional, y_val, label_names_list, vectorizers_traditional)
        if results_trad:
            sorted_results_trad = sort_results_by_f1(results_trad)
            save_experiment_results(sorted_results_trad, label_names_list, f'results_enhanced/{label_name}/')

        X_train_embedding = temp_train_df['Sentences_clean']
        X_val_embedding = temp_val_df['Sentences_clean']
        
        vectorizers_embedding = {
            'embedding': {'Word2Vec': Word2VecVectorizer(), 'FastText': FastTextVectorizer()}
        }
        
        results_emb = run_enhanced_embedding_experiments(X_train_embedding, y_train, X_val_embedding, y_val, label_name, label_names_list, label_encoders, vectorizers_embedding, keyword_dict)
        if results_emb:
            sorted_results_emb = sort_results_by_f1(results_emb)
            save_experiment_results(sorted_results_emb, label_names_list, f'results_enhanced/{label_name}/', mode='a')
    
    print("\n\n✅ Les expériences sont terminées. Veuillez consulter les dossiers 'results_baseline' et 'results_enhanced' pour l'analyse.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run experiments with different vectorization methods.")
    parser.add_argument('--vectorization_method', type=str, default=None,
                        choices=['traditional', 'embedding', 'bert'],
                        help="Specify the vectorization method to use (traditional, embedding, bert). If not specified, all methods will be run.")
    args = parser.parse_args()
    main(vectorization_method=args.vectorization_method)