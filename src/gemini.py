import os
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import json
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report
import time
import random
import argparse

# Load environment variables from .env file
load_dotenv()

# --- 解析命令行参数 ---
parser = argparse.ArgumentParser(description='Process medical forum data with Gemini API.')
parser.add_argument('--num_samples', type=int, default=None,
                    help='Number of test samples to process (default: all)')
args = parser.parse_args()

try:
    API_KEY = os.getenv('GEMINI_API_KEY')
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error loading API Key: {e}")
    print("Please ensure you have a .env file in the same directory with your Gemini API Key named 'GEMINI_API_KEY'.")
    exit()

model = genai.GenerativeModel('models/gemini-2.5-flash')

# --- 2. 配置 Gemini API (如果之前没有运行) ---
# 使用环境变量中的 API 密钥，已在前面配置过
model = genai.GenerativeModel('models/gemini-2.0-flash-001')

# --- 3. 加载数据集 ---
test_file_path = 'data/dataset/test_dataset.csv'

try:
    test_df = pd.read_csv(test_file_path)
    print(f"测试集加载成功: {len(test_df)} 条数据")
except FileNotFoundError:
    print("请确保 'test_dataset.csv' 文件存在于指定路径下。")
    exit()

# 数据预处理：处理NA_CATEGORY
def process_categories(df):
    return df

test_df = process_categories(test_df)

# --- 4. 读取 Few-shot 示例 ---
try:
    few_shot_file_path = 'data/few_shot_examples.csv'
    few_shot_df = pd.read_csv(few_shot_file_path)
    few_shot_data = few_shot_df.to_dict('records')
    print(f"Few-shot 示例加载成功: {len(few_shot_data)} 条数据")
except FileNotFoundError:
    print(f"请确保 'few_shot_examples.csv' 文件存在于 '{few_shot_file_path}' 路径下。")
    exit()
except Exception as e:
    print(f"加载 Few-shot 示例失败: {e}")
    exit()

# --- 5. 构建 Prompt 函数 ---
def create_few_shot_prompt(text_to_classify, few_shot_examples):
    """
    根据few-shot示例构建Prompt。
    """
    few_shot_section = ""
    for ex in few_shot_examples:
        sentiment_present = ex['niveau3_1']
        polarity = ex['niveau3_2'] if sentiment_present == 'oui' else 'neutre' # 确保非情感文本的极性是 'neutre'

        few_shot_section += f"""
    **示例输入 (Exemple d'entrée):**
    "{ex['Sentences']}"

    **示例输出 (Exemple de sortie):**
    ```json
    {{
        "intention_generale": "{ex['niveau1']}",
        "objet_medical": "{ex['niveau2']}",
        "sentiment_analysis": {{
            "sentiment_present": "{sentiment_present}",
            "polarity": "{polarity}"
        }}
    }}
    ```
    """

    prompt = f"""
    你是一个专业的法语医学论坛内容分析助手。你需要对用户在法语医学论坛上发布的文本进行分析和分类。
    请根据以下三个维度对提供的文本进行分类，并以JSON格式输出结果：

    1.  **意图级别 (Niveau de l'intention générale)**：
        * "recherche_information" (信息查询)
        * "partage_experience" (经验分享)
        * "fonction_phatique" (寒暄或维持交流)

    2.  **医疗对象级别 (Niveau de l'objet médical)**：
        * "symptome" (症状)
        * "traitement" (治疗)
        * "diagnostique" (诊断)
        * "NA_CATEGORY" (不相关) (如果文本内容不涉及具体的医疗对象)

    3.  **情感分析级别 (Niveau sentiment analysis)**：
        * `sentiment_present`: "oui" (是) 或 "non" (否)
        * `polarity`: "positif" (积极), "négatif" (消极) 或 "NA_CATEGORY" (不相关) (仅当 `sentiment_present` 为 "oui" 时需要填写 `polarity`)

    请确保输出严格为JSON格式，包含 `intention_generale`, `objet_medical`, `sentiment_analysis` (包含 `sentiment_present` 和 `polarity`) 这三个顶层键。
    如果某个类别不适用，请将其设为 "NA_CATEGORY"。

    ---
    **Few-Shot 示例 (Exemples Few-Shot):**
    {few_shot_section}
    ---
    **要分类的文本 (Texte à classifier):**
    "{text_to_classify}"
    """
    return prompt

# --- 6. 对测试集全部数据进行分类推理 ---
predicted_niveau1 = []
predicted_niveau2 = []
predicted_niveau3_1 = []
predicted_niveau3_2 = []
actual_niveau1 = test_df['niveau1'].tolist()
actual_niveau2 = test_df['niveau2'].tolist()
actual_niveau3_1 = test_df['niveau3_1'].tolist()
actual_niveau3_2 = test_df['niveau3_2'].tolist()

# 获取测试集总样本数
total_test_samples = len(test_df)

# 如果用户指定了处理的样本数量，则只处理指定数量的样本
if args.num_samples is not None:
    total_test_samples = min(args.num_samples, total_test_samples)
    test_df = test_df.head(total_test_samples)
    print(f"\n--- 开始对测试集前 {total_test_samples} 个例子进行分类推理 ---")
else:
    print(f"\n--- 开始对测试集全部 {total_test_samples} 个例子进行分类推理 ---")

