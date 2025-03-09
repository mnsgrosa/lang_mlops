from backend.schema import TextInput
import slate3k as slate
import numpy as np
import hashlib
import os

class Reader:
    def __init__(self):
        self.algorithm = 'sha256'
        self.api_key = os.environ.get('API_KEY')
        self.path = os.environ.get('PDF_PATH')
        self.input_text = []
        
    def get_texts(self, filename):
        full_path = os.path.join(self.path, filename)
        with open(full_path, 'rb') as f:
            extracted_text = slate.PDF(f)
            extracted_text = ''.join(extracted_text)
        return extracted_text
    
    def generate_id(self, filename):
        hash_func = hashlib.new(self.algorithm)
        full_path = os.path.join(self.path, filename)
        with open(full_path, 'rb') as file:
            while chunk := file.read(8192): 
                hash_func.update(chunk)
        return hash_func.hexdigest()
    
    def workflow(self):
        self.input_text = []  
        all_files = os.listdir(self.path)
        all_pdfs = [file for file in all_files if file.endswith('.pdf')]  
        
        for pdf in all_pdfs:
            texts = self.get_texts(pdf)
            text_id = str(self.generate_id(pdf))
            self.input_text.append({'query_id':text_id, 'texts':texts}) 
        return self.input_text