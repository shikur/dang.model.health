from fastapi import FastAPI
import uvicorn
# from app.nlp.spacy_prorcessing import session__message_analyze
from app.nlp.langchain_processing import getIdentityNarrative, session_query
from app.nlp.spacy_prorcessing import session__message_analyze
from models.identityNarrativeBaseModel import IdentityNarrative
from models.identityNarrativeModel import IdentityNarrativeInterface
from typing import List




app = FastAPI()

@app.post("/analyze/")
async def message_analyze(text: str):
    return session__message_analyze(text)

@app.post("/query/") 
async def session(prompt: str):
    return session_query(prompt)


@app.post("/get0IdentityNarrative/") 
async def session(identitynarrative: List[IdentityNarrative]):

    return getIdentityNarrative(identitynarrative)

    # uvicorn app.main:app --host 0.0.0.0 --port 8000


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)