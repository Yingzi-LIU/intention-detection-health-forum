import json
import os
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# This classifier dictionary is suitable for models that work with both dense (embeddings)
# and sparse (BoW, TF-IDF) feature representations.
CLASSIFIERS = {
    'LogisticRegression': (LogisticRegression(), {'C': [0.1, 1, 10], 'solver': ['liblinear']}),
    'SVM': (SVC(), {'C': [0.1, 1, 10], 'kernel': ['linear']}),
    'DecisionTree': (DecisionTreeClassifier(), {'max_depth': [None, 5, 10]}),
    'KNN': (KNeighborsClassifier(), {'n_neighbors': [3, 5, 7]})
}

# This separate classifier is for models that require count-based, non-negative features.
# It should only be used with traditional vectorizers like CountVectorizer or TfidfVectorizer.
TRADITIONAL_CLASSIFIERS = {
    'MultinomialNB': (MultinomialNB(), {'alpha': [0.1, 0.5, 1.0]})
}


def save_experiment_results(results, label_names, output_dir, mode='w'):
    """
    Saves the experiment results to a file.
    Args:
        results (dict): Dictionary containing the experiment results.
        label_names (list): List of class labels.
        output_dir (str): Directory where the results will be saved.
        mode (str): File open mode ('w' for write, 'a' for append).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    results_path = os.path.join(output_dir, "results.json")

    # If in append mode, load existing data first
    if mode == 'a' and os.path.exists(results_path):
        with open(results_path, 'r') as f:
            try:
                existing_results = json.load(f)
            except json.JSONDecodeError:
                existing_results = {}
    else:
        existing_results = {}

    # Merge new results with existing ones
    existing_results.update(results)

    with open(results_path, 'w') as f:
        json.dump(existing_results, f, indent=4)

    # Save a human-readable summary
    summary_path = os.path.join(output_dir, "summary.md")
    
    if mode == 'w' or not os.path.exists(summary_path):
        with open(summary_path, 'w') as f:
            f.write("# Experiment Results Summary\n\n")
            f.write(f"**Labels:** {', '.join(label_names)}\n\n")

    with open(summary_path, 'a') as f:
        for model_name, res in results.items():
            f.write(f"## {model_name}\n\n")
            f.write(f"- **Weighted F1 Score:** {res['f1_weighted']:.4f}\n")
            f.write(f"- **Accuracy:** {res['accuracy']:.4f}\n")
            f.write(f"- **Best Parameters:** {res['best_params']}\n")
            f.write("```json\n")
            f.write(json.dumps(res['classification_report'], indent=4))
            f.write("\n```\n\n")