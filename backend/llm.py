from langchain_ollama import ChatOllama

class MyLLM:
    def __init__(self, local_model = 'llama3.1:8b'):
        self.chat = ChatOllama(model = local_model)

    def invoke(self, contexts, prompt:str):
        template = f'''
        You are a machine learning specialist and you are inserted in the following context
        {contexts}
        and now that you have the context you should answer the following question:
        {prompt}
        '''
        return self.chat.invoke(template).content