# 迭代测试集的所有行数据
for index, row in test_df.iterrows():
    text = row['Sentences']
    prompt = create_few_shot_prompt(text, few_shot_data)

    retries = 0
    max_retries = 5  # 最大重试次数
    base_delay = 5   # 初始延迟秒数

    while retries < max_retries:
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.2,
                    max_output_tokens=200
                )
            )

            raw_output = response.text.strip()
            # 清理并解析JSON
            if raw_output.startswith("```json"):
                json_str = raw_output[len("```json"):].strip()
                if json_str.endswith("```"):
                    json_str = json_str[:-len("```")].strip()
            else:
                json_str = raw_output

            classified_result = json.loads(json_str)

            predicted_niveau1.append(classified_result.get('intention_generale', '未知'))
            predicted_niveau2.append(classified_result.get('objet_medical', '未知'))

            sentiment_analysis = classified_result.get('sentiment_analysis', {})
            predicted_niveau3_1.append(sentiment_analysis.get('sentiment_present', '未知'))
            polarity = sentiment_analysis.get('polarity', '未知')
            if sentiment_analysis.get('sentiment_present') == 'non' and polarity == '未知':
                polarity = 'neutre'
            predicted_niveau3_2.append(polarity)

            # 如果成功，跳出重试循环
            break

        except Exception as e:
            if "429" in str(e): # 检查是否是配额错误
                retries += 1
                wait_time = base_delay * (2 ** (retries - 1)) + random.uniform(0, 1) # 指数增长并增加随机抖动
                print(f"处理文本 ID {row['ID']} 遇到配额错误 (429)。第 {retries}/{max_retries} 次重试，等待 {wait_time:.2f} 秒...")
                time.sleep(wait_time)
            else:
                # 其他错误，不重试
                print(f"处理文本 ID {row['ID']} 失败: {e}")
                print(f"原始模型输出:\n{response.text if 'response' in locals() else '无响应'}")
                predicted_niveau1.append('未知')
                predicted_niveau2.append('未知')
                predicted_niveau3_1.append('未知')
                predicted_niveau3_2.append('未知')
                break # 跳出重试循环，处理下一个样本
    else: # 如果所有重试都失败了
        print(f"处理文本 ID {row['ID']} 在 {max_retries} 次重试后仍然失败，跳过此项。")
        predicted_niveau1.append('未知')
        predicted_niveau2.append('未知')
        predicted_niveau3_1.append('未知')
        predicted_niveau3_2.append('未知')

    # 更新进度显示
    if (index + 1) % 10 == 0 or (index + 1) == total_test_samples:
        print(f"已处理 {index + 1}/{total_test_samples} 条数据...")

print("\n--- 分类推理完成 ---")

# --- 7. 评估模型性能 (对所有测试集数据进行评估) ---

# 注意：这里的 actual_niveauX 列表不再需要切片，因为 predicted 列表现在包含了所有数据
actual_niveau1_full = actual_niveau1
actual_niveau2_full = actual_niveau2
actual_niveau3_1_full = actual_niveau3_1
actual_niveau3_2_full = actual_niveau3_2


def evaluate_category(actual_labels, predicted_labels, category_name):
    print(f"\n--- 评估: {category_name} ---")

    # 过滤掉 '未知' 预测，只评估成功分类的部分
    filtered_actual = []
    filtered_predicted = []
    for a, p in zip(actual_labels, predicted_labels):
        if p != '未知':
            filtered_actual.append(a)
            filtered_predicted.append(p)

    if not filtered_actual:
        print(f"没有成功分类的数据用于评估 {category_name}。")
        return

    # 获取所有可能的标签，确保报告的完整性。
    # 从完整的数据集中获取所有可能的标签，确保报告的完整性。

    # 对于 niveau1
    if category_name == "意图级别 (Niveau 1)":
        # 只使用提示中定义的带下划线的标签
        all_possible_labels = ['fonction_phatique', 'partage_experience', 'recherche_information']

    # 对于 niveau2
    elif category_name == "医疗对象级别 (Niveau 2)":
        # 只使用指定的标签
        all_possible_labels = ['symptome', 'traitement', 'diagnostique', 'NA_CATEGORY']

    # 对于 niveau3.1
    elif category_name == "情感存在 (Niveau 3.1)":
        # 只使用指定的标签
        all_possible_labels = ['oui', 'non']

    # 对于 niveau3.2
    elif category_name == "情感极性 (Niveau 3.2)":
        # 只使用指定的标签
        all_possible_labels = ['positif', 'negatif', 'neutre', 'NA_CATEGORY']
    else:
        all_possible_labels = sorted(list(set(filtered_actual + filtered_predicted))) # 备用方案

    # 打印分类报告
    print(classification_report(filtered_actual, filtered_predicted, labels=all_possible_labels, zero_division=0))

    accuracy = accuracy_score(filtered_actual, filtered_predicted)
    print(f"准确率 (Accuracy): {accuracy:.4f}")


# 评估所有数据
evaluate_category(actual_niveau1_full, predicted_niveau1, "意图级别 (Niveau 1)")
evaluate_category(actual_niveau2_full, predicted_niveau2, "医疗对象级别 (Niveau 2)")
evaluate_category(actual_niveau3_1_full, predicted_niveau3_1, "情感存在 (Niveau 3.1)")
evaluate_category(actual_niveau3_2_full, predicted_niveau3_2, "情感极性 (Niveau 3.2)")

print("\n--- 评估完成 ---")