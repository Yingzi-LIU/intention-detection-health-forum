import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# --- Configuration ---
FULL_DATA_PATH = 'data/projet_annotation_sante_final_M1.csv'
SPECIFIC_20_IDS = [
    3, 24, 18, 17, 238, 242, 307, 324, 326, 656,
    4, 23, 32, 75, 201, 21, 8, 38, 98, 91,
    568, 505, 526, 41, 481, 154, 475, 6, 784, 15
]
LABEL_COLS = ['niveau1', 'niveau2', 'niveau3']
TEST_SIZE = 300
VAL_SIZE = 100
MIN_CLASS_COUNT = 2

# --- 1. Load Data ---
df = pd.read_csv(FULL_DATA_PATH)

# Handle NaN values
nan_cols = df.isnull().sum()
if nan_cols.sum() > 0:
    print("\nColumns with NaN values before handling:")
    print(nan_cols[nan_cols > 0])
    df = df.fillna('NA_CATEGORY')
    print("NaN values have been replaced with 'NA_CATEGORY'.")
else:
    print("\nNo NaN values found in the dataset.")

if 'ID' not in df.columns:
    raise ValueError("Column 'ID' not found in the dataset")

# --- 2. Merge Rare Classes per Column ---
def merge_rare_classes(df, label_col, min_count=2):
    counts = df[label_col].value_counts()
    rare_classes = counts[counts < min_count].index
    df[label_col] = df[label_col].apply(lambda x: x if x not in rare_classes else 'RARE_CLASS')
    return df

for col in LABEL_COLS:
    df = merge_rare_classes(df, col, min_count=MIN_CLASS_COUNT)

# --- 3. Create Combined Labels ---
df['combined_labels'] = df[LABEL_COLS].astype(str).agg('_'.join, axis=1)

# --- 3.1 Merge Single-Sample Classes in Full Dataset ---
counts = df['combined_labels'].value_counts()
rare_classes = counts[counts < 2].index
if len(rare_classes) > 0:
    print("⚠️ The following combined labels in the full dataset have only 1 sample and will be merged into RARE_CLASS:", rare_classes.tolist())
    df['combined_labels'] = df['combined_labels'].apply(
        lambda x: x if x not in rare_classes else 'RARE_CLASS'
    )

# --- 4. Split Fixed Training Set ---
df_train_fixed = df[df['ID'].isin(SPECIFIC_20_IDS)].copy()
df_remaining = df[~df['ID'].isin(SPECIFIC_20_IDS)].copy()

# --- 4.1 df_remaining: Merge Single-Sample Classes Again ---
df_remaining['combined_labels'] = df_remaining[LABEL_COLS].astype(str).agg('_'.join, axis=1)
counts_remaining = df_remaining['combined_labels'].value_counts()
rare_classes_remaining = counts_remaining[counts_remaining < 2].index
df_remaining['combined_labels'] = df_remaining['combined_labels'].apply(
    lambda x: x if x not in rare_classes_remaining else 'RARE_CLASS'
)

# --- 4.2 If RARE_CLASS has only 1 sample, add it directly to the training set ---
rare_count = df_remaining[df_remaining['combined_labels']=='RARE_CLASS'].shape[0]
if rare_count == 1:
    df_train_fixed = pd.concat([df_train_fixed, df_remaining[df_remaining['combined_labels']=='RARE_CLASS']])
    df_remaining = df_remaining[df_remaining['combined_labels']!='RARE_CLASS']

# --- 4.3 Ensure each combined label has at least 2 samples for stratified splitting ---
counts_remaining = df_remaining['combined_labels'].value_counts()
rare_classes_remaining = counts_remaining[counts_remaining < 2].index
if len(rare_classes_remaining) > 0:
    print("⚠️ The following combined labels in the remaining data have only 1 sample and will be merged into RARE_CLASS:", rare_classes_remaining.tolist())
    df_remaining['combined_labels'] = df_remaining['combined_labels'].apply(
        lambda x: x if x not in rare_classes_remaining else 'RARE_CLASS'
    )

