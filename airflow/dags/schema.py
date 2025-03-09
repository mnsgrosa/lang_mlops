from pydantic import BaseModel
from typing import List

class Background(BaseModel):
    bg:str

class TextInput(BaseModel):
    query_id: str
    text: str

class ListTextInput(BaseModel):
    inputs:List[TextInput]

class QueryText(BaseModel):
    query: str
    n_results: int

class TextOutput(BaseModel):
    text:List[str]

class Question(BaseModel):
    question: str
    n_contexts: int
    
class LLMInput(BaseModel):
    text:str

class LLMOutput(BaseModel):
    texts:str
