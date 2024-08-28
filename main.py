from pdf_tools.PDFReader import PDFReader
from pdf_tools.KeywordClassifier import KeywordClassifier
from pdf_tools.PDFKeywordProcessor import PDFKeywordProcessor

if __name__ == "__main__":
    file_path = "curriculums/JohnDoeResume.pdf"
    keyword = "palavra-chave"

    pdf_reader = PDFReader()
    keyword_classifier = KeywordClassifier()
    processor = PDFKeywordProcessor(pdf_reader, keyword_classifier)

    result = processor.process(file_path, keyword)
    print(f"Palavra-chave encontrada? {result}")