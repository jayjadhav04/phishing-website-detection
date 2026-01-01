## 🛡️ Phishing Website Detection System

A hybrid **Machine Learning + Rule-Based** web application that detects whether a website URL is **Legitimate**, **Suspicious**, or **Phishing**. Built using **Python, Flask, and XGBoost** following a complete industry-standard ML pipeline.

## 🚀 Features
- URL-based phishing detection
- Hybrid Rule-Based + Machine Learning approach
- Three-level classification:# 🔐 Phishing Website Detection
### Data Science Project (Applied Machine Learning)

An end-to-end **Data Science project with Applied Machine Learning** that detects whether a given website URL is **Legitimate or Phishing**.  
The system applies **data analysis, feature engineering, model comparison, and ML deployment** using an **XGBoost classifier**, and provides predictions with a **confidence score** via a Flask web application.

---

## 📌 Problem Statement
Phishing websites imitate legitimate platforms to steal sensitive user information such as login credentials and financial details.  
Due to evolving attack patterns, manual detection is unreliable, creating a need for **data-driven and automated phishing detection systems**.

---

## 🎯 Solution Overview
This project follows a **Data Science workflow**:
- Data understanding and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering on URL-based patterns
- Training and evaluating multiple ML models
- Selecting the best model based on performance metrics
- Deploying the final model as a web application

The system classifies URLs as:
- ✅ Legitimate  
- ❌ Phishing  

And returns a **confidence score** for better interpretability.

---

## 🧠 Data Science & Machine Learning Approach
- **Domain:** Cybersecurity
- **Learning Type:** Supervised Classification
- **Input:** Website URL
- **Output:** Class label + confidence score
- **Final Model:** XGBoost Classifier

### 🔍 Feature Engineering
- URL length
- Special character frequency
- HTTPS presence
- Suspicious keywords
- Redirection indicators
- Domain-based attributes

---

## 📊 Model Evaluation & Results
Multiple machine learning models were trained and evaluated as part of the **model selection phase** of the data science lifecycle.  
Special emphasis was placed on **Phishing Recall**, as false negatives are costly in cybersecurity applications.

### 🔎 Model Comparison

| Model | Accuracy | Phishing Recall |
|------|---------|----------------|
| Logistic Regression | 93.65% | 93.35% |
| Decision Tree | 93.31% | 93.00% |
| SVM | 95.27% | 95.01% |
| Random Forest | 96.41% | 96.94% |
| **XGBoost (Final Model)** | **97.03%** | **97.64%** |

### 🏆 Final Model Performance (XGBoost)
- **Accuracy:** 96.85%
- **Precision:** 95.89%
- **Recall:** 97.90%
- **F1-Score:** 96.88%

XGBoost was selected as the final model due to its superior performance and high recall, ensuring effective phishing detection while minimizing false negatives.

---

## ⚙️ End-to-End Workflow
1. URL input provided by the user  
2. URL-based feature extraction  
3. Data preprocessing and transformation  
4. Prediction using trained XGBoost model  
5. Output classification with confidence score  
6. Logging of predictions for analysis  

---

## 🖥️ Web Application
A Flask-based web interface enables:
- Real-time URL input
- Instant phishing/legitimate prediction
- Display of confidence level for transparency

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Data Science:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn, XGBoost  
- **Web Framework:** Flask  
- **Visualization:** Matplotlib, Seaborn  

---

## ▶️ How to Run the Project
1. Clone the repository:
git clone https://github.com/jayjadhav04/phishing-website-detection.git

2. Navigate to the project directory:
cd phishing-website-detection

3. Install dependencies:
pip install -r requirements.txt

4. Run the Flask application:
python app/app.py

5. Open your browser and visit:
http://127.0.0.1:5000/

---

## 🚀 Future Enhancements
- Cloud deployment (AWS / Render / Streamlit)
- Integration of blacklist & WHOIS-based features
- Advanced feature engineering
- Deep learning-based phishing detection
- Analytics dashboard for prediction insights

---

## 🧪 Technologies Used
- Python
- Flask
- Scikit-learn
- XGBoost
- Pandas, NumPy
- HTML, CSS

## Future Scope
- WHOIS domain age integration
- Web traffic analysis APIs
- Deep learning based phishing
