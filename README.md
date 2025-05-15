📝 Text Summarizer  
This project is a simple yet powerful web application for summarizing long texts using both extractive and abstractive techniques. Built with NLTK, Hugging Face Transformers, and Streamlit, it offers a clean interface for quick and accurate text summarization.

🚀 Features  
🧠 Extractive Summarization: Selects key sentences from the original text to form a concise summary.  
🤖 Abstractive Summarization: Uses transformer models (e.g., `distilbart-cnn-12-6`) to generate human-like summaries.  
🖥️ Streamlit Frontend: Interactive and user-friendly UI for real-time text input and summarization.  
🎯 Customizable Length: Choose the number of sentences for extractive summaries and adjust min/max length for abstractive ones.  
⚙️ Lightweight: Fast and efficient — perfect for quick use cases and demonstrations.

🧰 Technologies Used  
- NLTK  
- Hugging Face Transformers  
- Streamlit  
- PyTorch (used by the transformer model)

📸 Demo  
Watch the demo and walkthrough of the app: *Coming Soon* 🎥

📂 Getting Started  
Clone the repository and run the app locally:

```bash
git clone https://github.com/your-username/Text-Summarizer
cd Text-Summarizer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
