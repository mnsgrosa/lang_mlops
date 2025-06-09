import chromadb

class DBClient:
    def __init__(self, persist_dir = '/tmp/chroma'):
        self.client = chromadb.PersistentClient(path = persist_dir)
        try:
            self.collection = self.client.get_collection('contexts')
        except:
            self.collection = self.client.create_collection(name = 'contexts')

    def add_context(self, ids, texts, metadata = None):
        self.collection.add(ids = ids, documents = texts, metadatas = metadata)
        return self
    
    def query(self, query, n_results,metadatas = None):
        return self.collection.query(query_texts = query, n_results = n_results, metadatas = metadatas).get('documents')

    def get(self):
        return self.collection.get()