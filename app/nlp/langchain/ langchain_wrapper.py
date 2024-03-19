from langchain.llms import OpenAI

class LangChainWrapper:
    def __init__(self, api_key):
        self.llm = OpenAI(api_key)

    def generate_text(self, prompt):
        response = self.llm(prompt)
        return response["choices"][0]["text"]
