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

# --- 5. Build Prompt Function ---
def create_few_shot_prompt(text_to_classify, few_shot_examples):
    """
    Builds a prompt based on few-shot examples.
    """
    few_shot_section = ""
    for ex in few_shot_examples:
        
        emotion_label = ex['niveau3']

        few_shot_section += f"""
    **(Exemple d'entrée):**
    "{ex['Sentences']}"

    **(Exemple de sortie):**
    ```json
    {{
        "intention_generale": "{ex['niveau1']}",
        "objet_medical": "{ex['niveau2']}",
        "emotion": "{emotion_label}"
    }}
    ```
    """

    prompt = f"""
    Vous êtes un assistant professionnel d'analyse de contenu de forum médical français. Vous devez analyser et classer les textes publiés par les utilisateurs sur un forum médical français.
    Veuillez classer le texte fourni selon les trois dimensions suivantes et afficher les résultats au format JSON :

    1.  **Niveau de l'intention générale** :
        * "recherche_information" (Recherche d'informations)
        * "partage_experience" (Partage d'expérience)
        * "fonction_phatique" (Salutations ou maintien de la communication)

    2.  **Niveau de l'objet médical** :
        * "symptome" (Symptôme)
        * "traitement" (Traitement)
        * "diagnostique" (Diagnostic)
        * "NA_CATEGORY" (Non pertinent) (Si le contenu du texte ne concerne pas un objet médical spécifique)

    3.  **Niveau émotionnel** :
        * "positif" (Positif)
        * "negatif" (Négatif)
        * "non" (Neutre)
        * "NA_CATEGORY" (Non pertinent)

    Veuillez vous assurer que la sortie est strictement au format JSON et contient les trois clés de niveau supérieur : `intention_generale`, `objet_medical`, `emotion`.
    Si une catégorie n'est pas applicable, veuillez la définir sur "NA_CATEGORY".

    ---
    **(Exemples Few-Shot):**
    {few_shot_section}
    ---
    **(Texte à classifier):**
    "{text_to_classify}"
    """
    return prompt

