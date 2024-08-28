from pdf_tools.PDFReader import PDFReader
from pdf_tools.KeywordClassifier import KeywordClassifier

class PDFKeywordProcessor:
    def __init__(self, pdf_reader, keyword_classifier):
        self.pdf_reader = pdf_reader
        self.keyword_classifier = keyword_classifier

    def process(self, file_path, keyword):
        text = self.pdf_reader.extract_text(file_path)
        return self.keyword_classifier.has_keyword(text, keyword)