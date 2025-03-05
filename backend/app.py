from fastapi import FastAPI
from .schema import TextInput, ListTextInput, Question, TextOutput, LLMInput, LLMOutput
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .llm import MyLLM
from .chroma import DBClient

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
def add_context(textinput:TextInput):
    db.add_context(textinput)
    return {'status': 'success'} 

@app.get('/context/get')
def get_context(textinput:ListTextInput):
    results = db.query(query = textinput.query, n_results = 3).get('documents')
    output = TextOutput(**{'text':results[0]})
    return {'text':output}

@app.get('/llm/response')
def get_llm_response(prompt_body:Question):
    context = db.query(query = prompt_body.question, n_results = 1).get('documents')
    llm_response = model.invoke(contexts = context, prompt = prompt_body.question)
    return {'text': llm_response}