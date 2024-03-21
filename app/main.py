import os
from uuid import uuid4
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
import uvicorn
# from app.nlp.spacy_prorcessing import session__message_analyze
from app.nlp.langchain_processing import getIdentityNarrative, session_query
from app.nlp.spacy_prorcessing import session__message_analyze
from models.identityNarrativeBaseModel import IdentityNarrative
from models.identityNarrativeModel import IdentityNarrativeInterface
from typing import List




app = FastAPI()


_ = load_dotenv(find_dotenv())

load_dotenv('app/.env')
unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_TRACING_V2"] = "True"
os.environ["LANGCHAIN_PROJECT"] = f"demo Narrative - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com" 
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')  # Update to your API key

@app.post("/analyze/")
async def message_analyze(text: str):
    return session__message_analyze(text)

@app.post("/query/") 
async def session(prompt: str):
    return session_query(prompt)


@app.post("/get0IdentityNarrative/") 
async def session(identitynarrative: List[IdentityNarrative]):

    return await getIdentityNarrative(identitynarrative)

    # uvicorn app.main:app --host 0.0.0.0 --port 8000


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)