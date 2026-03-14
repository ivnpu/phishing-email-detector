import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def train_model():

    data = pd.read_csv("phishing_small.csv")

    X = data["text_combined"].astype(str)
    y = data["label"]

    vectorizer = TfidfVectorizer()
    X_vector = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vector, y)

    return model, vectorizer