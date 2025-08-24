import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# --- 配置 ---
FULL_DATA_PATH = 'data/projet_annotation_sante_final_M1.csv'
SPECIFIC_30_IDS = [
    3, 24, 18, 17, 238, 242, 307, 324, 326, 656,
    4, 23, 32, 75, 201, 21, 8, 38, 98, 91,
    568, 505, 526, 41, 481, 154, 475, 6, 784, 15
]
LABEL_COLS = ['niveau1', 'niveau2', 'niveau3_1', 'niveau3_2']
TEST_SIZE = 300
VAL_SIZE = 100
MIN_CLASS_COUNT = 2

# --- 1. 加载数据 ---
df = pd.read_csv(FULL_DATA_PATH)

# 处理 NaN
nan_cols = df.isnull().sum()
if nan_cols.sum() > 0:
    print("\nColumns with NaN values before handling:")
    print(nan_cols[nan_cols > 0])
    df = df.fillna('NA_CATEGORY')
    print("NaN values have been replaced with 'NA_CATEGORY'.")
else:
    print("\nNo NaN values found in the dataset.")

if 'ID' not in df.columns:
    raise ValueError("数据集中未找到 'ID' 列")

# --- 2. 合并每列稀有类别 ---
def merge_rare_classes(df, label_col, min_count=2):
    counts = df[label_col].value_counts()
    rare_classes = counts[counts < min_count].index
    df[label_col] = df[label_col].apply(lambda x: x if x not in rare_classes else 'RARE_CLASS')
    return df

for col in LABEL_COLS:
    df = merge_rare_classes(df, col, min_count=MIN_CLASS_COUNT)

# --- 3. 创建组合标签 ---
df['combined_labels'] = df[LABEL_COLS].astype(str).agg('_'.join, axis=1)

# --- 3.1 全量合并单样本类别 ---
counts = df['combined_labels'].value_counts()
rare_classes = counts[counts < 2].index
if len(rare_classes) > 0:
    print("⚠️ 全量数据中以下组合标签只有 1 个样本，将它们合并为 RARE_CLASS：", rare_classes.tolist())
    df['combined_labels'] = df['combined_labels'].apply(
        lambda x: x if x not in rare_classes else 'RARE_CLASS'
    )

# --- 4. 拆出固定训练集 ---
df_train_fixed = df[df['ID'].isin(SPECIFIC_30_IDS)].copy()
df_remaining = df[~df['ID'].isin(SPECIFIC_30_IDS)].copy()

# --- 4.1 df_remaining 再次合并单样本类别 ---
df_remaining['combined_labels'] = df_remaining[LABEL_COLS].astype(str).agg('_'.join, axis=1)
counts_remaining = df_remaining['combined_labels'].value_counts()
rare_classes_remaining = counts_remaining[counts_remaining < 2].index
df_remaining['combined_labels'] = df_remaining['combined_labels'].apply(
    lambda x: x if x not in rare_classes_remaining else 'RARE_CLASS'
)

# --- 4.2 如果 RARE_CLASS 只有 1 个样本，直接放入训练集 ---
rare_count = df_remaining[df_remaining['combined_labels']=='RARE_CLASS'].shape[0]
if rare_count == 1:
    df_train_fixed = pd.concat([df_train_fixed, df_remaining[df_remaining['combined_labels']=='RARE_CLASS']])
    df_remaining = df_remaining[df_remaining['combined_labels']!='RARE_CLASS']

# --- 4.3 确保每个组合标签至少有2个样本，以便进行分层划分 ---
counts_remaining = df_remaining['combined_labels'].value_counts()
rare_classes_remaining = counts_remaining[counts_remaining < 2].index
if len(rare_classes_remaining) > 0:
    print("⚠️ 剩余数据中以下组合标签只有 1 个样本，将它们合并为 RARE_CLASS：", rare_classes_remaining.tolist())
    df_remaining['combined_labels'] = df_remaining['combined_labels'].apply(
        lambda x: x if x not in rare_classes_remaining else 'RARE_CLASS'
    )

# --- 5. 划分测试集 ---
df_remaining, df_test = train_test_split(
    df_remaining,
    test_size=TEST_SIZE,
    random_state=42,
    stratify=df_remaining['combined_labels']
)

# --- 6. 划分随机训练集和验证集 ---
random_train_size = 572 - len(df_train_fixed)
val_ratio = VAL_SIZE / len(df_remaining)

# 确保验证集划分时每个类别至少有2个样本
counts_remaining = df_remaining['combined_labels'].value_counts()
rare_classes_remaining = counts_remaining[counts_remaining < 2].index
if len(rare_classes_remaining) > 0:
    print("⚠️ 验证集划分前，以下组合标签只有 1 个样本，将它们合并为 RARE_CLASS：", rare_classes_remaining.tolist())
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

# --- 7. 合并训练集 ---
df_train_final = pd.concat([df_train_fixed, df_random_train])

# --- 8. 保存 CSV ---
df_train_final.to_csv('data/dataset/train_dataset.csv', index=False, encoding='utf-8')
df_val.to_csv('data/dataset/validation_dataset.csv', index=False, encoding='utf-8')
df_test.to_csv('data/dataset/test_dataset.csv', index=False, encoding='utf-8')

# --- 9. 打印 & 保存分布 ---
def print_distribution(df, name):
    print(f"\n{name} ({len(df)} 行) 分布统计:")
    print("-" * 40)
    print("组合标签分布:")
    print(df['combined_labels'].value_counts().sort_index())
    print("\n子标签分布:")
    for col in LABEL_COLS:
        print(f"{col} 分布:")
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

# --- 10. 绘制分布条形图 ---
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

        plt.title(f"Répartition des étiquettes ({col})", fontsize=14)
        plt.xlabel("Étiquettes", fontsize=12)
        plt.ylabel("Nombre d'échantillons", fontsize=12)
        plt.xticks(x + width, all_labels, rotation=45, ha="right")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{save_path_prefix}_{col}.png", dpi=150)
        plt.close()

dfs = {"train": df_train_final, "validation": df_val, "test": df_test}
labels = {"train": "Entraînement", "validation": "Validation", "test": "Test"}

plot_distribution_grouped(dfs, labels, ['combined_labels'] + LABEL_COLS)

print("\n✅ 数据集划分完成：固定训练集 + 随机训练集 + 验证集 + 测试集，稀有类别合并 + 分布图保存完成。")
