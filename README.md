# 📰 Fake News Detection

This is a simple machine learning web app that detects whether a news article is **Real** or **Fake** using a trained model.

🚀 **[Click here to try the app]()**

## 🔍 Features
- Enter any news headline or article
- Instantly get prediction: ✅ Real or 🟥 Fake
- Built with: Python, Scikit-learn, and Streamlit

## 📁 Files in This Repo
- `app.py` – Streamlit application
- `model.pkl` – Trained ML model
- `vectorizer.pkl` – TF-IDF vectorizer
- `Fake.csv` and `True.csv` – Datasets
- `Fake_news_detection.ipynb` – Model training notebook

## 🛠️ Run Locally (Optional)
To run on your machine:

```bash
pip install streamlit scikit-learn pandas
streamlit run app.py
