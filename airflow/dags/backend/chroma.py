import chromadb
from schema import TextInput

class DBClient:
    def __init__(self, persist_dir = '/tmp/chroma'):
        self.client = chromadb.PersistentClient(path = persist_dir)
        try:
            self.collection = self.client.get_collection('contexts')
        except:
            self.collection = self.client.create_collection(name = 'contexts')

    def add_context(self, ids, texts):
        self.collection.add(ids = ids, documents = texts)
        return self
    
    def query(self, query, n_results):
        return self.collection.query(query_texts = query, n_results = n_results).get('documents')