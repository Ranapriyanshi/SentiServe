import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Classifier", layout="centered")
st.title("🧠 SentiServe: Emotion Classifier (Powered by Hugging Face & FastAPI)")

# Input box
text_input = st.text_area("Enter text to analyze", height=150)
# Model selector
model_choice = st.selectbox("Choose a model:", ["distilbert", "bert", "finbert"])


# Submit button
if st.button("Analyze Emotion"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    "http://localhost:8000/api/sentiment", json={"text": text_input, "model": model_choice}
                )
                # st.code(response.text)
                result = response.json()
                st.subheader("🔍 Results")

                # Display results as a table
                st.write("Using model:", model_choice)

                for item in result["sentiment"]:
                    st.write(f"**{item['label']}**: {round(item['score'] * 100, 2)}%")
                    # st.write(result["text"])

            except Exception as e:
                st.error(f"Request failed: {e}")
