from PyPDF2 import PdfReader
import os

class Reader:
    def __init__(self, path_to_pdfs, api_key):
        self.api_key = os.environ.get('API_KEY')
        self.path = os.environ.get('PDF_PATH')
        self.texts = []

    def get_texts(self, filename):
        full_path = os.path.join(self.path, filename)
        text = ''

        pdf_reader = PdfReader(full_path)
        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        self.texts.append(text)

        return self

    def workflow(self):
        all_pdfs = os.listdir(self.path)
        for pdf in all_pdfs:
            self.get_texts(pdf)
        
        return self