import os
from pdf_tools.PDFReader import PDFReader
from pdf_tools.KeywordClassifier import KeywordClassifier
from pdf_tools.PDFKeywordProcessor import PDFKeywordProcessor
from db.MongoDBManager import MongoDBManager

if __name__ == "__main__":
    keyword = "fullstack"
    pdf_directory = "curriculums"

    pdf_reader = PDFReader()
    keyword_classifier = KeywordClassifier()
    processor = PDFKeywordProcessor(pdf_reader, keyword_classifier)
    mongo_manager = MongoDBManager()

    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_directory, filename)
            text = pdf_reader.extract_text(file_path)
            result = processor.process(file_path, keyword)
            if result:
                mongo_id = mongo_manager.save_curriculum(filename, text)
                print(f"Palavra-chave '{keyword}' encontrada no arquivo {filename}. Currículo salvo no banco de dados com ID: {mongo_id}")
            else:
                print(f"Palavra-chave '{keyword}' não encontrada no arquivo {filename}. Currículo não salvo.")
