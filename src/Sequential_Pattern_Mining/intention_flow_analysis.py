import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import os

def analyze_intention_flow(file_path, flow_length=2):
    """
    Analyzes the sequential flow of 'niveau1', 'niveau2', and 'niveau3'
    intentions within each post by combining them into a single pattern.

    Args:
        file_path (str): The path to the JSON file containing reconstructed posts.
        flow_length (int): The number of steps in the intention flow (e.g., 2 for a two-step flow).
        
    Returns:
        dict: A dictionary with composite intention flow patterns as keys and their frequencies as values.
    """
    if flow_length < 2:
        print("Erreur : la 'flow_length' doit être d'au moins 2.")
        return {}
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Erreur : le fichier '{file_path}' est introuvable. Veuillez vous assurer que le chemin est correct.")
        return {}

    all_sequences = []
    
    for post in data:
        # Check if 'sentences' key exists and is not empty
        if 'sentences' in post and post['sentences']:
            # Create a composite label for each sentence by combining all three levels
            sequence = [
                f"{s.get('niveau1', 'NA')}_{s.get('niveau2', 'NA')}_{s.get('niveau3', 'NA')}"
                for s in post['sentences'] if s.get('niveau1') is not None
            ]
            
            # Find all consecutive sub-sequences of the specified length
            if len(sequence) >= flow_length:
                for i in range(len(sequence) - flow_length + 1):
                    # Combine the labels into a flow pattern string
                    sub_sequence = " -> ".join(sequence[i:i + flow_length])
                    all_sequences.append(sub_sequence)
                
    # Count the frequency of each unique sequence
    sequence_counts = defaultdict(int)
    for seq in all_sequences:
        sequence_counts[seq] += 1
        
    # Sort sequences by frequency in descending order
    sorted_sequences = sorted(sequence_counts.items(), key=lambda x: x[1], reverse=True)
    
    return dict(sorted_sequences)

def filter_repetitive_patterns(patterns):
    """
    Filters out intention flow patterns where all intentions are the same.
    
    Args:
        patterns (dict): A dictionary of patterns and their frequencies.
        
    Returns:
        dict: A new dictionary with repetitive patterns removed.
    """
    filtered_patterns = {}
    for pattern, count in patterns.items():
        # Split the pattern string into individual intentions
        intentions = pattern.split(' -> ')
        # Check if there is more than one unique intention
        if len(set(intentions)) > 1:
            filtered_patterns[pattern] = count
    return filtered_patterns

def visualize_patterns(patterns, top_n=10, flow_length=2):
    """
    Generates a bar chart to visualize the most frequent composite intention flow patterns.
    
    Args:
        patterns (dict): A dictionary of patterns and their frequencies.
        top_n (int): The number of top patterns to visualize.
        flow_length (int): The number of steps in the intention flow being visualized.
    """
    if not patterns:
        print("Aucun modèle à visualiser. Veuillez vérifier les données d'entrée.")
        return
        
    # Define the output directory and create it if it doesn't exist
    output_dir = 'intention_flow_schema'
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the top N patterns
    top_patterns = dict(list(patterns.items())[:top_n])
    
    # Create the plot with a larger figure size and a better aspect ratio for long labels
    plt.figure(figsize=(20, 12))
    bars = plt.barh(list(top_patterns.keys()), list(top_patterns.values()), color='skyblue')
    
    plt.xlabel('Fréquence', fontsize=12)
    plt.ylabel("Modèle de flux d'intention", fontsize=12)
    plt.title(f'Les {top_n} modèles de flux d\'intention les plus fréquents ({flow_length} étapes)', fontsize=14)
    plt.gca().invert_yaxis()  # Display highest frequency at the top
    
    # Adjust font size of y-axis ticks to accommodate long labels
    plt.tick_params(axis='y', labelsize=10)
    
    # Add frequency labels on the bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2, f' {width}', va='center', ha='left')
        
    plt.tight_layout()
    
    # Save the figure to the new directory
    file_path = os.path.join(output_dir, f'intention_flow_patterns_{flow_length}-step.png')
    plt.savefig(file_path)
    plt.show()
    print(f"✅ Le graphique de flux d'intention de {flow_length} étapes est enregistré sous '{file_path}'")

def write_patterns_to_markdown(patterns, flow_length, output_dir):
    """
    Writes the intention flow patterns to a Markdown file in a table format.

    Args:
        patterns (dict): A dictionary of patterns and their frequencies.
        flow_length (int): The number of steps in the intention flow.
        output_dir (str): The directory to save the file.
    """
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'intention_flow_schema.md')
    
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"\n\n### Résultats d'analyse pour les flux d'intention de {flow_length} étapes\n")
        f.write("--------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("| Modèle de flux d'intention | Fréquence |\n")
        f.write("|----------------------------|-----------|\n")
        for i, (pattern, count) in enumerate(patterns.items()):
            if i >= 10:
                break
            f.write(f"| {pattern} | {count} |\n")
        f.write("--------------------------------------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    FILE_PATH = 'data/reconstructed_posts_final.json'
    FLOW_LENGTHS_TO_ANALYZE = [2, 5]

    for length in FLOW_LENGTHS_TO_ANALYZE:
        print(f"\n🚀 Analyse des flux d'intention de {length} étapes...")
        # Step 1: Analyze intention flow patterns
        flow_patterns = analyze_intention_flow(FILE_PATH, flow_length=length)
        
        if flow_patterns:
            # Step 2: Filter out repetitive patterns to show more meaningful transitions
            filtered_patterns = filter_repetitive_patterns(flow_patterns)
            
            # Write the filtered results to a markdown table file
            write_patterns_to_markdown(filtered_patterns, length, 'intention_flow_schema')
            print(f"✅ Les résultats d'analyse pour les flux d'intention de {length} étapes sont enregistrés dans 'intention_flow_schema/intention_flow_schema.md'")
        else:
            print(f"Aucun modèle de flux d'intention de {length} étapes trouvé. Veuillez vérifier le contenu de votre fichier JSON.")
