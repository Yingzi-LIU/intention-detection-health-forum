import json
import matplotlib.pyplot as plt
import numpy as np
import os

def analyze_post_length(file_path):
    """
    Analyse la longueur (nombre de phrases) de chaque postes dans le fichier JSON.

    Args:
        file_path (str): Le chemin d'accès au fichier JSON contenant les postes reconstruites.
        
    Returns:
        list: Une liste du nombre de phrases pour chaque postes.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable. Veuillez vous assurer que le chemin d'accès au fichier est correct.")
        return []

    post_lengths = []
    for post in data:
        if 'sentences' in post and post['sentences']:
            post_lengths.append(len(post['sentences']))
    
    return post_lengths

def visualize_post_lengths(lengths):
    """
    Génère un histogramme pour visualiser la distribution des longueurs des postes.

    Args:
        lengths (list): Une liste des longueurs des postes.
    """
    if not lengths:
        print("Aucune donnée à visualiser.")
        return

    # Calculer les statistiques
    min_len = np.min(lengths)
    max_len = np.max(lengths)
    mean_len = np.mean(lengths)

    print(f"\n--- Résumé de la longueur des postes ---")
    print(f"Nombre total de postes analysées : {len(lengths)}")
    print(f"Nombre minimal de phrases par postes : {min_len}")
    print(f"Nombre maximal de phrases par postes : {max_len}")
    print(f"Nombre moyen de phrases par postes : {mean_len:.2f}")
    
    # Créer l'histogramme
    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=range(min_len, max_len + 2), edgecolor='black', alpha=0.7)
    
    plt.title('Distribution de la longueur des postes (par phrase)', fontsize=14)
    plt.xlabel('Nombre de phrases par postes', fontsize=12)
    plt.ylabel('Nombre de postes', fontsize=12)
    plt.xticks(range(min_len, max_len + 2))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    # Définir le répertoire de sortie et le créer s'il n'existe pas
    output_dir = 'intention_flow_schema'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'post_length_distribution.png')
    
    plt.savefig(file_path)
    plt.show()
    print(f"✅ Le graphique de distribution de la longueur des postes est enregistré sous '{file_path}'")


if __name__ == '__main__':
    FILE_PATH = 'data/reconstructed_posts_final.json'
    
    post_lengths = analyze_post_length(FILE_PATH)
    
    if post_lengths:
        visualize_post_lengths(post_lengths)
    else:
        print("Impossible d'analyser la longueur des postes. Veuillez vérifier votre fichier JSON.")
