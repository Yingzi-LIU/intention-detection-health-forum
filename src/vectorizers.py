import numpy as np
from gensim.models import Word2Vec, FastText, KeyedVectors
import os
import warnings

# Suppress DeprecationWarning from Gensim regarding old vector loading
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Path for a pre-trained GloVe model.
GLOVE_MODEL_PATH = 'wiki_giga_2024_300_MFT20_vectors_seed_2024_alpha_0.75_eta_0.05_combined.txt'

class Word2VecVectorizer:
    def __init__(self, size=100, window=5, min_count=1, workers=4):
        self.size = size
        self.window = window
        self.min_count = min_count
        self.workers = workers
        self.model = None

    def fit(self, X):
        """Trains the Word2Vec model on the provided text data."""
        tokenized_sentences = [str(doc).split() for doc in X]
        print("    -> Training Word2Vec...")
        self.model = Word2Vec(
            sentences=tokenized_sentences,
            vector_size=self.size,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers
        )
        print("    ✅ Word2Vec trained.")
        return self

    def transform(self, X):
        """Transforms text data into a document vector by averaging word vectors."""
        if self.model is None:
            raise RuntimeError("Model has not been fitted yet.")
        
        tokenized_sentences = [str(doc).split() for doc in X]
        
        filtered_vectors = [[self.model.wv[word] for word in sentence if word in self.model.wv] for sentence in tokenized_sentences]
        
        doc_vectors = []
        for doc_vecs in filtered_vectors:
            if len(doc_vecs) > 0:
                doc_vectors.append(np.mean(doc_vecs, axis=0))
            else:
                doc_vectors.append(np.zeros(self.size))
        
        return np.array(doc_vectors)

    def fit_transform(self, X, y=None):
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
        print("    -> Training FastText...")
        self.model = FastText(
            sentences=tokenized_sentences,
            vector_size=self.size,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers
        )
        print("    ✅ FastText trained.")
        return self

    def transform(self, X):
        """Transforms text data into a document vector by averaging word vectors."""
        if self.model is None:
            raise RuntimeError("Model has not been fitted yet.")

        tokenized_sentences = [str(doc).split() for doc in X]
        
        doc_vectors = []
        for sentence in tokenized_sentences:
            if len(sentence) > 0:
                sentence_vectors = [self.model.wv[word] for word in sentence]
                doc_vectors.append(np.mean(sentence_vectors, axis=0))
            else:
                doc_vectors.append(np.zeros(self.size))
        
        return np.array(doc_vectors)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)


class GloveVectorizer:
    def __init__(self, glove_path=GLOVE_MODEL_PATH):
        self.glove_path = glove_path
        self.model = None
        self.vector_size = 0

    def fit(self, X, y=None):
        """Loads the pre-trained GloVe vectors."""
        print("    -> Loading pre-trained GloVe model...")
        try:
            self.model = KeyedVectors.load_word2vec_format(self.glove_path, binary=False, no_header=True)
            self.vector_size = self.model.vector_size
            print("    ✅ GloVe model loaded.")
        except FileNotFoundError:
            print(f"❌ Error: GloVe model file not found at '{self.glove_path}'.")
            self.model = None
            self.vector_size = 0
        except Exception as e:
            print(f"❌ Error loading GloVe model: {e}")
            self.model = None
            self.vector_size = 0
        return self

    def transform(self, X):
        """Transforms text data into a document vector by averaging word vectors."""
        if self.model is None or self.vector_size == 0:
            print("⚠️ GloVe model not loaded. Returning zeros.")
            return np.zeros((len(X), 1))
        
        tokenized_sentences = [str(doc).split() for doc in X]
        
        doc_vectors = []
        for sentence in tokenized_sentences:
            word_vectors = [self.model[word] for word in sentence if word in self.model]
            
            if len(word_vectors) > 0:
                doc_vectors.append(np.mean(word_vectors, axis=0))
            else:
                doc_vectors.append(np.zeros(self.vector_size))
        
        return np.array(doc_vectors)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)
