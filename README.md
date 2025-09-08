# Détection des intentions dans les postes des utilisateurs sur le forum de santé Doctissimo

Ce projet de recherche porte sur l’analyse des intentions exprimées dans les postes publiés par les utilisateurs du forum de santé **Doctissimo**. L’objectif est de classer automatiquement des phrases extraites de ces postes selon trois niveaux d’annotation complémentaires : l’intention générale du locuteur, l’objet médical évoqué et le sentiment exprimé. Pour ce faire, le projet s’appuie sur une combinaison de méthodes traditionnelles de traitement automatique des langues (TAL) (vectorisation BoW/TF-IDF, embeddings Word2Vec et FastText, caractéristiques basées sur les mots-clés), de modèles récents de type Transformer (BERT, CamemBERT, CamemBERT-bio) entraînés et **fine-tunés** dans un cadre **multi-tâches**, ainsi que sur l’exploration de **Grands Modèles de Langage (LLM)** (Google Gemini, OpenAI GPT) via des approches de *few-shot prompting*. L’ensemble de ces approches vise à mieux comprendre les besoins, les expériences et les émotions des utilisateurs, tout en évaluant les apports respectifs des techniques classiques, des modèles spécialisés et des LLM de pointe pour l’analyse de données issues de forums médicaux en ligne.


## Données et Annotation

Le jeu de données se compose de 972 phrases en français, extraites individuellement des paragraphes des postes du forum de santé Doctissimo. Les catégories d’annotation utilisées dans ce projet — couvrant l’intention générale, l’objet médical et le sentiment — ainsi que le travail concret d’annotation ont été proposés et réalisés par les étudiantes du Master en TAL, Lise Brisset, Patricia Augustyn et Solomiia Korol, dans le cadre du cours *Enrichissement de corpus* dirigé par Mme Eshkol-Taravella en 2024. Leur contribution a permis de définir les conventions d’annotation et de constituer le jeu de données sur lequel repose ce travail.

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

Le projet adopte une approche complète et comparative, articulée autour de trois axes principaux. Dans un premier temps, des méthodes classiques de traitement automatique des langues (TAL) sont mobilisées, combinant différentes stratégies de **représentation linguistique** — telles que la vectorisation (BoW, TF-IDF), les embeddings de type Word2Vec, FastText et Glove, ainsi que des caractéristiques basées sur des mots-clés — avec l’application de modèles d’**apprentissage automatique supervisé** (régression logistique, SVM, Naïve Bayes, arbres de décision, k-plus proches voisins), dont les hyperparamètres sont optimisés par recherche systématique (Grid Search). Dans un second temps, des modèles modernes fondés sur les architectures **Transformer (BERT, CamemBERT, CamemBERT-bio)** sont entraînés et fine-tunés dans un cadre **multi-tâches**, permettant de capturer plus finement le contexte linguistique et de traiter simultanément les trois dimensions d’annotation

L’entraînement de ces modèles intègre plusieurs stratégies avancées :  

* **Fonction de perte adaptée** : entropie croisée multi-tâches.  
* **Optimiseur et Scheduler** : gestion du taux d’apprentissage (learning rate).  
* **Échantillonnage pondéré aléatoire** (`WeightedRandomSampler`) : pour contrer le déséquilibre des classes.  
* **Augmentation des données**, incluant :  
  * **Sur-échantillonnage** des classes minoritaires.  
  * **Rétro-traduction** (français → anglais → français).  
  * **Augmentation par mots-clés**.  
  * **Stratégies combinées** intégrant plusieurs méthodes d’augmentation.

Enfin, l’étude examine l’apport des **Grands Modèles de Langage (LLM)**, tels que Gemini et GPT, exploités au moyen de techniques de **few-shot prompting** afin d’évaluer leur capacité à réaliser les classifications sans entraînement spécifique, tout en produisant des réponses interactives adaptées au contenu analysé.  

Cette méthodologie permet de confronter des approches fondées sur des représentations explicites et l’apprentissage automatique supervisé, des modèles entraînés en profondeur et des modèles pré-entraînés de grande échelle, 
afin d’évaluer de manière systématique leurs forces et limites respectives dans l’analyse des intentions générales, objets médicaux et sentiments des utilisateurs du forum de santé **Doctissimo**.


### 1. Préparation et Division des Données

