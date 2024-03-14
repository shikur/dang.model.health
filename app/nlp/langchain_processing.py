from langchain.llms import OpenAI
import openai

import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key=os.getenv("OPENAI_API_KEY")
# openai = OpenAI(api_key=openai_api_key)

def session_query(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate chat model
            messages=[{"role": "system", "content": "Your system message here, if any"},
                      {"role": "user", "content": prompt}]
        )
        return {"session_query": response.choices[0].message['content']}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
    # response = openai(prompt)
#     params = {
#     "model": "text-davinci-003",       # Model ID
#     "prompt": prompt,  # Your prompt to the model
#     "max_tokens": 150,                 # Maximum length of the generated text
#     "temperature": 0.7,                # Creativity of the response
#     "top_p": 1.0,                      # Using nucleus sampling
#     "n": 1,                            # Number of generated responses
#     "stop": None,                      # No specific stop sequence
#     "presence_penalty": 0.0,           # No penalty on new tokens based on presence
#     "frequency_penalty": 0.0           # No penalty on new tokens based on frequency
# }
#    params = {
#     "prompts": [prompt],  # Note the list here
#     "model": "gpt-3.5-turbo",  # Example model, change as per requirement
#     "max_tokens": 50
   
#       }

# Call the generate method with the parameters
#    response = openai.generate(**params)

    
#     # llm = OpenAI()
#     # response = llm(prompt)
#    return {"session_query": response}
