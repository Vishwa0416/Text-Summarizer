import streamlit as st
from summarizer import extractive_summary, abstractive_summary

st.set_page_config(page_title="Text Summarizer", layout="wide")

st.title("📝 Text Summarizer Tool")

text_input = st.text_area("Enter Text to Summarize", height=300)

mode = st.radio("Choose Summarization Mode:", ("Extractive", "Abstractive"))

num_sentences = st.slider("Number of Sentences (Extractive)", 1, 10, 3)

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            if mode == "Extractive":
                result = extractive_summary(text_input, num_sentences)
            else:
                result = abstractive_summary(text_input)
        st.subheader("Summary:")
        st.success(result)
