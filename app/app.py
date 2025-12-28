from flask import Flask, render_template, request
import numpy as np
import joblib
from urllib.parse import urlparse
import csv, os
from datetime import datetime

app = Flask(__name__)

# Load model & scaler
model = joblib.load("../models/final_phishing_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

LOG_FILE = "../logs/predictions.csv"


# ---------- FEATURE EXTRACTION ----------
def extract_features(url):
    parsed = urlparse(url)
    features = []

    features.append(len(url))                         # URL length
    features.append(len(parsed.netloc))               # Hostname length
    features.append(1 if parsed.scheme == "https" else 0)
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))

    suspicious_words = ["login", "secure", "verify", "update", "account",
                        "bank", "paypal", "apple", "microsoft"]
    features.append(1 if any(w in url.lower() for w in suspicious_words) else 0)

    # Pad remaining features with 0
    TOTAL_FEATURES = scaler.mean_.shape[0]
    while len(features) < TOTAL_FEATURES:
        features.append(0)

    return np.array(features).reshape(1, -1)


# ---------- RULE-BASED CHECK ----------
def rule_based(url):
    url = url.lower()

    if any(k in url for k in ["login", "verify", "secure", "update"]):
        if not url.startswith("https"):
            return "Phishing"

    if any(tld in url for tld in [".xyz", ".info", ".top", ".tk"]):
        return "Phishing"

    if url.count('-') >= 3 or url.count('.') >= 4:
        return "Suspicious"

    return "Safe"


# ---------- LOGGING ----------
def log_result(url, result, confidence):
    os.makedirs("../logs", exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["time", "url", "result", "confidence"])
        writer.writerow([datetime.now(), url, result, confidence])


# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]

    # ---------- RULE-BASED CHECK ----------
    rule = rule_based(url)

    if rule == "Phishing":
        safe_percent = 5   # very unsafe
        confidence = "High Risk"
        log_result(url, "Phishing", confidence)

        return render_template(
            "result.html",
            result="Phishing",
            confidence=confidence,
            safe_percent=safe_percent,
            url=url
        )

    if rule == "Suspicious":
        safe_percent = 45
        confidence = "Suspicious"
        log_result(url, "Suspicious", confidence)

        return render_template(
            "result.html",
            result="Suspicious",
            confidence=confidence,
            safe_percent=safe_percent,
            url=url
        )

    # ---------- ML PREDICTION ----------
    features = extract_features(url)
    features = scaler.transform(features)

    prob = model.predict_proba(features)[0][1] * 100
    safe_percent = round(100 - prob)

    if prob >= 75:
        result = "Phishing"
    elif prob >= 40:
        result = "Suspicious"
    else:
        result = "Legitimate"

    confidence = f"{safe_percent}% Safe"
    log_result(url, result, confidence)

    return render_template(
        "result.html",
        result=result,
        confidence=confidence,
        safe_percent=safe_percent,
        url=url
    )




if __name__ == "__main__":
    app.run(debug=True)
