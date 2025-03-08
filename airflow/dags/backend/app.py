from fastapi import FastAPI
from typing import List
from schema import TextInput, Question, TextOutput, LLMInput, LLMOutput, QueryText
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from llm import MyLLM
from chroma import DBClient

model = MyLLM()
app = FastAPI()
db = DBClient()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post('/context/post')
def add_context(textinput:List[TextInput]):
    ids = [item.query_id for item in textinput]
    text = [item.text for item in textinput]
    client.add_context()
    return {'status': 'success'} 

@app.get('/context/get')
def get_context(textinput:QueryText):
    results = db.query(query = textinput.query, n_results = textinput.n_results)
    output = TextOutput([item for item in results.get('documents')])
    return {'text':output}

@app.get('/llm/response')
def get_llm_response(prompt_body:Question):
    context = db.query(query = prompt_body.question, n_results = prompt_body.n_contexts)
    llm_response = model.invoke(contexts = context, prompt = prompt_body.question)
    return {'text': llm_response}