from transformers import pipeline

class KeywordClassifier:
    def __init__(self):
        self.llm = pipeline("zero-shot-classification")

    def has_keyword(self, text, keyword):
        result = self.llm(text, candidate_labels=[keyword])
        return result['labels'][0] == keyword