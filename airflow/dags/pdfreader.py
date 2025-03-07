from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
import os

class Reader:
    def __init__(self, path_to_pdfs, api_key):
        self.api_key = os.environ.get('API_KEY')
        self.path = path_to_pdfs
        self.texts = []
        self.chunks = []

    def get_texts(self, collection):
        text = ''
        for pdf in collection:
            pdf_reader = PdfReader(pdf)
            for page in pdf.reader_pages:
                text += page.extract_text()
        self.texts.append(text)
        return self

    def get_text_chunk(self, text):
        text_splitter = CharacterTextSplitter(
            separators = '\n',
            chunk_size = 10000,
            chunk_overlap = 200,
            length_function = len
        )

        self.chunks = text_splitter
        return self