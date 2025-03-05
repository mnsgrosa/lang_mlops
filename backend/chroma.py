import chromadb
from .schema import TextInput

class DBClient:
    def __init__(self, persist_dir = '/tmp/chroma'):
        self.client = chromadb.PersistentClient(path = persist_dir)
        try:
            self.collection = self.client.get_collection('contexts')
        except:
            self.collection = self.client.create_collection(name = 'contexts')

    def add_context(self, textinput:TextInput):
        self.collection.add(documents = textinput.text, ids = textinput.query_id)
        return self
    
    def query(self, query, n_results = 1):
        return self.collection.query(query_texts = query, n_results = n_results)