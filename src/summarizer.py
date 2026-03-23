import spacy
from heapq import nlargest
from string import punctuation
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


class TextSummarizer:
    def __init__(self, model_name: str = "en_core_web_sm"):
        self.nlp = spacy.load(model_name)
        self.stop_words = set(stopwords.words("english"))
        self.punctuation_marks = punctuation + "\n"

    def preprocess(self, text: str):
        return self.nlp(text)

    def get_word_frequencies(self, text: str) -> dict:
        doc = self.preprocess(text)
        word_frequencies = defaultdict(int)

        for token in doc:
            if (
                token.text.lower() not in self.stop_words
                and token.text.lower() not in self.punctuation_marks
                and token.is_alpha
            ):
                lemma = token.lemma_.lower()
                word_frequencies[lemma] += 1

        if not word_frequencies:
            return {}

        max_freq = max(word_frequencies.values())

        for word in word_frequencies:
            word_frequencies[word] /= max_freq

        return dict(word_frequencies)

    def score_sentences(self, text: str, word_frequencies: dict) -> dict:
        sentences = sent_tokenize(text)
        sentence_scores = {}

        for sentence in sentences:
            sentence_doc = self.nlp(sentence)
            score = 0
            word_count = 0

            for token in sentence_doc:
                lemma = token.lemma_.lower()
                if lemma in word_frequencies:
                    score += word_frequencies[lemma]
                    word_count += 1

            if word_count > 0:
                sentence_scores[sentence] = score / word_count

        return sentence_scores

    def summarize(self, text: str, summary_ratio: float = 0.3) -> str:
        word_frequencies = self.get_word_frequencies(text)
        sentence_scores = self.score_sentences(text, word_frequencies)
        sentences = sent_tokenize(text)

        select_length = max(1, int(len(sentences) * summary_ratio))
        summary_sentences = nlargest(
            select_length, sentence_scores, key=sentence_scores.get
        )

        return " ".join(summary_sentences)