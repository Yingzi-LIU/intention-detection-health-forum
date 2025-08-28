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
        # 现在 few_shot_examples 中的 'niveau3' 直接包含情感标签
        emotion_label = ex['niveau3']

        few_shot_section += f"""
    **示例输入 (Exemple d'entrée):**
    "{ex['Sentences']}"

    **示例输出 (Exemple de sortie):**
    ```json
    {{
        "intention_generale": "{ex['niveau1']}",
        "objet_medical": "{ex['niveau2']}",
        "emotion": "{emotion_label}"
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

    3.  **情感级别 (Niveau emotion)**：
        * "positif" (积极)
        * "negatif" (消极)
        * "non" (无情感)
        * "NA_CATEGORY" (不相关)

    请确保输出严格为JSON格式，包含 `intention_generale`, `objet_medical`, `emotion` 这三个顶层键。
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
    emotion = classified_result.get('emotion', '未知') # 获取新的 'emotion' 键

    def get_response_strategy(intention, medical_object, emotion):
        # 意图: recherche_information (信息查询)
        if intention == "recherche_information":
            if medical_object == "symptome":
                if emotion == "positif":
                    return "用户对症状持积极态度，可能是在寻求确认或进一步了解。请提供关于症状的常见信息，并建议用户咨询医生以获取专业意见。"
                elif emotion == "negatif":
                    return "用户对症状感到担忧或不适。请提供安慰，给出关于症状的常见信息，并强烈建议用户尽快咨询医生。"
                else: # non / NA_CATEGORY
                    return "用户正在查询症状信息。请提供关于症状的常见信息，并建议用户咨询医生。"
            elif medical_object == "traitement":
                if emotion == "positif":
                    return "用户对治疗有积极的期望或正在分享治疗进展。请提供治疗相关的一般信息，并强调遵循医嘱的重要性。"
                elif emotion == "negatif":
                    return "用户对治疗感到沮丧、担忧或不满意。请提供支持和理解，建议用户回顾治疗方案或寻求第二意见。"
                else: # non / NA_CATEGORY
                    return "用户正在查询治疗信息。请提供治疗相关的一般信息，并强调遵循医嘱的重要性。"
            elif medical_object == "diagnostique":
                if emotion == "positif":
                    return "用户对诊断结果持积极态度，可能是在寻求确认或了解更多。请提供诊断相关的一般信息，并建议用户与医生讨论后续步骤。"
                elif emotion == "negatif":
                    return "用户对诊断结果感到困惑、担忧或沮丧。请提供安慰和支持，建议用户寻求进一步的解释或第二意见。"
                else: # non / NA_CATEGORY
                    return "用户正在查询诊断信息。请提供诊断相关的一般信息，并建议用户与医生讨论后续步骤。"
            else: # medical_object == "NA_CATEGORY"
                return "用户正在查询信息，但医疗对象不明确。请提供通用健康信息或建议用户提供更具体的问题。"
        
        # 意图: partage_experience (经验分享)
        elif intention == "partage_experience":
            if medical_object == "symptome":
                if emotion == "positif":
                    return "用户积极分享症状经验。请鼓励用户分享更多细节，例如症状如何开始、持续多久、以及采取了哪些措施。同时，可以询问他们是否有任何积极的应对策略可以分享给其他社区成员。"
                elif emotion == "negatif":
                    return "用户消极分享症状经验。请表达同情和理解，鼓励用户详细描述他们的感受和遇到的挑战。可以询问他们目前正在寻求哪些支持，并提醒他们社区成员都在这里倾听和支持。"
                else: # non / NA_CATEGORY
                    return "用户正在分享症状经验。请鼓励用户分享更多细节，并提供支持。"
            elif medical_object == "traitement":
                if emotion == "positif":
                    return "用户积极分享治疗经验。请鼓励用户分享治疗过程中的亮点、有效的策略或他们认为有帮助的资源。可以询问他们对其他正在经历类似治疗的成员有什么建议。"
                elif emotion == "negatif":
                    return "用户消极分享治疗经验。请表达同情和理解，鼓励用户分享治疗中遇到的困难、副作用或挫折。可以询问他们希望从社区获得哪些支持或建议，并提醒他们寻求专业帮助的重要性。"
                else: # non / NA_CATEGORY
                    return "用户正在分享治疗经验。请鼓励用户分享更多细节，并提供支持。"
            elif medical_object == "diagnostique":
                if emotion == "positif":
                    return "用户积极分享诊断经验。请鼓励用户分享诊断过程中的关键信息、他们是如何接受诊断的，以及他们采取了哪些积极的应对措施。可以询问他们是否有任何资源或建议可以分享给新确诊的成员。"
                elif emotion == "negatif":
                    return "用户消极分享诊断经验。请表达同情和理解，鼓励用户分享诊断带来的情感冲击、困惑或挑战。可以询问他们目前最需要哪些方面的支持，并提醒他们寻求心理健康支持的重要性。"
                else: # non / NA_CATEGORY
                    return "用户正在分享诊断经验。请鼓励用户分享更多细节，并提供支持。"
            else: # medical_object == "NA_CATEGORY"
                return "用户正在分享经验，但医疗对象不明确。请鼓励用户分享更多细节，并提供通用支持。"

        # 意图: fonction_phatique (寒暄或维持交流)
        elif intention == "fonction_phatique":
            return "请给予友好的回应，鼓励用户继续参与社区讨论。"
        
        # 未知意图
        else:
            return "无法识别意图，请提供通用且礼貌的回复，并引导用户提供更清晰的信息。"

    response_strategy = get_response_strategy(intention, medical_object, emotion)

    response_prompt = f"""
    用户在医学论坛上发布了以下内容: "{user_input}"

    该内容的分类结果如下:
    - 意图级别: {intention}
    - 医疗对象级别: {medical_object}
    - 情感级别: {emotion}

    请根据这些分类结果，以一个专业的医学论坛助手的身份，给出一个合理且有帮助的回复。
    {response_strategy}
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