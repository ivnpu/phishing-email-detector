# AI Phishing Email Detector

A web-based application that detects phishing emails using Machine Learning.

The system analyzes email content and predicts whether the message is **Safe** or **Phishing**.

## Live Demo

Try the application online:

https://phishing-email-detector-production.up.railway.app/

## Features

- Detect phishing emails using Machine Learning
- Analyze email text using TF-IDF vectorization
- Predict phishing probability
- Detect suspicious links inside emails
- Simple and user-friendly web interface

## Technologies Used

Python  
Flask  
scikit-learn  
HTML / CSS  
Git & GitHub  

## Machine Learning Model

The system uses a Machine Learning model built with:

TF-IDF Vectorizer – for converting text into numerical features  
Multinomial Naive Bayes – for classifying emails as phishing or safe  

The model was trained on a phishing email dataset and predicts the probability that an email is malicious.

## How It Works

1. The user pastes an email message in the web interface.
2. The system processes the text using TF-IDF vectorization.
3. The machine learning model analyzes the email.
4. The system predicts whether the email is **Safe** or **Phishing**.
5. If a suspicious link is detected, a warning message is displayed.

## Project Structure

phishing-email-detector
│
├── app.py
├── model.py
├── phishing_small.csv
├── requirements.txt
│
└── templates
    └── index.html

## Installation

Clone the repository:

git clone https://github.com/ivnpu/phishing-email-detector.git

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open in your browser:

http://127.0.0.1:5000

## Future Improvements

- Improve phishing detection accuracy
- Add URL reputation checking
- Enhance the user interface
- Add more cybersecurity detection features

## Author

Ali Abdullah  
Computer Science Student interested in Cybersecurity and Machine Learning.
