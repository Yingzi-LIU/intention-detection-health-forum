import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV
file_path = 'data/projet_annotation_sante_final_M1.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Le fichier '{file_path}' a été chargé avec succès. Dimensions : {df.shape}")
except FileNotFoundError:
    print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé. Veuillez vous assurer que le fichier est bien présent dans votre environnement Colab.")
    exit()

# Vérifier et gérer les valeurs NaN potentielles
nan_cols = df.isnull().sum()
nan_cols = nan_cols[nan_cols > 0]
if not nan_cols.empty:
    print("\nColonnes avec des valeurs NaN avant traitement :")
    print(nan_cols)
    df = df.fillna('NA_CATEGORY')
    print("Les valeurs NaN ont été remplacées par 'NA_CATEGORY'.")
else:
    print("\nAucune valeur NaN n'a été trouvée dans le jeu de données.")


label_col1 = 'niveau1' 
label_col2 = 'niveau2'       
label_col3 = 'niveau3' 


for col in [label_col1, label_col2, label_col3]:
    if col not in df.columns:
        print(f"Erreur : La colonne de libellé '{col}' est introuvable dans le DataFrame. Veuillez vérifier les noms des colonnes de votre fichier CSV.")
        exit()

# Définir les titres pour chaque graphique
plot_titles = {
    label_col1: 'Niveau de l\'intention générale',
    label_col2: 'Niveau de l\'objet médical',
    label_col3: 'Niveau d\'analyse de sentiment'
}

# Analyser la distribution des libellés dans le jeu de données original
print("\n--- Analyse de la distribution des libellés du jeu de données original ---")
label_cols_to_plot = [label_col1, label_col2, label_col3]

for col in label_cols_to_plot:
    plt.figure(figsize=(12, 6))
    
    # Compter la fréquence de chaque libellé
    label_counts = df[col].astype(str).value_counts().sort_values(ascending=True)
    
    # Créer le graphique à barres horizontal
    ax = sns.barplot(y=label_counts.index, x=label_counts.values, palette='viridis')
    
    # Ajouter les titres, les étiquettes des axes et les chiffres sur les barres
    plt.title(plot_titles.get(col, f'Distribution des catégories : {col}'), fontsize=16)
    plt.xlabel('Nombres', fontsize=12)
    plt.ylabel('Catégories', fontsize=12)
    
    # Ajouter les valeurs numériques sur les barres
    for index, value in enumerate(label_counts.values):
        plt.text(value + 1, index, str(value), va='center')

    plt.tight_layout()
    plt.savefig(f'schema/distribution_{col}.png')
    plt.close()

print("L'analyse de la distribution des libellés est terminée. La suite du code de division des données peut être exécutée.")


