import httpx
import json
from schema import TextInput, ListTextInput, Question

class APIClient:
    def __init__(self, port='8000'):
        self.client = httpx.Client(timeout = 300)
        self.base_url = f'http://localhost:{port}'
        self.getter = '/context/get'
        self.poster = '/context/post'
        self.llm = '/llm/response'

    def post(self, text_input):
        if not isinstance(text_input, dict):
            raise ValueError("Input must be a dictionary")
        
        validated_input = TextInput(**text_input)
        
        response = self.client.post(
            self.base_url + self.poster,
            json=validated_input.model_dump(),
        )
        
        response.raise_for_status()
        return response.json()

    def get(self, query):
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary")
        
        validated_input = ListTextInput(**query)
        
        response = self.client.request(
            method='GET',
            url=self.base_url + self.getter,
            json=validated_input.model_dump()
        )
        
        response.raise_for_status()
        return response.json()

    def get_llm_response(self, question):
        if not isinstance(question, dict):
            raise ValueError("Question must be a dictionary")
        
        validated_input = Question(**question)
       
        response = self.client.request(
            method='GET',
            url=self.base_url + self.llm,
            json=validated_input.model_dump()
        )
        
        response.raise_for_status()
        return response.json()