import numpy as np
from gensim.models import Word2Vec, FastText
from transformers import BertModel, BertTokenizer
import torch
import os

class Word2VecVectorizer:
    def __init__(self, size=100, window=5, min_count=1, workers=4):
        self.size = size
        self.window = window
        self.min_count = min_count
        self.workers = workers
        self.model = None

    def fit(self, X):
        """Trains the Word2Vec model on the provided text data."""
        # Gensim's Word2Vec and FastText require a list of tokenized sentences.
        tokenized_sentences = [str(doc).split() for doc in X]
        print("    -> Entraînement de Word2Vec...")
        self.model = Word2Vec(
            sentences=tokenized_sentences,
            vector_size=self.size,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers
        )
        print("    ✅ Word2Vec entraîné.")
        return self

    def transform(self, X):
        """Transforms text data into a document vector by averaging word vectors."""
        if self.model is None:
            raise RuntimeError("Model has not been fitted yet.")
        
        tokenized_sentences = [str(doc).split() for doc in X]
        
        # Filter out words not in the model's vocabulary
        filtered_vectors = [[self.model.wv[word] for word in sentence if word in self.model.wv] for sentence in tokenized_sentences]
        
        # Calculate the mean vector for each document
        doc_vectors = []
        for doc_vecs in filtered_vectors:
            if len(doc_vecs) > 0:
                doc_vectors.append(np.mean(doc_vecs, axis=0))
            else:
                doc_vectors.append(np.zeros(self.size)) # Use a zero vector for empty documents
        
        return np.array(doc_vectors)

    def fit_transform(self, X, y=None):
        """Fits the model and transforms the data in a single step."""
        return self.fit(X).transform(X)


class FastTextVectorizer:
    def __init__(self, size=100, window=5, min_count=1, workers=4):
        self.size = size
        self.window = window
        self.min_count = min_count
        self.workers = workers
        self.model = None

    def fit(self, X):
        """Trains the FastText model on the provided text data."""
        tokenized_sentences = [str(doc).split() for doc in X]
        print("    -> Entraînement de FastText...")
        self.model = FastText(
            sentences=tokenized_sentences,
            vector_size=self.size,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers
        )
        print("    ✅ FastText entraîné.")
        return self

    def transform(self, X):
        """Transforms text data into a document vector by averaging word vectors."""
        if self.model is None:
            raise RuntimeError("Model has not been fitted yet.")

        tokenized_sentences = [str(doc).split() for doc in X]
        
        # FastText can handle out-of-vocabulary words, so we don't need to filter.
        doc_vectors = []
        for sentence in tokenized_sentences:
            if len(sentence) > 0:
                # Calculate the mean vector for the document
                sentence_vectors = [self.model.wv[word] for word in sentence]
                doc_vectors.append(np.mean(sentence_vectors, axis=0))
            else:
                doc_vectors.append(np.zeros(self.size))
        
        return np.array(doc_vectors)

    def fit_transform(self, X, y=None):
        """Fits the model and transforms the data in a single step."""
        return self.fit(X).transform(X)


class BertVectorizer:
    def __init__(self, model_name='bert-base-multilingual-cased', max_length=128):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.max_length = max_length

    def fit(self, X):
        return self

    def transform(self, X):
        # We process in batches to avoid out-of-memory errors
        batch_size = 32
        doc_vectors = []
        for i in range(0, len(X), batch_size):
            batch = list(X.iloc[i:i+batch_size])
            # Tokenize and encode the batch
            encoded_input = self.tokenizer(
                batch,
                padding='longest',
                truncation=True,
                max_length=self.max_length,
                return_tensors='pt'
            )
            # Disable gradient calculations for faster inference
            with torch.no_grad():
                model_output = self.model(**encoded_input)
            
            # Use the CLS token as the sentence vector
            cls_vectors = model_output.last_hidden_state[:, 0, :].numpy()
            doc_vectors.append(cls_vectors)
            
        return np.vstack(doc_vectors)
