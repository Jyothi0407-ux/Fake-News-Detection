import streamlit as st
import pickle

# Use regular open() for both files
import pickle
import gzip
import numpy as np

# Load the machine learning model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Reduce the precision of numerical values
model.weights = np.around(model.weights, decimals=4)

# Remove unnecessary data
del model.dataset

# Compress the pickle file
with gzip.open('model.pkl.gz', 'wb') as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("📰 Fake News Detector")
st.write("Enter a news headline or article and find out if it's Real or Fake!")

user_input = st.text_area("Enter News Here:")

if st.button("Predict"):
    if user_input:
        input_vector = vectorizer.transform([user_input])
        result = model.predict(input_vector)
        if result[0] == 1:
            st.success("✅ This is REAL News.")
        else:
            st.error("🟥 This is FAKE News.")
    else:
        st.warning("⚠️ Please enter some text.")
