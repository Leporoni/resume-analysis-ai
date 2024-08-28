import PyPDF2

class PDFReader:
    def __init__(self):
        self.reader = PyPDF2.PdfReader

    def extract_text(self, file_path):
        with open(file_path, 'rb') as file:
            pdf = self.reader(file)
            return "".join(page.extract_text() for page in pdf.pages)