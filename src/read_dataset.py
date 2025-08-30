import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
file_path = 'data/projet_annotation_sante_final_M1.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Successfully loaded '{file_path}'. Shape: {df.shape}")
except FileNotFoundError:
    print(f"Error: '{file_path}' not found. Please ensure the file is uploaded to your Colab environment.")
    exit()

# Check and handle potential NaN values
nan_cols = df.isnull().sum()
nan_cols = nan_cols[nan_cols > 0]
if not nan_cols.empty:
    print("\nColumns with NaN values before handling:")
    print(nan_cols)
    df = df.fillna('NA_CATEGORY')
    print("NaN values have been replaced with 'NA_CATEGORY'.")
else:
    print("\nNo NaN values found in the dataset.")




label_col1 = 'niveau1' 
label_col2 = 'niveau2'       
label_col3 = 'niveau3' 


for col in [label_col1, label_col2, label_col3]:
    if col not in df.columns:
        print(f"Error: Label column '{col}' not found in the DataFrame. Please check your CSV column names.")
        exit()
# Analyze original data label distribution before splitting 
print("\n--- Analyzing Original Dataset Label Distribution ---")
label_cols_to_plot = [label_col1, label_col2, label_col3]

for col in label_cols_to_plot:
    plt.figure(figsize=(12, 6))
    
    # Count the frequency of each label
    label_counts = df[col].astype(str).value_counts().sort_values(ascending=True)  # Horizontal charts are usually sorted from bottom to top
    
    # Horizontal bar chart
    sns.barplot(y=label_counts.index, x=label_counts.values, palette='viridis')
    
    # Add title and labels
    plt.title(f'Distribution of Label: {col} in Original Dataset', fontsize=16)
    plt.xlabel('Frequency', fontsize=12)
    plt.ylabel('Label Categories', fontsize=12)
    
    # Display specific values on the bar chart
    for index, value in enumerate(label_counts.values):
        plt.text(value + max(label_counts.values)*0.01, index, str(value), va='center')
    
    plt.tight_layout()
    plt.savefig(f'schema/distribution_{col}.png') # Save the plot
    plt.close() # Close the plot to free up memory

print("Original dataset label distribution analysis complete. Proceeding with data splitting.")


