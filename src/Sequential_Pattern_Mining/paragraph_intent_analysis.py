import json
import os
from collections import Counter
from tabulate import tabulate

def load_data(file_path):
    """
    Loads reconstructed post data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        
    Returns:
        list: A list of post dictionaries.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def get_overall_intent_weighted(post):
    """
    Determines the overall intent of a post using a weighted voting method.
    
    Args:
        post (dict): A dictionary representing a post.
        
    Returns:
        tuple: The determined overall intent and the weighted scores.
    """
    sentences = post.get('sentences', [])
    if not sentences:
        return "NA_CATEGORY", {}

    # Define the weighting scheme
    weights = {
        'first_sentence': 3,
        'last_sentence': 2,
        'other': 1
    }
    
    intent_scores = Counter()
    
    for i, sentence in enumerate(sentences):
        # Use the level 1 label for the overall intent
        intent = sentence.get('niveau1', 'NA_CATEGORY')
        
        # Assign a weight based on the sentence's position
        if i == 0:
            weight = weights['first_sentence']
        elif i == len(sentences) - 1:
            weight = weights['last_sentence']
        else:
            weight = weights['other']
        
        intent_scores[intent] += weight

    # Find the intent with the highest score
    if intent_scores:
        overall_intent = intent_scores.most_common(1)[0][0]
    else:
        overall_intent = "NA_CATEGORY"

    return overall_intent, dict(intent_scores)

def main():
    FILE_PATH = 'data/reconstructed_posts_final.json'
    posts_data = load_data(FILE_PATH)
    if not posts_data:
        return

    print("==========================================================================")
    print("Analyzing overall post intent using the weighted voting method")
    print("==========================================================================\n")
    
    for post in posts_data:
        overall_intent, weighted_scores = get_overall_intent_weighted(post)
        post_id = post.get('post_id')
        
        print(f"✅ Analyzing Post ID: {post_id}")
        print(f"  Determined Overall Intent: {overall_intent}")
        
        # Display the weighted scores count
        table_data = [[intent, score] for intent, score in weighted_scores.items()]
        headers = ["Intent", "Weighted Score"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("\n")
        
    print("🎉 Analysis complete.")

if __name__ == '__main__':
    main()
