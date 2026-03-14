from model import train_model
import re
from flask import Flask, request, render_template

app = Flask(__name__)

model, vectorizer = train_model()


@app.route("/", methods=["GET","POST"])
def home():

    prediction = ""
    warning = ""
    probability = ""

    if request.method == "POST":

        email = request.form["email"]

        links = re.findall(r'https?://\S+', email)

        if links:
            warning = "⚠ Suspicious link detected"

        email_vector = vectorizer.transform([email])

        result = model.predict(email_vector)

        prob = model.predict_proba(email_vector)

        phishing_prob = round(prob[0][1] * 100,2)

        probability = f"Probability: {phishing_prob}%"

       
        if result[0] == 1 or links:
           prediction = "Phishing Email"
        else:
           prediction = "Safe Email"


    return render_template(
        "index.html",
        prediction=prediction,
        warning=warning,
        probability=probability
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
