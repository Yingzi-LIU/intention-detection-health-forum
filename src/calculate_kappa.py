import pandas as pd
import numpy as np

def fleiss_kappa(data, annotators=3):
    """
    Calculates the Fleiss' Kappa for a given dataset.

    Args:
        data (pd.DataFrame): The input DataFrame.
        annotators (int): The number of annotators.

    Returns:
        dict: A dictionary of kappa values for each category.
    """
    kappa_results = {}
    
    # Process each set of columns (each category)
    for i in range(0, data.shape[1], annotators):
        category_name = f'niveau_{i//annotators + 1}'
        
        # Extract the annotations for the current category
        annotations = data.iloc[:, i:i+annotators].copy()
        
        # Drop rows where all annotations for the category are empty
        annotations.dropna(how='all', inplace=True)
        
        # If no data is left for this category, skip
        if annotations.empty:
            kappa_results[category_name] = np.nan
            continue
            
        # Get all unique labels, excluding empty strings and NaN
        all_labels = pd.unique(annotations.values.ravel('K'))
        all_labels = [label for label in all_labels if pd.notna(label) and label != '']
        
        # If there's only one label, kappa is not well-defined.
        if len(all_labels) <= 1:
            kappa_results[category_name] = np.nan
            continue
        
        n = len(annotations)
        k = annotators
        
        counts_matrix = np.zeros((n, len(all_labels)))
        label_to_col = {label: j for j, label in enumerate(all_labels)}
        
        for item_idx, row in annotations.iterrows():
            for label in row:
                if pd.notna(label) and label != '':
                    if label in label_to_col:
                        counts_matrix[annotations.index.get_loc(item_idx), label_to_col[label]] += 1
        
        p0_numerator = np.sum(np.sum(counts_matrix * (counts_matrix - 1), axis=1))
        p0_denominator = n * k * (k - 1)
        
        if p0_denominator == 0:
            P_0 = 1.0
        else:
            P_0 = p0_numerator / p0_denominator
        
        p_j = np.sum(counts_matrix, axis=0) / (n * k)
        P_e = np.sum(p_j**2)
        
        if 1 - P_e == 0:
            kappa = 1.0
        else:
            kappa = (P_0 - P_e) / (1 - P_e)
            
        kappa_results[category_name] = kappa
        
    return kappa_results

def check_agreement_issues(data, category_index, annotators=3):
    """
    Identifies and prints rows with disagreements for a specific category.

    Args:
        data (pd.DataFrame): The input DataFrame.
        category_index (int): The index of the category to check (0-based).
        annotators (int): The number of annotators.
    """
    print(f"\n--- Analysing Disagreements for Niveau_{category_index + 1} ---")
    
    # Get the columns for the specified category
    start_col = category_index * annotators
    end_col = start_col + annotators
    annotations = data.iloc[:, start_col:end_col].copy()

    # Find rows where not all values are the same
    # Use .nunique(axis=1) to find rows with more than one unique value
    disagreements = annotations[annotations.nunique(axis=1) > 1]
    
    if disagreements.empty:
        print("No disagreements found for this category.")
    else:
        print(f"Found {len(disagreements)} rows with disagreements:")
        print(disagreements)

    # Analyze individual annotator distribution
    print("\n--- Annotator Distribution Analysis for Niveau_{category_index + 1} ---")
    for j in range(annotators):
        annotator_col = annotations.columns[j]
        distribution = annotations[annotator_col].value_counts(normalize=True).round(4)
        print(f"Annotator {j+1} Distribution:\n{distribution}\n")

# Main script
# Load your data from a CSV file
df = pd.read_csv('data/accord_annotation.csv', header=None, on_bad_lines='skip')

# Replace empty strings with NaN for consistent processing
df.replace('', np.nan, inplace=True)

# Drop any rows that are completely empty
df.dropna(how='all', inplace=True)

# The fillna with method='ffill' is now deprecated, let's use the new way.
df.ffill(inplace=True)

# Run the Fleiss' Kappa calculation
kappa_scores = fleiss_kappa(df, annotators=3)

# Print the results
print("Fleiss' Kappa Scores per Category:")
for category, score in kappa_scores.items():
    print(f"{category.capitalize()}: {score:.4f}")

# Call the new function to check for disagreements in Niveau_2
# The index for Niveau_2 is 1 (since it's 0-based)
check_agreement_issues(df, category_index=1, annotators=3)