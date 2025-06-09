from pydantic import BaseModel
from typing import Dict, Optional

class Background(BaseModel):
    bg:str

class TextInput(BaseModel):
    query_id: str
    text: str
    metadatas: Optional[Dict[str, str]] = None

class QueryText(BaseModel):
    query: str
    n_results: int
    metadatas: Optional[Dict[str, str]] = None

class Question(BaseModel):
    question: str
    n_contexts: int
