import warnings
import sys
import numpy as np
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

from preprocessing import load_data, preprocess_dataset, encode_labels, add_keyword_features, save_cleaned_data
from vectorizers import Word2VecVectorizer, FastTextVectorizer, BertVectorizer
from models import save_experiment_results, CLASSIFIERS

warnings.filterwarnings("ignore")

# This is a custom transformer used to extract specified columns from a DataFrame.
# This allows processing DataFrames within ColumnTransformer, rather than just Series.
class ColumnExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.columns]

def run_experiment(X_train, y_train, X_val, y_val, label_names, vectorizers, vectorization_method=None):
    results = {}
    print("🔬 Starting experiments...")
    methods_to_run = vectorizers.keys() if not vectorization_method else ([vectorization_method] if vectorization_method in vectorizers else vectorizers.keys())

    for method_type in methods_to_run:
        for fe_name, fe_model in vectorizers[method_type].items():
            print(f"\n  -> Vectorization with {fe_name}...")
            # Traditional and Embedding vectorizers have different input requirements
            if method_type == 'traditional':
                X_train_vec = fe_model.fit_transform(X_train)
                X_val_vec = fe_model.transform(X_val)
            elif method_type == 'embedding':
                X_train_vec = fe_model.fit_transform(pd.Series(X_train))
                X_val_vec = fe_model.transform(pd.Series(X_val))
            elif method_type == 'bert':
                X_train_vec = fe_model.transform(X_train)
                X_val_vec = fe_model.transform(X_val)

            for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
                model_name = f"{fe_name}_{clf_name}"
                # Handle models that cannot handle negative inputs (MultinomialNB)
                if isinstance(clf_model, MultinomialNB) and (method_type in ['embedding', 'bert'] or np.any(X_train_vec.data < 0)):
                    continue
                
                grid_search = GridSearchCV(clf_model, param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
                try:
                    grid_search.fit(X_train_vec, y_train)
                    y_pred = grid_search.predict(X_val_vec)
                    report = classification_report(y_val, y_pred, labels=np.unique(y_pred), target_names=label_names, output_dict=True)
                    cm = confusion_matrix(y_val, y_pred)
                    results[model_name] = {
                        'f1_weighted': f1_score(y_val, y_pred, average='weighted'),
                        'accuracy': accuracy_score(y_val, y_pred),
                        'classification_report': report,
                        'confusion_matrix': cm.tolist(),
                        'best_params': grid_search.best_params_
                    }
                except Exception as e:
                    print(f"Error: {e}")
    return results

def run_enhanced_traditional_experiments(X_train, y_train, X_val, y_val, label_names, vectorizers):
    results = {}
    print("\n🔬 Starting experiments with traditional features and keywords...")
    keyword_cols = [col for col in X_train.columns if col.startswith('keyword_')]

    for fe_name, fe_model in vectorizers['traditional'].items():
        preprocessor = ColumnTransformer(
            transformers=[
                ('text_vectorizer', fe_model, 'Sentences_clean'),
                ('keywords', 'passthrough', keyword_cols)
            ]
        )
        for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
            model_name = f"{fe_name}_{clf_name}_Enhanced"
            pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('classifier', clf_model)
            ])
            full_param_grid = {f'classifier__{key}': value for key, value in param_grid.items()}
            grid_search = GridSearchCV(pipeline, full_param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
            grid_search.fit(X_train, y_train)
            y_pred = grid_search.predict(X_val)
            report = classification_report(y_val, y_pred, labels=np.unique(y_pred), target_names=label_names, output_dict=True)
            cm = confusion_matrix(y_val, y_pred)
            results[model_name] = {
                'f1_weighted': f1_score(y_val, y_pred, average='weighted'),
                'accuracy': accuracy_score(y_val, y_pred),
                'classification_report': report,
                'confusion_matrix': cm.tolist(),
                'best_params': grid_search.best_params_
            }
    return results

# New enhanced embedding experiment function, fixing data leakage issues
def run_enhanced_embedding_experiments(X_train_df, y_train, X_val_df, y_val, label_names, vectorizers):
    results = {}
    print("\n🔬 Starting experiments with word embeddings and keywords...")
    
    keyword_cols = [col for col in X_train_df.columns if col.startswith('keyword_')]

    # Define a preprocessor to handle both types of features
    preprocessor = ColumnTransformer(
        transformers=[
            # Process text column to generate word embedding vectors
            ('embedding_vectorizer', 'passthrough', 'Sentences_clean'),
            # Process keyword columns to ensure they are handled correctly
            ('keywords', 'passthrough', keyword_cols)
        ]
    )

    for fe_name, fe_model in vectorizers['embedding'].items():
        print(f"\n  -> Vectorization with {fe_name}...")
        
        # Use a custom ColumnExtractor to adapt to the fit_transform method
        X_train_text = X_train_df['Sentences_clean']
        X_val_text = X_val_df['Sentences_clean']
        
        # Generate embedding vectors
        X_train_emb = fe_model.fit_transform(pd.Series(X_train_text))
        X_val_emb = fe_model.transform(pd.Series(X_val_text))

        # Extract keyword features
        X_train_kw = X_train_df[keyword_cols].values
        X_val_kw = X_val_df[keyword_cols].values
        
        # Concatenate both types of features
        X_train_combined = np.hstack((X_train_emb, X_train_kw))
        X_val_combined = np.hstack((X_val_emb, X_val_kw))

        for clf_name, (clf_model, param_grid) in CLASSIFIERS.items():
            model_name = f"{fe_name}_{clf_name}_Enhanced"
            if clf_name == 'MultinomialNB':
                continue
            grid_search = GridSearchCV(clf_model, param_grid, cv=3, scoring='f1_weighted', n_jobs=-1, verbose=0)
            grid_search.fit(X_train_combined, y_train)
            y_pred = grid_search.predict(X_val_combined)
            report = classification_report(y_val, y_pred, labels=np.unique(y_pred), target_names=label_names, output_dict=True)
            cm = confusion_matrix(y_val, y_pred)
            results[model_name] = {
                'f1_weighted': f1_score(y_val, y_pred, average='weighted'),
                'accuracy': accuracy_score(y_val, y_pred),
                'classification_report': report,
                'confusion_matrix': cm.tolist(),
                'best_params': grid_search.best_params_
            }
    return results

def sort_results_by_f1(results):
    return dict(sorted(results.items(), key=lambda item: item[1]['f1_weighted'], reverse=True))

def main(vectorization_method=None):
    BASE_PATH = 'data/dataset/'
    keyword_dict = {'overall_intent': { 'recherche d\'information': ['question', 'savoir', 'quelqu’un', 'aider', 'renseignement', 'explication', 'avis', 'conseil', 'expérience (chez les autres)', 'information', 'réponse', 'témoignage', 'qui a déjà', 'est-ce que', 'comment'], 'partage d\'expérience': ['moi', 'j’ai', 'vécu', 'mon cas', 'personnellement', 'ça m’est arrivé', 'depuis', 'après', 'je souffre', 'quand j’ai', 'pour ma part', 'autrefois', 'chez moi', 'je raconte', 'expérience'], 'fonction phatique': ['bonjour', 'salut', 'merci', 'courage', 'bisous', 'bonne journée', 'à bientôt', 'tiens', 'coucou', 'au revoir', 'bonne chance', 'prends soin', 'je pense à toi', 'bravo', 'félicitations'] }, 'medical_object': { 'symptome': ['douleur', 'fièvre', 'toux', 'fatigue', 'nausée', 'vomissement', 'mal de tête', 'vertige', 'saignement', 'diarrhée', 'essoufflement', 'crampe', 'frisson', 'démangeaison', 'inflammation'], 'traitement': ['médicament', 'antibiotique', 'comprimé', 'injection', 'ordonnance', 'opération', 'chirurgie', 'perfusion', 'thérapie', 'séance', 'pommade', 'crème', 'gélule', 'traitement', 'protocole'], 'diagnostique': ['médecin', 'rendez-vous', 'examen', 'analyse', 'prise de sang', 'radio', 'IRM', 'scanner', 'consultation', 'diagnostic', 'spécialiste', 'test', 'résultat', 'donnée', 'explication', 'bilan', 'contrôle'], 'NA_CATEGORY': ['bonjour', 'salut', 'merci', 'courage', 'bisous', 'bonne journée', 'à bientôt', 'tiens', 'coucou', 'au revoir', 'bonne chance', 'prends soin', 'je pense à toi', 'bravo', 'félicitations'] }, 'emotion': { 'positif': ['amélioration', 'guérison', 'efficace', 'solution', 'soulagement', 'espoir', 'bon', 'normal', 'rassuré', 'progrès', 'confiance', 'réussite', 'stable', 'bien', 'positif', 'joie', 'bravo', 'félicitations', 'merci'], 'negatif': ['douleur', 'pire', 'rechute', 'inefficace', 'aggravation', 'souffrance', 'inquiétant', 'mauvais', 'problème', 'compliqué', 'peur', 'triste', 'inquiétude', 'négatif', 'désespoir', 'angoisse', 'stress', 'honte', 'colère', 'déception', 'culpabilité'], 'non': ['neutre', 'bonsoir', 'bonjour', 'merci', 'cordialement', 'accord', 'rapport', 'statistique', 'description', 'message', 'donnée', 'explication', 'résultat', 'réponse', 'conseils']}}
    label_col_map = {'overall_intent': 'niveau1', 'medical_object': 'niveau2', 'emotion': 'niveau3'}

    train_df, val_df, test_df = load_data(BASE_PATH)
    if train_df is None: return
    
    train_df = preprocess_dataset(train_df, remove_stopwords=True)
    val_df = preprocess_dataset(val_df, remove_stopwords=True)
    test_df = preprocess_dataset(test_df, remove_stopwords=True)
    save_cleaned_data(train_df, val_df, test_df, 'data/dataset_clean/')

    for label_name, label_col in label_col_map.items():
        temp_train_df, temp_val_df, temp_test_df, label_encoders = encode_labels(
            train_df.copy(), val_df.copy(), test_df.copy(), {label_name: label_col}
        )
        unique_labels = np.unique(np.concatenate([temp_train_df[label_col], temp_val_df[label_col]]))
        label_names_list = label_encoders[label_name].inverse_transform(unique_labels)
        X_train = temp_train_df['Sentences_clean'].astype(str)
        y_train = temp_train_df[label_col]
        X_val = temp_val_df['Sentences_clean'].astype(str)
        y_val = temp_val_df[label_col]

        vectorizers_all = {
            'traditional': {'BoW': CountVectorizer(), 'TF-IDF': TfidfVectorizer(), 'TF-IDF_ngram': TfidfVectorizer(ngram_range=(1, 2))},
            'embedding': {'Word2Vec': Word2VecVectorizer(), 'FastText': FastTextVectorizer()},
            'bert': {'Bert': BertVectorizer()}
        }

        if vectorization_method in ['traditional', 'embedding', 'bert', None]:
            results = run_experiment(X_train, y_train, X_val, y_val, label_names_list, vectorizers_all, vectorization_method)
            if results:
                sorted_results = sort_results_by_f1(results)
                save_experiment_results(sorted_results, label_names_list, f'results_baseline/{label_name}/')

    train_df_enhanced = add_keyword_features(train_df.copy(), keyword_dict)
    val_df_enhanced = add_keyword_features(val_df.copy(), keyword_dict)
    test_df_enhanced = add_keyword_features(test_df.copy(), keyword_dict)

    for label_name, label_col in label_col_map.items():
        temp_train_df, temp_val_df, _, label_encoders = encode_labels(
            train_df_enhanced.copy(), val_df_enhanced.copy(), test_df_enhanced.copy(), {label_name: label_col}
        )
        unique_labels = np.unique(np.concatenate([temp_train_df[label_col], temp_val_df[label_col]]))
        label_names_list = label_encoders[label_name].inverse_transform(unique_labels)

        # Enhanced experiments for traditional models
        if vectorization_method in ['traditional', None]:
            X_train_trad = temp_train_df[['Sentences_clean'] + [c for c in temp_train_df.columns if c.startswith('keyword_')]]
            X_val_trad = temp_val_df[['Sentences_clean'] + [c for c in temp_val_df.columns if c.startswith('keyword_')]]
            y_train = temp_train_df[label_col]
            y_val = temp_val_df[label_col]
            vectorizers_trad = {'traditional': {'BoW': CountVectorizer(), 'TF-IDF': TfidfVectorizer(), 'TF-IDF_ngram': TfidfVectorizer(ngram_range=(1, 2))}}
            results_trad = run_enhanced_traditional_experiments(X_train_trad, y_train, X_val_trad, y_val, label_names_list, vectorizers_trad)
            if results_trad:
                sorted_results_trad = sort_results_by_f1(results_trad)
                save_experiment_results(sorted_results_trad, label_names_list, f'results_enhanced/{label_name}/')

        # Enhanced experiments for embedding models (new version)
        if vectorization_method in ['embedding', None]:
            y_train = temp_train_df[label_col]
            y_val = temp_val_df[label_col]
            vectorizers_emb = {'embedding': {'Word2Vec': Word2VecVectorizer(), 'FastText': FastTextVectorizer()}}
            results_emb = run_enhanced_embedding_experiments(temp_train_df, y_train, temp_val_df, y_val, label_names_list, vectorizers_emb)
            if results_emb:
                sorted_results_emb = sort_results_by_f1(results_emb)
                save_experiment_results(sorted_results_emb, label_names_list, f'results_enhanced/{label_name}/', mode='a')

    print("\n\n✅ Experiments completed.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run experiments with different vectorization methods.")
    parser.add_argument('--vectorization_method', type=str, default=None,
                        choices=['traditional', 'embedding', 'bert'])
    args = parser.parse_args()
    main(vectorization_method=args.vectorization_method)