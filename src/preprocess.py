# src/preprocess.py

from sklearn.feature_extraction.text import TfidfVectorizer

def vetorizar_textos(textos, max_features=5000):
    """
    Converte a lista de textos em matriz TF-IDF.
    """
    vectorizer = TfidfVectorizer(stop_words="english", max_df=0.5, max_features=max_features)
    X = vectorizer.fit_transform(textos)
    return X, vectorizer
