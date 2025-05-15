import nltk
from nltk.tokenize import sent_tokenize
from transformers import pipeline

nltk.download("punkt")

def extractive_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:num_sentences])

abstractive_pipeline = pipeline("summarization")

def abstractive_summary(text, max_length=130, min_length=30):
    summary = abstractive_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