*   **Chargement des données** : Les données brutes sont chargées à partir du fichier `data/projet_annotation_sante_final_M1.csv` en utilisant la fonction `load_data` (`src/preprocessing.py`).
*   **Gestion des valeurs manquantes** : Les valeurs `NaN` sont remplacées par `'NA_CATEGORY'`.
*   **Fusion des classes rares** : Avant la division, les classes d'étiquettes avec moins de 2 échantillons sont fusionnées en `'RARE_CLASS'` pour garantir la robustesse de l'échantillonnage stratifié, géré par la fonction `merge_rare_classes` (`src/split_dataset.py`).
*   **Nettoyage du texte** : Le texte est nettoyé à l'aide des fonctions `clean_text` et `preprocess_dataset` (`src/preprocessing.py`), incluant :
    *   Conversion en minuscules.
    *   Remplacement des émoticônes et emojis par des tokens spécifiques (ex: `EMOJI_SMILE`).
    *   Suppression des balises HTML, URLs, hashtags et mentions.
    *   Suppression de la ponctuation et des caractères spéciaux.
    *   Remplacement des nombres par `NUM`.
    *   Lemmatisation des mots français.
    *   Suppression optionnelle des mots vides (stop words) français.
*   **Division du jeu de données** : Le jeu de données est divisé en trois ensembles : 572 phrases pour l'entraînement, 100 phrases pour la validation et 300 phrases pour le test. L'ensemble d'entraînement est composé d'un sous-ensemble fixe (basé sur des IDs spécifiques) et d'une partie échantillonnée aléatoirement, en utilisant un échantillonnage stratifié pour maintenir la distribution des étiquettes. Les fonctions `print_distribution`, `save_distribution` et `plot_distribution_grouped` (`src/split_dataset.py`) sont utilisées pour analyser et visualiser la distribution des données.
*   **Encodage des étiquettes** : Les étiquettes textuelles sont converties en IDs numériques à l'aide de `LabelEncoder` via la fonction `encode_labels` (`src/preprocessing.py`). Les données nettoyées sont sauvegardées avec `save_cleaned_data` (`src/preprocessing.py`).

### 2. Ingénierie des Caractéristiques et Vectorisation

*   **Vectorisation traditionnelle** :
    *   Bag-of-Words (BoW) via `CountVectorizer`.
    *   TF-IDF (Term Frequency-Inverse Document Frequency) via `TfidfVectorizer`, incluant des unigrammes et des bigrammes (`ngram_range=(1, 2)`).
*   **Word Embeddings** :
    *   Word2Vec (`Word2VecVectorizer`).
    *   FastText (`FastTextVectorizer`).
    *   GloVe (`GloveVectorizer`).
*   **Caractéristiques basées sur les mots-clés** : Des caractéristiques booléennes sont ajoutées, indiquant la présence de mots-clés spécifiques (définis sur la base de notre expertise et de notre compréhension des catégories d’annotation) pour chaque tâche et étiquette. Ces caractéristiques sont ajoutées via la fonction `add_keyword_features` (`src/preprocessing.py`). Ces caractéristiques peuvent ensuite être combinées avec des méthodes de vectorisation traditionnelles ou des embeddings pour enrichir l’entrée des modèles d’apprentissage automatique ou des Transformers.

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

*   **Architecture du modèle** : Un encodeur partagé (BERT ou CamemBERT) est utilisé, suivi de trois têtes de classification indépendantes, une pour chaque tâche (intention, objet médical, sentiment). Les classes `DatasetMultiTache` et `MultiTaskModel` (définies dans `src/evaluate_all_bert_camenbert_models.py`) sont utilisées pour la gestion des données et la construction du modèle multi-tâches. La fonction `evaluer_modele` est responsable de l'évaluation des performances du modèle.
*   **Modèles pré-entraînés** :
    *   **BERT** : `bert-base-multilingual-cased` est utilisé pour sa capacité à gérer plusieurs langues, y compris le français.
    *   **CamemBERT** : `camembert-base` (un modèle RoBERTa entraîné sur un grand corpus français) et `almanach/camembert-bio-base` (un CamemBERT spécialisé dans le domaine biomédical français) sont explorés pour leurs performances potentiellement supérieures sur des textes français. Les scripts `Camembert_bio_MultiTask_Medical.py` et `CamenBERT_Baseline.py` (`src/CamenBERT/`) sont utilisés pour l'entraînement de base et l'évaluation des modèles CamemBERT. Les scripts `Camembert_bio_MultiTask_Medical_Sampler.py` et `Camembert_MultiTask_Medical_Sampler.py` (`src/CamenBERT/`) implémentent des stratégies d'échantillonnage pondéré pour les modèles CamemBERT.
