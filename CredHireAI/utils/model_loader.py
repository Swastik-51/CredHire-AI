import joblib
import streamlit as st

@st.cache_resource
def load_resources():
    vectorizer = joblib.load(os.path.join("CredHireAI/model & vectorizer/", "vectorizer.pkl"))
    model = joblib.load(os.path.join("CredHireAI/model & vectorizer/", "model.pkl"))
    return vectorizer, model
