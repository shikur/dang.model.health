from fastapi import FastAPI
from app.nlp.spacy_prorcessing import session__message_analyze
from app.nlp.langchain_processing import session_query

app = FastAPI()

@app.post("/analyze/")
async def message_analyze(text: str):
    return session__message_analyze(text)

@app.post("/query/") 
async def session(prompt: str):
    return session_query(prompt)