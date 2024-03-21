from langchain.llms import OpenAI
import mlflow
import openai

import os

from dotenv import load_dotenv, find_dotenv

from app.nlp.langchain.input_identityNarrative import concated_inputNarrative
from models.identityNarrativeBaseModel import CoreChallenges, IdentityNarrative
from models.identityNarrativeModel import AspirationsDreams, BasicInformation, Conclusion, Contemplations, IdentityNarrativeInterface, InteractsWithSociety , KeyRoles, CoreChallenges, LifeEvents, LifeStyle, PersonalAnecdote, ValueBeliefs

_ = load_dotenv(find_dotenv())

load_dotenv('app/.env')

openai.api_key = os.getenv("OPENAI_API_KEY")

def session_query_task(prompt: str):
    try:
        response = openai.Completion.create(model="gpt-3.5-turbo",  # Use the appropriate chat model
        messages=[{"role": "system", "content": "Your system message here, if any"},
                  {"role": "user", "content": prompt}])
        flag_on_experiment = True
        modellist = response.choices[0].message.content.split(" ")
        if flag_on_experiment:
            for modecurrent in modellist:
                return {"session_query": response.choices[0].message.content}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
  

def session_query(prompt: str):
    pass

def getIdentityNarrative(details: IdentityNarrative):  
    try:
     detail_str_list= concated_inputNarrative(details)
    except Exception as e:
            print(f"Error: {e}")
            return {"error": str(e)}   
    
    try:
       for detail_str in detail_str_list:                                    
           response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct", # Specify the model here
                prompt= f"please generate a paragraph using  words:\n {detail_str}", # Your prompt
                temperature=0.7, # Adjust creativity
                max_tokens=500, # Maximum length of the generated text
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0)
           return response.choices[0].text
           
    except Exception as e:
            print(f"Error: {e}")
            return {"error": str(e)}
    return {"received_data": details}
 