import streamlit as st
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "news_classifier.joblib"
model = joblib.load(MODEL_PATH)

category_names = {
    1: "World 🌍",
    2: "Sports ⚽",
    3: "Business 📈",
    4: "Sci/Tech 💻"
}

st.set_page_config(
    page_title="News Category Classifier",
    page_icon="📰",
    layout="centered"
)

st.title(" News Category & Topic Classifier")

st.write(
    "Enter a news headline or article below "
    "to predict its category."
)

news_text = st.text_area(
    "Enter news text",
    placeholder="Example: The stock market rose after the latest economic report..."
)

if st.button("Classify News"):
    if news_text.strip():
        prediction = model.predict([news_text])[0]

        st.success(
            f"Predicted Category: {category_names[prediction]}"
        )
    else:
        st.warning("Please enter some news text first.")
