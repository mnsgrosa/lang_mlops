from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    query_id: str
    text: str

class ListTextInput(BaseModel):
    query: str

class TextOutput(BaseModel):
    text:List[str]

class Question(BaseModel):
    question: str
    
class LLMInput(BaseModel):
    text:str

class LLMOutput(BaseModel):
    texts:str
