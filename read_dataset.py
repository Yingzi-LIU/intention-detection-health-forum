import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt # 新增这一行
import seaborn as sns

# 加载您的CSV文件
file_path = 'data/projet_annotation_sante_final_M1.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Successfully loaded '{file_path}'. Shape: {df.shape}")
except FileNotFoundError:
    print(f"Error: '{file_path}' not found. Please ensure the file is uploaded to your Colab environment.")
    exit()

# 检查并处理可能存在的NaN值
nan_cols = df.isnull().sum()
nan_cols = nan_cols[nan_cols > 0]
if not nan_cols.empty:
    print("\nColumns with NaN values before handling:")
    print(nan_cols)
    df = df.fillna('NA_CATEGORY')
    print("NaN values have been replaced with 'NA_CATEGORY'.")
else:
    print("\nNo NaN values found in the dataset.")


# 假设您的标签列与描述一致：
# 请根据您的CSV文件中的实际列名进行调整。
label_col1 = 'niveau1' # 请根据您的CSV文件中的实际列名调整
label_col2 = 'niveau2'       # 请根据您的CSV文件中的实际列名调整
label_col3 = 'niveau3' # 新的级别3列名

# 确保这些列存在
for col in [label_col1, label_col2, label_col3]:
    if col not in df.columns:
        print(f"Error: Label column '{col}' not found in the DataFrame. Please check your CSV column names.")
        exit()
# --- 新增代码：在划分前分析原始数据标签分布 ---
print("\n--- Analyzing Original Dataset Label Distribution ---")
label_cols_to_plot = [label_col1, label_col2, label_col3]

for col in label_cols_to_plot:
    plt.figure(figsize=(12, 6))
    
    # 统计每个标签的频率
    label_counts = df[col].astype(str).value_counts().sort_values(ascending=True)  # 横向图通常从下到上排序
    
    # 横向条形图
    sns.barplot(y=label_counts.index, x=label_counts.values, palette='viridis')
    
    # 添加标题和标签
    plt.title(f'Distribution of Label: {col} in Original Dataset', fontsize=16)
    plt.xlabel('Frequency', fontsize=12)
    plt.ylabel('Label Categories', fontsize=12)
    
    # 在条形图上显示具体数值
    for index, value in enumerate(label_counts.values):
        plt.text(value + max(label_counts.values)*0.01, index, str(value), va='center')
    
    plt.tight_layout()
    plt.savefig(f'schema/distribution_{col}.png') # Save the plot
    plt.close() # Close the plot to free up memory

print("Original dataset label distribution analysis complete. Proceeding with data splitting.")
# --- 新增代码结束 ---

