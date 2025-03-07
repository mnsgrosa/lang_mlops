from PyPDF2 import PdfReader
from .backend.schema import TextInput
import hashlib
import os

class Reader:
    def __init__(self):
        self.buf_size = 65536
        self.algorithm = 'sha256'
        self.hash_func = hashlib.new(self.algorithm)
        self.api_key = os.environ.get('API_KEY')
        self.path = os.environ.get('PDF_PATH')
        self.input_text = []

    def get_texts(self, filename):
        full_path = os.path.join(self.path, filename)
        text = ''

        pdf_reader = PdfReader(full_path)
        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text

    def generate_id(self, filename):
        full_path = os.path.join(self.path, filename)
        with open(full_path, 'rb') as file:
            while chunk := file.read(8192):
                self.hash_func.update(chunk)
        
        return hash_func.hexdigest
        

    def workflow(self):
        all_pdfs = os.listdir(self.path)
        for pdf in all_pdfs:
            texts = self.get_texts(pdf)
            text_id = self.generate_id()
            self.input_text.append(TextInput({'query_id':str(text_id), 'text':texts}))

        return self.input_texts