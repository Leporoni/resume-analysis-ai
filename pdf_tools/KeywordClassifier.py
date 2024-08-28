from transformers import pipeline

class KeywordClassifier:
    def __init__(self):
        self.llm = pipeline("zero-shot-classification")

    def has_keyword(self, text, keyword):
        text_lower = text.lower()
        keyword_lower = keyword.lower()
        
        return keyword_lower in text_lower
