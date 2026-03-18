import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model():

    data = pd.read_csv("phishing_small.csv")

    X = data["text_combined"].astype(str)
    y = data["label"]

    vectorizer = TfidfVectorizer()
    X_vector = vectorizer.fit_transform(X)

    # تقسيم البيانات (مهم للبحث)
    X_train, X_test, y_train, y_test = train_test_split(
        X_vector, y, test_size=0.2, random_state=42
    )

    # 🔹 Model 1: Naive Bayes
    nb_model = MultinomialNB()
    nb_model.fit(X_train, y_train)
    nb_pred = nb_model.predict(X_test)
    nb_acc = accuracy_score(y_test, nb_pred)

    # 🔹 Model 2: Logistic Regression
    lr_model = LogisticRegression(max_iter=500)
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    lr_acc = accuracy_score(y_test, lr_pred)

    # 🧠 اختيار الأفضل
    if lr_acc > nb_acc:
        best_model = lr_model
    else:
        best_model = nb_model

    print(f"Naive Bayes Accuracy: {nb_acc}")
    print(f"Logistic Regression Accuracy: {lr_acc}")

    return best_model, vectorizer
