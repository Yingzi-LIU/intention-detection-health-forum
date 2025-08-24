import pandas as pd
from sklearn.model_selection import train_test_split

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

# --- 1. 加载数据 ---
df = pd.read_csv(FULL_DATA_PATH)
if 'ID' not in df.columns:
    raise ValueError("数据集中未找到 'ID' 列")

# --- 2. 创建组合标签列用于分析 ---
df['combined_labels'] = df[LABEL_COLS[0]].astype(str)
for col in LABEL_COLS[1:]:
    df['combined_labels'] += '_' + df[col].fillna('NA').astype(str)

# --- 辅助函数: 合并稀有类别 ---
def merge_rare_classes(df, label_col):
    counts = df[label_col].value_counts()
    df[label_col] = df[label_col].apply(lambda x: x if counts[x] > 1 else 'RARE_CLASS')
    return df

# --- 3. 分离固定训练集 30 条 ---
df_train_fixed = df[df['ID'].isin(SPECIFIC_30_IDS)].copy()
df_remaining = df[~df['ID'].isin(SPECIFIC_30_IDS)].copy()

# --- 4. 划分测试集（按 niveau1 分层，而不是 combined_labels）---
df_remaining = merge_rare_classes(df_remaining, 'niveau1')
df_remaining, df_test = train_test_split(
    df_remaining,
    test_size=TEST_SIZE,
    random_state=42,
    stratify=df_remaining['niveau1']
)

# --- 5. 划分随机训练集和验证集（按 niveau1 分层）---
random_train_size = 572 - len(df_train_fixed)  # 572 总训练集 - 30 固定
val_ratio = VAL_SIZE / len(df_remaining)

df_remaining = merge_rare_classes(df_remaining, 'niveau1')
df_random_train, df_val = train_test_split(
    df_remaining,
    test_size=val_ratio,
    random_state=42,
    stratify=df_remaining['niveau1']
)

# 如果随机训练集多于目标数量，裁剪
if len(df_random_train) > random_train_size:
    df_random_train = df_random_train.sample(n=random_train_size, random_state=42)

# --- 6. 合并训练集 ---
df_train_final = pd.concat([df_train_fixed, df_random_train])

# --- 7. 保存 ---
df_train_final.to_csv('data/dataset/train_dataset.csv', index=False, encoding='utf-8')
df_val.to_csv('data/dataset/validation_dataset.csv', index=False, encoding='utf-8')
df_test.to_csv('data/dataset/test_dataset.csv', index=False, encoding='utf-8')

# --- 8. 输出信息 ---
def print_distribution(df, name):
    print(f"\n{name} ({len(df)} 行) 分布统计:")
    print("-" * 40)
    print("niveau1 分布:")
    print(df['niveau1'].value_counts().sort_index())
    print("\n组合标签分布:")
    print(df['combined_labels'].value_counts().sort_index())
    print("\n子标签分布:")
    for col in LABEL_COLS:
        print(f"{col} 分布:")
        print(df[col].value_counts().sort_index())
        print("-" * 20)

print_distribution(df_train_final, "训练集")
print_distribution(df_val, "验证集")
print_distribution(df_test, "测试集")

# --- 9. 清理 ---
for d in [df, df_train_fixed, df_remaining, df_random_train, df_val, df_train_final, df_test]:
    if 'combined_labels' in d.columns:
        d.drop(columns=['combined_labels'], inplace=True, errors='ignore')

print("\n数据集划分完成：固定训练集 + 随机训练集 + 验证集 + 测试集，均按 niveau1 分层，可复现。")
