import json
import os
from collections import Counter
from tabulate import tabulate # Utilise la bibliothèque tabulate pour créer un tableau

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

def build_intent_transitions(posts_data):
    """
    Construit un dictionnaire des transitions d'intention et de leurs fréquences.

    Args:
        posts_data (list): Une liste de dictionnaires de publications.

    Returns:
        collections.Counter: Un objet Counter des transitions.
    """
    transitions = Counter()
    for post in posts_data:
        sentences = post.get('sentences', [])
        if len(sentences) > 1:
            for i in range(len(sentences) - 1):
                current_intent = sentences[i].get('niveau1', 'NA')
                next_intent = sentences[i+1].get('niveau1', 'NA')
                if current_intent and next_intent:
                    transitions[(current_intent, next_intent)] += 1
    return transitions

def print_and_save_transition_table(transitions, min_frequency=2, output_dir='intention_flow_schema'):
    """
    Affiche un tableau des transitions d'intention fréquentes et le sauvegarde.

    Args:
        transitions (collections.Counter): Un objet Counter des transitions.
        min_frequency (int): La fréquence minimale pour qu'une transition soit incluse dans le tableau.
        output_dir (str): Le répertoire de sortie où le fichier sera enregistré.
    """
    if not transitions:
        print("Il n'y a pas assez de transitions d'intention à afficher.")
        return

    # Trier les transitions par fréquence décroissante
    sorted_transitions = sorted(transitions.items(), key=lambda item: item[1], reverse=True)
    
    table_data = []
    for (source, target), count in sorted_transitions:
        if count >= min_frequency:
            table_data.append([source, target, count])

    if not table_data:
        print(f"Aucune transition n'a été trouvée avec une fréquence minimale de {min_frequency}.")
        return

    headers = ["Intention Source", "Intention Cible", "Fréquence"]
    
    # Formater le tableau
    formatted_table = tabulate(table_data, headers=headers, tablefmt="grid")

    # Afficher le tableau dans le terminal
    print("\n--- Tableau de transition des intentions ---")
    print(formatted_table)
    print("\n✅ Tableau des transitions d'intention généré avec succès.")
    
    # Sauvegarder le tableau dans un fichier
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'intent_flow_table.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("--- Tableau de transition des intentions ---\n")
        f.write(formatted_table)
    print(f"✅ Le tableau a été enregistré dans le fichier '{file_path}'.")


def main():
    FILE_PATH = 'data/reconstructed_posts_final.json'
    posts_data = load_data(FILE_PATH)
    if not posts_data:
        return

    transitions = build_intent_transitions(posts_data)
    # Définir la fréquence minimale, que vous pouvez ajuster au besoin
    min_freq = 2 
    print_and_save_transition_table(transitions, min_frequency=min_freq)

if __name__ == '__main__':
    main()
