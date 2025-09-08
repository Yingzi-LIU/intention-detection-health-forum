import json
import os
from tabulate import tabulate # Utilise la bibliothèque tabulate

def load_data(file_path):
    """
    Charge les données de publications reconstruites à partir d'un fichier JSON.
    
    Args:
        file_path (str): Le chemin d'accès au fichier JSON.
        
    Returns:
        list: Une liste de dictionnaires de publications.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        return []

def find_posts_by_pattern(posts_data, pattern):
    """
    Recherche les publications qui contiennent un modèle de transition d'intention spécifique.

    Args:
        posts_data (list): Une liste de dictionnaires de publications.
        pattern (list): Une liste de chaînes de caractères d'intention représentant la séquence.

    Returns:
        list: Une liste de dictionnaires, chacun contenant l'ID d'une publication correspondante et ses phrases.
    """
    matching_posts = []
    pattern_len = len(pattern)
    
    for post in posts_data:
        sentences = post.get('sentences', [])
        if len(sentences) >= pattern_len:
            # Créer une liste de chaînes d'intention combinées pour la publication
            post_intents = [
                f"{s.get('niveau1', 'NA')}_{s.get('niveau2', 'NA')}_{s.get('niveau3', 'NA')}"
                for s in sentences
            ]

            # Vérifier la présence du modèle en tant que sous-séquence contiguë
            for i in range(len(post_intents) - pattern_len + 1):
                if post_intents[i:i+pattern_len] == pattern:
                    match_info = {
                        "post_id": post.get("post_id"),
                        "sentences": sentences[i:i+pattern_len]
                    }
                    matching_posts.append(match_info)
                    break # Passer à la publication suivante après avoir trouvé la première correspondance
                    
    return matching_posts

def main():
    FILE_PATH = 'data/reconstructed_posts_final.json'
    posts_data = load_data(FILE_PATH)
    if not posts_data:
        return

    # Définir les modèles de flux d'intention qui vous intéressent
    patterns_to_search = [
        ['partage_experience_traitement_non', 'partage_experience_symptome_non'],
        ['partage_experience_symptome_non', 'partage_experience_symptome_negatif']
    ]

    for pattern in patterns_to_search:
        print(f"======================================================")
        print(f"Recherche du modèle : {' -> '.join(pattern)}")
        print(f"======================================================")
        
        found_posts = find_posts_by_pattern(posts_data, pattern)
        
        if found_posts:
            for post in found_posts:
                print(f"✅ Correspondance trouvée dans la publication ID : {post['post_id']}")
                table_data = [[s['niveau1'], s['text']] for s in post['sentences']]
                headers = ["Intention", "Texte de la phrase"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
                print("\n")
        else:
            print("Aucune publication ne correspond à ce modèle.")
        print("\n")

if __name__ == '__main__':
    main()