*   **Stratégies d'entraînement** :
    *   **Fonction de perte** : La perte d'entropie croisée est utilisée pour chaque tâche, et les pertes sont sommées pour l'optimisation multi-tâches.
    *   **Optimiseur et Scheduler** : L'optimiseur AdamW est employé avec un scheduler de taux d'apprentissage linéaire (`get_linear_schedule_with_warmup`).
    *   **Échantillonnage pondéré aléatoire (`WeightedRandomSampler`)** : Pour contrer le déséquilibre des classes, un échantillonnage pondéré est appliqué aux données d'entraînement, ciblant spécifiquement les tâches d'intention, d'objet médical ou de sentiment selon les expériences. Les scripts `BERT_MTL_WeightedSampler_Intention.py`, `BERT_MTL_WeightedSampler_ObjetMedical.py` et `BERT_MTL_WeightedSampler_sentiment.py` (`src/BERT_MTL/`) implémentent cette stratégie pour les tâches respectives.
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
    *   Les modèles LLM sont utilisés avec une approche de *few-shot prompting*. Cela implique de fournir au modèle quelques exemples annotés (`data/few_shot_examples.csv`) directement dans le prompt, afin de guider le modèle vers le format de sortie et les catégories souhaitées. Les fonctions `create_few_shot_prompt` et `evaluate_category` (`src/LLM/gemini.py` et `src/LLM/openai_model.py`) sont utilisées pour cette approche.
    *   Le prompt est structuré pour demander une classification en format JSON pour les trois niveaux d'annotation (intention générale, objet médical, sentiment).
*   **Processus de classification** :
    *   Chargement des exemples *few-shot* et du jeu de données de test.
    *   Construction dynamique du prompt pour chaque phrase à classer, incluant les instructions et les exemples.
    *   Appel à l'API du LLM (Gemini ou OpenAI) pour obtenir les prédictions.
    *   Gestion des erreurs et des limites de taux (*rate limits*) avec des mécanismes de réessai.
*   **Génération de réponses interactives (pour Gemini)** :
    *   Un module interactif (`src/LLM/interactive_gemini.py`) permet de tester le classifieur LLM en temps réel, utilisant les fonctions `create_few_shot_prompt` et `get_response_strategy`.
    *   Après classification, une stratégie de réponse personnalisée est générée en français, basée sur l'intention, l'objet médical et le sentiment détectés dans la phrase de l'utilisateur. Cela simule un assistant de forum médical capable de fournir des conseils ou un soutien adaptés.

### 6. Évaluation

Les performances des modèles sont évaluées à l'aide de plusieurs métriques, notamment :

*   Précision (Accuracy)
*   F1-score (Macro et Micro)
*   Précision (Macro)
*   Rappel (Macro)
*   F1-score par classe

Des scripts sont mis en place pour automatiser l'entraînement, l'évaluation et la comparaison des différents modèles et stratégies d'augmentation, générant des rapports de performance détaillés. Le script `compare_all_models.py` (`src/BERT_MTL/`) est utilisé pour comparer les performances de tous les modèles entraînés.

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

## Analyse des flux d'intention et des caractéristiques des publications

Le répertoire `src/Sequential_Pattern_Mining/` contient des scripts pour l'analyse des flux d'intention et des caractéristiques des publications :

*   **`reconstruct_posts.py`** : Reconstruit les publications à partir des phrases annotées, en regroupant les phrases par ID de publication, en utilisant les fonctions `reconstruct_from_ids`, `save_reconstructed_data` et `check_missing_ids`. Le résultat est sauvegardé dans `data/reconstructed_posts_final.json`.
*   **`intention_flow_analysis.py`** : Analyse les séquences d'intentions (niveau1, niveau2, niveau3) au sein des publications, en utilisant les fonctions `analyze_intention_flow`, `filter_repetitive_patterns`, `visualize_patterns` et `write_patterns_to_markdown`. Il identifie les modèles de flux d'intention fréquents (par exemple, des flux à 2 ou 5 étapes), filtre les modèles répétitifs et génère des visualisations graphiques (`intention_flow_patterns_X-step.png`) ainsi que des tableaux Markdown (`intention_flow_schema.md`).
*   **`intent_graph_visualization.py`** : Construit et affiche un tableau des transitions d'intention fréquentes entre les phrases, en utilisant les fonctions `build_intent_transitions` et `print_and_save_transition_table`. Le tableau est sauvegardé dans `intention_flow_schema/intent_flow_table.txt`.
*   **`post_length_analysis.py`** : Analyse la distribution de la longueur des publications (nombre de phrases par publication), en utilisant les fonctions `analyze_post_length` et `visualize_post_lengths`, et génère un histogramme (`post_length_distribution.png`).
*   **`qualitative_analysis.py`** : Permet de rechercher des publications spécifiques contenant des modèles de transition d'intention définis, en utilisant la fonction `find_posts_by_pattern`, facilitant l'analyse qualitative.