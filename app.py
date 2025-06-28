import streamlit as st
import pickle

# Use regular open() for both files
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

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