while True:
    user_input = input("\nVeuillez entrer votre question sur le forum médical (ou tapez 'exit' pour quitter) : ")
    if user_input.lower() == 'exit':
        print("Merci d'avoir utilisé, au revoir !")
        break

    print("\n--- Classification de votre entrée en cours ---")
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
            print("\n--- Résultats de la classification ---")
            print(json.dumps(classified_result, indent=2, ensure_ascii=False))
            break

        except Exception as e:
            if "429" in str(e):
                retries += 1
                wait_time = base_delay * (2 ** (retries - 1)) + random.uniform(0, 1)
                print(f"Erreur de quota (429) rencontrée lors de la classification. Tentative {retries}/{max_retries}, attente de {wait_time:.2f} secondes...")
                time.sleep(wait_time)
            else:
                print(f"Échec de la classification : {e}")
                print(f"Sortie brute du modèle :\n{response.text if 'response' in locals() else 'Aucune réponse'}")
                classified_result = None
                break
    
    if classified_result is None:
        print("Impossible de classer votre entrée, veuillez réessayer plus tard.")
        continue


   intention = classified_result.get('intention_generale', 'inconnu')
    medical_object = classified_result.get('objet_medical', 'inconnu')
    emotion = classified_result.get('emotion', 'inconnu') 

    def get_response_strategy(intention, medical_object, emotion):
        # Intention: recherche_information (Information seeking)
        if intention == "recherche_information":
            if medical_object == "symptome":
                if emotion == "positif":
                    return "L'utilisateur a une attitude positive envers les symptômes, il cherche peut-être une confirmation ou des informations supplémentaires. Veuillez fournir des informations générales sur les symptômes et conseiller à l'utilisateur de consulter un médecin pour un avis professionnel."
                elif emotion == "negatif":
                    return "L'utilisateur est préoccupé ou mal à l'aise avec les symptômes. Veuillez offrir du réconfort, fournir des informations générales sur les symptômes et fortement conseiller à l'utilisateur de consulter un médecin dès que possible."
                else: # non / NA_CATEGORY
                    return "L'utilisateur recherche des informations sur les symptômes. Veuillez fournir des informations générales sur les symptômes et conseiller à l'utilisateur de consulter un médecin."
            elif medical_object == "traitement":
                if emotion == "positif":
                    return "L'utilisateur a des attentes positives concernant le traitement ou partage des progrès. Veuillez fournir des informations générales sur le traitement et souligner l'importance de suivre les conseils médicaux."
                elif emotion == "negatif":
                    return "L'utilisateur est frustré, préoccupé ou insatisfait du traitement. Veuillez offrir soutien et compréhension, et suggérer à l'utilisateur de revoir le plan de traitement ou de demander un deuxième avis."
                else: # non / NA_CATEGORY
                    return "L'utilisateur recherche des informations sur le traitement. Veuillez fournir des informations générales sur le traitement et souligner l'importance de suivre les conseils médicaux."
            elif medical_object == "diagnostique":
                if emotion == "positif":
                    return "L'utilisateur a une attitude positive envers le diagnostic, il cherche peut-être une confirmation ou des informations supplémentaires. Veuillez fournir des informations générales sur le diagnostic et conseiller à l'utilisateur de discuter des prochaines étapes avec son médecin."
                elif emotion == "negatif":
                    return "L'utilisateur est confus, préoccupé ou frustré par le diagnostic. Veuillez offrir réconfort et soutien, et suggérer à l'utilisateur de demander des éclaircissements supplémentaires ou un deuxième avis."
                else: # non / NA_CATEGORY
                    return "L'utilisateur recherche des informations sur le diagnostic. Veuillez fournir des informations générales sur le diagnostic et conseiller à l'utilisateur de discuter des prochaines étapes avec son médecin."
            else: # medical_object == "NA_CATEGORY"
                return "L'utilisateur recherche des informations, mais l'objet médical n'est pas clair. Veuillez fournir des informations générales sur la santé ou suggérer à l'utilisateur de poser une question plus spécifique."
        
        # Intention: partage_experience (Experience sharing)
        elif intention == "partage_experience":
            if medical_object == "symptome":
                if emotion == "positif":
                    return "L'utilisateur partage positivement son expérience des symptômes. Veuillez encourager l'utilisateur à partager plus de détails, tels que le début des symptômes, leur durée et les mesures prises. Vous pouvez également leur demander s'ils ont des stratégies d'adaptation positives à partager avec d'autres membres de la communauté."
                elif emotion == "negatif":
                    return "L'utilisateur partage négativement son expérience des symptômes. Veuillez exprimer votre sympathie et votre compréhension, et encourager l'utilisateur à décrire en détail ses sentiments et les défis rencontrés. Vous pouvez leur demander quel type de soutien ils recherchent actuellement et leur rappeler que les membres de la communauté sont là pour écouter et soutenir."
                else: # non / NA_CATEGORY
                    return "L'utilisateur partage son expérience des symptômes. Veuillez encourager l'utilisateur à partager plus de détails et à offrir un soutien."
            elif medical_object == "traitement":
                if emotion == "positif":
                    return "L'utilisateur partage positivement son expérience du traitement. Veuillez encourager l'utilisateur à partager les points saillants du processus de traitement, les stratégies efficaces ou les ressources qu'il a trouvées utiles. Vous pouvez leur demander s'ils ont des conseils à donner aux autres membres qui suivent un traitement similaire."
                elif emotion == "negatif":
                    return "L'utilisateur partage négativement son expérience du traitement. Veuillez exprimer votre sympathie et votre compréhension, et encourager l'utilisateur à partager les difficultés, les effets secondaires ou les revers rencontrés pendant le traitement. Vous pouvez leur demander quel type de soutien ou de conseils ils souhaitent obtenir de la communauté et leur rappeler l'importance de demander une aide professionnelle."
                else: # non / NA_CATEGORY
                    return "L'utilisateur partage son expérience du traitement. Veuillez encourager l'utilisateur à partager plus de détails et à offrir un soutien."
            elif medical_object == "diagnostique":
                if emotion == "positif":
                    return "L'utilisateur partage positivement son expérience du diagnostic. Veuillez encourager l'utilisateur à partager les informations clés du processus de diagnostic, comment il a accepté le diagnostic et les mesures positives qu'il a prises. Vous pouvez leur demander s'ils ont des ressources ou des conseils à partager avec les membres nouvellement diagnostiqués."
                elif emotion == "negatif":
                    return "L'utilisateur partage négativement son expérience du diagnostic. Veuillez exprimer votre sympathie et votre compréhension, et encourager l'utilisateur à partager l'impact émotionnel, la confusion ou les défis du diagnostic. Vous pouvez leur demander quel type de soutien ils ont le plus besoin actuellement et leur rappeler l'importance de demander un soutien en santé mentale."
                else: # non / NA_CATEGORY
                    return "L'utilisateur partage son expérience du diagnostic. Veuillez encourager l'utilisateur à partager plus de détails et à offrir un soutien."
            else: # medical_object == "NA_CATEGORY"
                return "L'utilisateur partage son expérience, mais l'objet médical n'est pas clair. Veuillez encourager l'utilisateur à partager plus de détails et à offrir un soutien général."

        # Intention: fonction_phatique (Greetings or maintaining communication)
        elif intention == "fonction_phatique":
            return "Veuillez donner une réponse amicale et encourager l'utilisateur à continuer à participer aux discussions de la communauté."
        
        # Unknown intention
        else:
            return "Intention non identifiée, veuillez fournir une réponse générale et polie, et guider l'utilisateur à fournir des informations plus claires."

    response_strategy = get_response_strategy(intention, medical_object, emotion)

    response_prompt = f"""
    L'utilisateur a posté le contenu suivant sur le forum médical : "{user_input}"

    Les résultats de la classification de ce contenu sont les suivants :
    - Niveau d'intention : {intention}
    - Niveau d'objet médical : {medical_object}
    - Niveau émotionnel : {emotion}

    Veuillez fournir une réponse raisonnable et utile en tant qu'assistant professionnel du forum médical, basée sur ces résultats de classification.
    {response_strategy}
    Veuillez vous assurer que la réponse est en français.
    """

    print("\n--- Génération de la réponse en cours ---")
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
            print("\n--- Réponse de l'assistant ---")
            print(generated_response)
            break
        except Exception as e:
            if "429" in str(e):
                retries += 1
                wait_time = base_delay * (2 ** (retries - 1)) + random.uniform(0, 1)
                print(f"Erreur de quota (429) rencontrée lors de la génération de la réponse. Tentative {retries}/{max_retries}, attente de {wait_time:.2f} secondes...")
                time.sleep(wait_time)
            else:
                print(f"Échec de la génération de la réponse : {e}")
                print(f"Sortie brute du modèle :\n{response.text if 'response' in locals() else 'Aucune réponse'}")
                generated_response = "Désolé, impossible de générer une réponse. Veuillez réessayer plus tard."
                break
    
    if generated_response is None:
        print("Désolé, impossible de générer une réponse. Veuillez réessayer plus tard.")