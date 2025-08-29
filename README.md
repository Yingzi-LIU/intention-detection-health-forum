# Analyse de l'Intention des Messages sur le Forum de Santé Doctissimo

Ce projet de recherche porte sur l’analyse des intentions exprimées dans les messages publiés par les utilisateurs du forum de santé **Doctissimo**. L’objectif est de classer automatiquement des phrases extraites de ces posts selon trois niveaux d’annotation complémentaires : l’intention générale du locuteur, l’objet médical évoqué et le sentiment exprimé. Pour ce faire, le projet s’appuie à la fois sur des méthodes traditionnelles de TAL (vectorisation BoW/TF-IDF, embeddings Word2Vec et FastText, caractéristiques basées sur les mots-clés) et sur des modèles récents de type Transformer (BERT, CamemBERT, CamemBERT-bio), entraînés et **fine-tunés** dans un cadre multi-tâches. L’ensemble de ces approches vise à mieux comprendre les besoins, les expériences et les émotions des utilisateurs, tout en évaluant les apports respectifs des techniques classiques et des modèles de pointe pour l’analyse de données issues de forums médicaux en ligne.


## Données et Annotation

Le jeu de données se compose de 972 phrases en français, extraites individuellement des paragraphes des posts du forum. Chaque phrase est annotée selon trois catégories principales :

1.  **Niveau d'Intention Générale (`niveau1`)** : Ce niveau se rapproche des actes de langage et de l'intention communicative du locuteur. Les étiquettes incluent :
    *   `recherche_information` (Recherche d'information)
    *   `partage_experience` (Partage d'expérience)
    *   `fonction_phatique` (Fonction phatique / Salutations)

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

Le projet adopte une approche complète, combinant des techniques de traitement du langage naturel (TAL) traditionnelles et des modèles d'apprentissage profond basés sur les Transformers.

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

### 5. Évaluation

Les performances des modèles sont évaluées à l'aide de plusieurs métriques, notamment :

*   Précision (Accuracy)
*   F1-score (Macro et Micro)
*   Précision (Macro)
*   Rappel (Macro)
*   F1-score par classe

Des scripts sont mis en place pour automatiser l'entraînement, l'évaluation et la comparaison des différents modèles et stratégies d'augmentation, générant des rapports de performance détaillés.