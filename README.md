# 🧠 NLP Text Summarizer

Extractive text summarization using **NLTK** and **SpaCy**.

This project demonstrates how to automatically generate a concise summary of a long English text using classic NLP techniques such as tokenization, lemmatization, and frequency-based sentence scoring.

---

## 🚀 Features

- Text preprocessing
- Stopword removal (NLTK)
- Lemmatization (SpaCy)
- Word frequency normalization
- Sentence scoring with normalization
- Extractive summarization using `heapq`
- Readability-enhanced summary
- Compression metrics

---

## 🧠 Approach

The summarization pipeline follows these steps:

1. Tokenize the text
2. Remove stopwords and punctuation
3. Lemmatize words using SpaCy
4. Compute normalized word frequencies
5. Score sentences based on word importance
6. Select top sentences using `heapq.nlargest`
7. Generate final summary

This is an **extractive summarization approach**, meaning sentences are selected directly from the original text.

---

## 📂 Project Structure
nlp_text_summarizer/
│
├── src/
│ └── summarizer.py # Core summarization logic
│
├── notebooks/
│ └── summarization.ipynb # Jupyter notebook with full pipeline
│
├── data/ # Optional data storage
│
├── README.md
├── requirements.txt
└── .gitignore


---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/nlp_text_summarizer.git
cd nlp_text_summarizer

2. Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Download SpaCy model
python -m spacy download en_core_web_sm

▶️ Usage

Run Jupyter Notebook:

jupyter notebook

Open:

notebooks/summarization.ipynb
📊 Example Output
Extractive Summary

Discovery flew thirty-nine missions, more than any other orbiter.
It played a major role in the construction of the International Space Station.
It was also used for return-to-flight missions after major space shuttle accidents.

Improved Summary

Space Shuttle Discovery is one of the most significant orbiters in NASA history.
It completed thirty-nine missions and played a key role in building the ISS.
It was also used in critical missions after major accidents and introduced important engineering upgrades.

📉 Compression Metrics

Original text: ~700+ words

Summary: ~150–200 words

Compression ratio: ~0.25–0.35

🧠 Technologies

Python 3.11

NLTK

SpaCy

heapq

🔮 Future Improvements

TF-IDF based scoring

TextRank algorithm

Transformer-based models (BERT, T5)

ROUGE evaluation metrics

REST API for summarization

📌 Key Learnings

Practical use of NLP preprocessing techniques

Importance of lemmatization vs raw tokens

Trade-offs between extractive and abstractive summarization

Sentence scoring strategies

🧑‍💻 Author

Developed as part of NLP coursework and hands-on practice.

⭐️ If you like this project

Give it a star ⭐ on GitHub!


---

```bash
OleksiiMoloiko
