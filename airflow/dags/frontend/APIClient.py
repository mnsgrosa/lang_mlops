import httpx
import json
from schema import TextInput, Question, ListTextInput, QueryText, Background

class APIClient:
    def __init__(self, port='8000'):
        self.client = httpx.Client(timeout = 300)
        self.base_url = f'http://backend:{port}'
        self.getter = '/context/get'
        self.poster = '/context/post'
        self.background = '/background'
        self.llm = '/llm/response'

    def post(self, text_input):
        if not isinstance(text_input, list):
            raise ValueError("Input must be a list of dictionaries")

        response = self.client.post(
            self.base_url + self.poster,
            json = text_input,
        )
        
        response.raise_for_status()
        return response.json()

    def get(self, query):
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary")

        query = QueryText(**query)

        response = self.client.request(
            method = 'GET',
            url = self.base_url + self.getter,
            json = query.model_dump(),
        )
        
        response.raise_for_status()
        return response.json()

    def post_background(self, background):
        if not isinstance(background, dict):
            raise ValueError("Background must be a dictionary")

        background = Background(**background)

        response = self.client.post(
            self.base_url + self.background,
            json = background
        )
        response.raise_for_status()
        return response.json()

    def get_llm_response(self, question):
        if not isinstance(question, dict):
            raise ValueError("Question must be a dictionary")
       
        response = self.client.request(
            method='GET',
            url=self.base_url + self.llm,
            json=validated_input.model_dump()
        )
        
        response.raise_for_status()
        return response.json()
