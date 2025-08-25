import os
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import json
import time
import random

# Load environment variables from .env file
load_dotenv()

try:
    API_KEY = os.getenv('GEMINI_API_KEY')
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error loading API Key: {e}")
    print("Please ensure you have a .env file in the same directory with your Gemini API Key named 'GEMINI_API_KEY'.")
    exit()

model = genai.GenerativeModel('models/gemini-2.0-flash-001')

# --- 3. 加载 Few-shot 示例 ---
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

while True:
    user_input = input("\n请输入您的医学论坛问题 (或输入 'exit' 退出): ")
    if user_input.lower() == 'exit':
        print("感谢使用，再见！")
        break

    print("\n--- 正在分类您的输入 ---")
    classification_prompt = create_few_shot_prompt(user_input, few_shot_data)

    retries = 0
    max_retries = 5
    base_delay = 5

    classified_result = None
    while retries < max_retries:
        try:
            response = model.generate_content(
                classification_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.2,
                    max_output_tokens=200
                )
            )

            raw_output = response.text.strip()
            if raw_output.startswith("```json"):
                json_str = raw_output[len("```json"):].strip()
                if json_str.endswith("```"):
                    json_str = json_str[:-len("```")].strip()
            else:
                json_str = raw_output

            classified_result = json.loads(json_str)
            print("\n--- 分类结果 ---")
            print(json.dumps(classified_result, indent=2, ensure_ascii=False))
            break

        except Exception as e:
            if "429" in str(e):
                retries += 1
                wait_time = base_delay * (2 ** (retries - 1)) + random.uniform(0, 1)
                print(f"分类遇到配额错误 (429)。第 {retries}/{max_retries} 次重试，等待 {wait_time:.2f} 秒...")
                time.sleep(wait_time)
            else:
                print(f"分类失败: {e}")
                print(f"原始模型输出:\n{response.text if 'response' in locals() else '无响应'}")
                classified_result = None
                break
    
    if classified_result is None:
        print("无法分类您的输入，请稍后再试。")
        continue

    # --- 根据分类结果生成回复 ---
    intention = classified_result.get('intention_generale', '未知')
    medical_object = classified_result.get('objet_medical', '未知')
    sentiment_present = classified_result.get('sentiment_analysis', {}).get('sentiment_present', '未知')
    polarity = classified_result.get('sentiment_analysis', {}).get('polarity', '未知')

    response_prompt = f"""
    用户在医学论坛上发布了以下内容: "{user_input}"

    该内容的分类结果如下:
    - 意图级别: {intention}
    - 医疗对象级别: {medical_object}
    - 情感存在: {sentiment_present}
    - 情感极性: {polarity}

    请根据这些分类结果，以一个专业的医学论坛助手的身份，给出一个合理且有帮助的回复。
    如果意图是 "recherche_information" 且医疗对象是 "symptome"，请提供一些关于症状的常见信息或建议用户咨询医生。
    如果意图是 "partage_experience"，请鼓励用户分享更多细节或提供支持。
    如果意图是 "fonction_phatique"，请给予友好的回应。
    请确保回复是法语。
    """

    print("\n--- 正在生成回复 ---")
    retries = 0
    generated_response = None
    while retries < max_retries:
        try:
            response = model.generate_content(
                response_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7, # 提高温度以获得更多创造性的回复
                    max_output_tokens=500
                )
            )
            generated_response = response.text.strip()
            print("\n--- 助手回复 ---")
            print(generated_response)
            break
        except Exception as e:
            if "429" in str(e):
                retries += 1
                wait_time = base_delay * (2 ** (retries - 1)) + random.uniform(0, 1)
                print(f"生成回复遇到配额错误 (429)。第 {retries}/{max_retries} 次重试，等待 {wait_time:.2f} 秒...")
                time.sleep(wait_time)
            else:
                print(f"生成回复失败: {e}")
                print(f"原始模型输出:\n{response.text if 'response' in locals() else '无响应'}")
                generated_response = "抱歉，无法生成回复。请稍后再试。"
                break
    
    if generated_response is None:
        print("抱歉，无法生成回复。请稍后再试。")