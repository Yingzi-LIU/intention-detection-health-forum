# Détection des intentions dans les postes des utilisateurs sur le forum de santé Doctissimo

Ce projet de recherche porte sur l’analyse des intentions exprimées dans les postes publiés par les utilisateurs du forum de santé **Doctissimo**. L’objectif est de classer automatiquement des phrases extraites de ces postes selon trois niveaux d’annotation complémentaires : l’intention générale du locuteur, l’objet médical évoqué et le sentiment exprimé. Pour ce faire, le projet s’appuie sur une combinaison de méthodes traditionnelles de traitement automatique des langues (TAL) (vectorisation BoW/TF-IDF, embeddings Word2Vec et FastText, caractéristiques basées sur les mots-clés), de modèles récents de type Transformer (BERT, CamemBERT, CamemBERT-bio) entraînés et **fine-tunés** dans un cadre multi-tâches, ainsi que sur l’exploration de **Grands Modèles de Langage (LLM)** (Google Gemini, OpenAI GPT) via des approches de *few-shot prompting*. L’ensemble de ces approches vise à mieux comprendre les besoins, les expériences et les émotions des utilisateurs, tout en évaluant les apports respectifs des techniques classiques, des modèles spécialisés et des LLM de pointe pour l’analyse de données issues de forums médicaux en ligne.


## Données et Annotation

Le jeu de données se compose de 972 phrases en français, extraites individuellement des paragraphes des postes du forum de santé Doctissimo. Les catégories d’annotation utilisées dans ce projet — couvrant l’intention générale, l’objet médical et le sentiment — ont été proposées par les étudiantes du Master en TAL, Lise Brisset, Patricia Augustyn et Solomiia Korol, dans le cadre du cours *Enrichissement de corpus* dirigé par Mme Eshkol-Taravella l’année 2024. Leur contribution a permis de définir les conventions d’annotation sur lesquelles repose ce travail.

Ces catégories se déclinent en trois niveaux d’annotation complémentaires, détaillés ci-dessous :

