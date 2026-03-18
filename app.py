from flask import Flask, render_template, request
from model import train_model

app = Flask(__name__)

model, vectorizer, accuracy = train_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        email = request.form['email']
        email_vector = vectorizer.transform([email])
        result = model.predict(email_vector)[0]

        prediction = "Phishing ⚠️" if result == 1 else "Safe ✅"

    return render_template(
        'index.html',
        prediction=prediction,
        accuracy=round(accuracy * 100, 2)
    )

if __name__ == '__main__':
    app.run(debug=True)
