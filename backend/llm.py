from langchain_google_genai import GoogleGenerativeAI
import os

class MyLLM:
    def __init__(self, google_model = 'gemini-2.0-flash'):
        self.api_key = os.environ.get('API_KEY')
        self.model = google_model
        self.chat = GoogleGenerativeAI(model = self.model, google_api_key = self.api_key)
        self.background = None

    def get_background(self, background):
        self.background = background
        return self

    def invoke(self, contexts, prompt:str):
        if self.background:
            template = f'''
            {self.background},
            {contexts},
            agora responda a seguinte pergunta:
            {prompt}
            '''
            return self.chat.invoke(template).content
        template = f'''
        You are a machine learning specialist and you are inserted in the following context
        {contexts}
        and now that you have the context you should answer the following question:
        {prompt}
        '''
        return self.chat.invoke(template).content