1.  **Niveau d'Intention Générale (`niveau1`)** : Ce niveau se rapproche des actes de paroles en linguistique et des intentions des locuteurs. Les étiquettes incluent :
    *   `recherche_information` (Recherche d'information)
    *   `partage_experience` (Partage d'expérience)
    *   `fonction_phatique` (Fonction phatique)

2.  **Niveau d'Objet Médical (`niveau2`)** : Ce niveau identifie les concepts médicaux abordés dans la phrase. Les étiquettes incluent :
    *   `symptome` (Symptôme)
    *   `traitement` (Traitement)
    *   `diagnostique` (Diagnostic)
    *   `NA_CATEGORY` (Catégorie non applicable, pour les phrases sans objet médical clair)

3.  **Niveau d'Analyse Sentimentale (`niveau3`)** : Ce niveau évalue le sentiment exprimé dans la phrase. Les étiquettes incluent :
    *   `positif` (Positif)
    *   `negatif` (Négatif)
    *   `non` (Neutre)

## Méthodologie

Le projet adopte une approche complète et comparative, articulée autour de trois axes principaux.  
D’abord, des techniques classiques de traitement automatique des langues (TAL) sont mobilisées, incluant la vectorisation (BoW, TF-IDF), les embeddings de type Word2Vec et FastText, ainsi que des caractéristiques basées sur des mots-clés. Ensuite, des modèles modernes de type Transformer (BERT, CamemBERT, CamemBERT-bio) sont entraînés et fine-tunés dans un cadre multi-tâches pour capturer plus finement le contexte linguistique. Enfin, le projet explore l’apport des Grands Modèles de Langage (LLM) comme Gemini et GPT, utilisés via des techniques de *few-shot prompting*, afin d’évaluer leur capacité à classifier les intentions, objets médicaux et sentiments sans entraînement spécifique, tout en générant des réponses interactives.  

Cette méthodologie permet de confronter des approches fondées sur des représentations explicites, des modèles entraînés en profondeur et des modèles pré-entraînés de grande échelle, afin de mesurer leurs forces et limites respectives.


### 1. Préparation et Division des Données

*   **Chargement des données** : Les données brutes sont chargées à partir du fichier `data/projet_annotation_sante_final_M1.csv`.
*   **Gestion des valeurs manquantes** : Les valeurs `NaN` sont remplacées par `'NA_CATEGORY'`.
*   **Fusion des classes rares** : Avant la division, les classes d'étiquettes avec moins de 2 échantillons sont fusionnées en `'RARE_CLASS'` pour garantir la robustesse de l'échantillonnage stratifié.
*   **Nettoyage du texte** :
    *   Conversion en minuscules.
    *   Remplacement des émoticônes et emojis par des tokens spécifiques (ex: `EMOJI_SMILE`).
    *   Suppression des balises HTML, URLs, hashtags et mentions.
    *   Suppression de la ponctuation et des caractères spéciaux.
    *   Remplacement des nombres par `NUM`.
    *   Lemmatisation des mots français.
    *   Suppression optionnelle des mots vides (stop words) français.
*   **Division du jeu de données** : Le jeu de données est divisé en ensembles d'entraînement, de validation et de test. L'ensemble d'entraînement est composé d'un sous-ensemble fixe (basé sur des IDs spécifiques) et d'une partie échantillonnée aléatoirement, en utilisant un échantillonnage stratifié pour maintenir la distribution des étiquettes.
*   **Encodage des étiquettes** : Les étiquettes textuelles sont converties en IDs numériques à l'aide de `LabelEncoder`.

### 2. Ingénierie des Caractéristiques et Vectorisation

*   **Vectorisation traditionnelle** :
    *   Bag-of-Words (BoW) via `CountVectorizer`.
    *   TF-IDF (Term Frequency-Inverse Document Frequency) via `TfidfVectorizer`, incluant des unigrammes et des bigrammes (`ngram_range=(1, 2)`).
*   **Word Embeddings** :
    *   Word2Vec (`Word2VecVectorizer`).
    *   FastText (`FastTextVectorizer`).
*   **Vectorisation BERT** : Utilisation de modèles BERT pré-entraînés (`BertVectorizer`) pour générer des embeddings de phrases.
*   **Caractéristiques basées sur les mots-clés** : Des caractéristiques booléennes sont ajoutées, indiquant la présence de mots-clés spécifiques (définis dans un dictionnaire) pour chaque tâche et étiquette. Ces caractéristiques peuvent être combinées avec des méthodes de vectorisation traditionnelles ou des embeddings pour des modèles "améliorés".

### 3. Modèles d'Apprentissage Automatique (Baseline et Améliorés)

Des expériences initiales sont menées en utilisant des caractéristiques traditionnelles et des embeddings de mots avec une variété de classifieurs :

*   Régression Logistique (`LogisticRegression`)
*   Machines à Vecteurs de Support (SVM) (`SVC`)
*   Naïve Bayes Multinomial (`MultinomialNB`)
*   Arbres de Décision (`DecisionTreeClassifier`)
*   K-plus proches voisins (KNN) (`KNeighborsClassifier`)

L'optimisation des hyperparamètres est effectuée à l'aide de `GridSearchCV`, avec le score F1-pondéré comme métrique d'évaluation principale. Des expériences "améliorées" intègrent les caractéristiques de mots-clés.

### 4. Modèles d'Apprentissage Multi-Tâches basés sur les Transformers

Le cœur du projet réside dans l'application de modèles d'apprentissage multi-tâches (MTL) basés sur les architectures Transformer.

*   **Architecture du modèle** : Un encodeur partagé (BERT ou CamemBERT) est utilisé, suivi de trois têtes de classification indépendantes, une pour chaque tâche (intention, objet médical, sentiment).
*   **Modèles pré-entraînés** :
    *   **BERT** : `bert-base-multilingual-cased` est utilisé pour sa capacité à gérer plusieurs langues, y compris le français.
    *   **CamemBERT** : `camembert-base` (un modèle RoBERTa entraîné sur un grand corpus français) et `almanach/camembert-bio-base` (un CamemBERT spécialisé dans le domaine biomédical français) sont explorés pour leurs performances potentiellement supérieures sur des textes français.
*   **Stratégies d'entraînement** :
    *   **Fonction de perte** : La perte d'entropie croisée est utilisée pour chaque tâche, et les pertes sont sommées pour l'optimisation multi-tâches.
    *   **Optimiseur et Scheduler** : L'optimiseur AdamW est employé avec un scheduler de taux d'apprentissage linéaire (`get_linear_schedule_with_warmup`).
    *   **Échantillonnage pondéré aléatoire (`WeightedRandomSampler`)** : Pour contrer le déséquilibre des classes, un échantillonnage pondéré est appliqué aux données d'entraînement, ciblant spécifiquement les tâches d'intention, d'objet médical ou de sentiment selon les expériences.
*   **Augmentation des données (pour les modèles MTL)** :
    *   **Sur-échantillonnage** : Duplication des échantillons des classes minoritaires.
    *   **Rétro-traduction** : Traduction de phrases du français vers l'anglais, puis de l'anglais vers le français pour générer des paraphrases.
    *   **Augmentation par mots-clés** : Ajout de mots-clés pertinents aux phrases.
    *   **Augmentation combinée** : Intégration de plusieurs méthodes d'augmentation.

### 5. Utilisation des Grands Modèles de Langage (LLM)

Le projet explore également l'utilisation de **Grands Modèles de Langage (LLM)** pour la classification des intentions, des objets médicaux et des sentiments, en tirant parti de leurs capacités de raisonnement contextuel et de compréhension du langage naturel.

*   **Modèles utilisés** :
    *   **Google Gemini** : Via l'API Gemini (modèle `gemini-2.0-flash-001` ou `gemini-2.5-flash`).
    *   **OpenAI GPT** : Via l'API OpenAI (modèles comme `gpt-4o`).
*   **Approche Few-Shot Prompting** :
    *   Les modèles LLM sont utilisés avec une approche de *few-shot prompting*. Cela implique de fournir au modèle quelques exemples annotés (`data/few_shot_examples.csv`) directement dans le prompt, afin de guider le modèle vers le format de sortie et les catégories souhaitées.
    *   Le prompt est structuré pour demander une classification en format JSON pour les trois niveaux d'annotation (intention générale, objet médical, sentiment).
*   **Processus de classification** :
    *   Chargement des exemples *few-shot* et du jeu de données de test.
    *   Construction dynamique du prompt pour chaque phrase à classer, incluant les instructions et les exemples.
    *   Appel à l'API du LLM (Gemini ou OpenAI) pour obtenir les prédictions.
    *   Gestion des erreurs et des limites de taux (*rate limits*) avec des mécanismes de réessai.
*   **Génération de réponses interactives (pour Gemini)** :
    *   Un module interactif (`src/LLM/interactive_gemini.py`) permet de tester le classifieur LLM en temps réel.
    *   Après classification, une stratégie de réponse personnalisée est générée en français, basée sur l'intention, l'objet médical et le sentiment détectés dans la phrase de l'utilisateur. Cela simule un assistant de forum médical capable de fournir des conseils ou un soutien adaptés.

### 6. Évaluation

Les performances des modèles sont évaluées à l'aide de plusieurs métriques, notamment :

*   Précision (Accuracy)
*   F1-score (Macro et Micro)
*   Précision (Macro)
*   Rappel (Macro)
*   F1-score par classe

Des scripts sont mis en place pour automatiser l'entraînement, l'évaluation et la comparaison des différents modèles et stratégies d'augmentation, générant des rapports de performance détaillés.

### 7. Résultats des Modèles

Les résultats détaillés de chaque expérience (incluant les scores F1 pondérés, la précision, les meilleurs hyperparamètres et les rapports de classification) sont sauvegardés dans les répertoires suivants :

*   **`results_baseline/`** : Contient les résultats des modèles d'apprentissage automatique traditionnels.
    *   Chaque sous-répertoire (par exemple, `emotion/`, `medical_object/`, `overall_intent/`) contient :
        *   `results.json` : Fichier JSON avec les résultats bruts.
        *   `summary.md` : Résumé lisible des performances du modèle.
*   **`results_enhanced/`** : Contient les résultats des modèles améliorés avec des caractéristiques basées sur les mots-clés.
    *   Structure similaire à `results_baseline/`.
*   **`results_MTL/`** : Contient les résultats des modèles d'apprentissage multi-tâches basés sur les Transformers.
    *   `evaluation_results.json` : Fichier JSON avec les résultats d'évaluation agrégés.
    *   `evaluation_results.csv` : Fichier CSV avec les résultats d'évaluation agrégés.