# --- 5. Split Test Set ---
df_remaining, df_test = train_test_split(
    df_remaining,
    test_size=TEST_SIZE,
    random_state=42,
    stratify=df_remaining['combined_labels']
)

# --- 6. Split Random Training and Validation Sets ---
random_train_size = 572 - len(df_train_fixed)
val_ratio = VAL_SIZE / len(df_remaining)

# Ensure each category has at least 2 samples for validation set splitting
counts_remaining = df_remaining['combined_labels'].value_counts()
rare_classes_remaining = counts_remaining[counts_remaining < 2].index
if len(rare_classes_remaining) > 0:
    print("⚠️ Before validation set splitting, the following combined labels have only 1 sample and will be merged into RARE_CLASS:", rare_classes_remaining.tolist())
    df_remaining['combined_labels'] = df_remaining['combined_labels'].apply(
        lambda x: x if x not in rare_classes_remaining else 'RARE_CLASS'
    )

df_random_train, df_val = train_test_split(
    df_remaining,
    test_size=val_ratio,
    random_state=42,
    stratify=df_remaining['combined_labels']
)

if len(df_random_train) > random_train_size:
    df_random_train = df_random_train.sample(n=random_train_size, random_state=42)

# --- 7. Merge Training Sets ---
df_train_final = pd.concat([df_train_fixed, df_random_train])

# --- 8. Save CSV ---
df_train_final.to_csv('data/dataset/train_dataset.csv', index=False, encoding='utf-8')
df_val.to_csv('data/dataset/validation_dataset.csv', index=False, encoding='utf-8')
df_test.to_csv('data/dataset/test_dataset.csv', index=False, encoding='utf-8')

# --- 9. Print & Save Distribution ---
def print_distribution(df, name):
    print(f"\n{name} ({len(df)} rows) Distribution Statistics:")
    print("-" * 40)
    print("Combined Label Distribution:")
    print(df['combined_labels'].value_counts().sort_index())
    print("\nSub-label Distribution:")
    for col in LABEL_COLS:
        print(f"{col} Distribution:")
        print(df[col].value_counts().sort_index())
        print("-" * 20)

def save_distribution(df, name):
    rows = []
    for col in ['combined_labels'] + LABEL_COLS:
        counts = df[col].value_counts().sort_index()
        total = len(df)
        for label, count in counts.items():
            rows.append({
                'dataset': name,
                'label_type': col,
                'label': label,
                'count': count,
                'percentage': count / total
            })
    pd.DataFrame(rows).to_csv(f'data/dataset/distribution/{name}_distribution.csv', index=False, encoding='utf-8')

print_distribution(df_train_final, "训练集")
print_distribution(df_val, "验证集")
print_distribution(df_test, "测试集")

save_distribution(df_train_final, "train")
save_distribution(df_val, "validation")
save_distribution(df_test, "test")

# --- 10. Plot Distribution Bar Chart ---
def plot_distribution_grouped(dfs, labels, cols, save_path_prefix="data/dataset/distribution/dist_plot"):
    for col in cols:
        all_labels = sorted(set().union(*[df[col].unique() for df in dfs.values()]))
        x = np.arange(len(all_labels))
        width = 0.25

        plt.figure(figsize=(12,6))
        for i, (name, df) in enumerate(dfs.items()):
            counts = df[col].value_counts()
            values = [counts.get(label, 0) for label in all_labels]
            plt.bar(x + i*width, values, width=width, alpha=0.8, label=labels[name])

        plt.title(f"Label Distribution ({col})", fontsize=14)
        plt.xlabel("Labels", fontsize=12)
        plt.ylabel("Number of Samples", fontsize=12)
        plt.xticks(x + width, all_labels, rotation=45, ha="right")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{save_path_prefix}_{col}.png", dpi=150)
        plt.close()

dfs = {"train": df_train_final, "validation": df_val, "test": df_test}
labels = {"train": "Entraînement", "validation": "Validation", "test": "Test"}

plot_distribution_grouped(dfs, labels, ['combined_labels'] + LABEL_COLS)

print("\n✅ Dataset splitting complete: fixed training set + random training set + validation set + test set, rare classes merged + distribution plots saved.")
