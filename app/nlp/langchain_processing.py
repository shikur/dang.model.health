from langchain.llms import OpenAI

def session_query(prompt: str):
    llm = OpenAI()
    response = llm(prompt)
    return {"session_query": response}
