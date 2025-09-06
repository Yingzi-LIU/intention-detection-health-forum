import pandas as pd
import re
import emoji
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
import nltk
import os

# Download NLTK resources
nltk.download('stopwords')

def load_data(base_path):
    """
    Loads the datasets.
    """
    try:
        train_df = pd.read_csv(base_path + 'train_dataset.csv')
        val_df = pd.read_csv(base_path + 'validation_dataset.csv')
        test_df = pd.read_csv(base_path + 'test_dataset.csv')
        print("✅ All datasets loaded successfully.")
        return train_df, val_df, test_df
    except FileNotFoundError:
        print(f"❌ Error: One or more dataset files not found at '{base_path}'.")
        return None, None, None

# Original French stopwords
french_stopwords = set(stopwords.words('french'))
extra_french_stopwords = {
    "le", "la", "les", "un", "une", "des", "ce", "ça", "celui", "ceux",
    "qui", "que", "quoi", "je", "tu", "il", "elle", "nous", "vous", "ils",
    "elles", "me", "te", "se", "lui", "leur", "et", "ou", "mais", "donc",
    "car", "ni", "à", "de", "en", "pour", "avec", "sans", "sur", "sous",
    "chez", "dans", "du", "au", "aux"
}
french_stopwords.update(extra_french_stopwords)
lemmatizer = WordNetLemmatizer()

# 🔹 Emoticon/emoji mapping table
emoticon_dict = {
    ":)": "EMOJI_SMILE", ":-)": "EMOJI_SMILE", ":(": "EMOJI_SAD", ":-(": "EMOJI_SAD",
    ";)": "EMOJI_WINK", ":-D": "EMOJI_LAUGH", ":D": "EMOJI_LAUGH", "<3": "EMOJI_HEART"
}

def replace_emoticons(text):
    for emot, token in emoticon_dict.items():
        text = text.replace(emot, f" {token} ")
    return text

def replace_emojis(text):
    def _replace(e, data=None):
        name = emoji.demojize(e).upper().strip(":")
        return f" EMOJI_{name} "
    return emoji.replace_emoji(text, replace=_replace)

def clean_text(text, remove_stopwords=False):
    """Main text cleaning function"""
    text = str(text).lower()
    text = replace_emoticons(text)
    text = replace_emojis(text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"http\S+|www\S+", " URL ", text)
    text = re.sub(r"#\w+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    # Remove all punctuation and special characters
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s\d]", " ", text)
    text = re.sub(r"\d+", " NUM ", text)
    text = re.sub(r"\s+", " ", text).strip()
    words = text.split()
    if remove_stopwords:
        words = [w for w in words if w not in french_stopwords]
    return " ".join(words)

def preprocess_dataset(df, text_col="Sentences", min_tokens=2, remove_stopwords=False):
    """Preprocesses the entire dataset"""
    df[text_col + "_clean"] = df[text_col].apply(lambda x: clean_text(x, remove_stopwords))
    df = df.drop_duplicates(subset=[text_col + "_clean"])
    df = df[df[text_col + "_clean"].apply(lambda x: len(x.split()) >= min_tokens)]
    return df
def encode_labels(train_df, val_df, test_df, label_col_map):
    """
    Encodes specified label columns using LabelEncoder.
    
    Args:
        train_df, val_df, test_df (pd.DataFrame): DataFrames containing label columns.
        label_col_map (dict): Dictionary where keys are task names and values are actual data column names.
    
    Returns:
        tuple: (train_df, val_df, test_df, label_encoders) Tuple containing encoded labels and encoders.
    """
    label_encoders = {}
    
    # Iterate through the values in the dictionary, which are the actual column names
    for task_name, original_col in label_col_map.items():
        # Ensure the column name exists in the DataFrame
        if original_col not in train_df.columns:
            print(f"❌ Error: Column '{original_col}' not found in the DataFrame. Skipping encoding for '{task_name}'.")
            continue

        le = LabelEncoder()
        
        # ⚠️ Critical fix: Use the original column name (original_col) to access the DataFrame
        all_labels = pd.concat([train_df[original_col], val_df[original_col], test_df[original_col]]).astype(str).unique()
        le.fit(all_labels)
        
        # Similarly, use the original column name for transformation
        train_df[original_col] = le.transform(train_df[original_col].astype(str))
        val_df[original_col] = le.transform(val_df[original_col].astype(str))
        test_df[original_col] = le.transform(test_df[original_col].astype(str))
        
        label_encoders[task_name] = le

    if not label_encoders:
        print("⚠️ No labels were encoded. Please check your label column names.")

    print("✅ Labels encoded successfully.")
    return train_df, val_df, test_df, label_encoders

def save_cleaned_data(train_df, val_df, test_df, base_path):
    """Saves the cleaned and encoded datasets"""
    try:
        os.makedirs(base_path, exist_ok=True)
        train_path = os.path.join(base_path, "train_dataset_clean.csv")
        val_path = os.path.join(base_path, "validation_dataset_clean.csv")
        test_path = os.path.join(base_path, "test_dataset_clean.csv")
        
        train_df.to_csv(train_path, index=False, encoding="utf-8")
        val_df.to_csv(val_path, index=False, encoding="utf-8")
        test_df.to_csv(test_path, index=False, encoding="utf-8")
        
        print("\n📂 Cleaned datasets saved successfully.")
    except Exception as e:
        print(f"❌ Error saving cleaned data: {e}")

### Feature Enhancement

def add_keyword_features(df, keyword_dict):
    """
    Adds new boolean features to the DataFrame based on the presence of keywords.

    Args:
        df (pd.DataFrame): The DataFrame with a 'Sentences_clean' column.
        keyword_dict (dict): A nested dictionary of keywords for each task and label.

    Returns:
        pd.DataFrame: The DataFrame with new keyword feature columns.
    """
    # Create an empty DataFrame to store the new features
    new_features = pd.DataFrame(index=df.index)

    # Flatten the keyword dictionary to iterate through all labels
    for task_name, labels_dict in keyword_dict.items():
        for label_name, keywords in labels_dict.items():
            # Create a unique column name for this keyword feature
            column_name = f'keyword_{task_name}_{label_name}'
            
            # Check if any of the keywords for the current label are in the clean sentence
            new_features[column_name] = df['Sentences_clean'].apply(
                lambda x: any(keyword in x for keyword in keywords)
            ).astype(int)

    return pd.concat([df, new_features], axis=1)