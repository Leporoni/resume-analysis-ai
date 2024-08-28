import os

from pdf_tools.PDFReader import PDFReader
from pdf_tools.KeywordClassifier import KeywordClassifier
from pdf_tools.PDFKeywordProcessor import PDFKeywordProcessor

if __name__ == "__main__":
    keyword = "palavra-chave"
    pdf_directory = "curriculums"

    pdf_reader = PDFReader()
    keyword_classifier = KeywordClassifier()
    processor = PDFKeywordProcessor(pdf_reader, keyword_classifier)

    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_directory, filename)
            result = processor.process(file_path, keyword)
            print(f"Palavra-chave encontrada no arquivo {filename}? {result}")