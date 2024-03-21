from langchain.llms import OpenAI
import mlflow
from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import os

from dotenv import load_dotenv, find_dotenv

from agents.AgentExecutor import agent_executor
from app.nlp.langchain.input_identityNarrative import concated_inputNarrative
from app.nlp.mlflow_tracking.mlflow_setup import log_experiment
from models.identityNarrativeBaseModel import CoreChallenges, IdentityNarrative
from models.identityNarrativeModel import AspirationsDreams, BasicInformation, Conclusion, Contemplations, IdentityNarrativeInterface, InteractsWithSociety , KeyRoles, CoreChallenges, LifeEvents, LifeStyle, PersonalAnecdote, ValueBeliefs
from uuid import uuid4
from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from langsmith import traceable, Client
from langsmith.wrappers import wrap_openai
_ = load_dotenv(find_dotenv())

load_dotenv('app/.env')



unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_TRACING_V2"] = 'True'
os.environ["LANGCHAIN_PROJECT"] = f"healthdemo - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = 'ls__7a96a7f811844901b7e6b247c859530a' #os.getenv('LANGCHAIN_API_KEY')  # Update to your API key

# Used by the agent in this tutorial
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')



def session_query_task(prompt: str):
    try:
        response = client.completions.create(model="gpt-3.5-turbo",  # Use the appropriate chat model
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

    """
    The objective of this method to run agent
    """
async def excagentmain(detail_str):
    try:
        result = await agent_executor(detail_str, os.getenv("OPENAI_API_KEY"))
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}    
    return result

    """
       It required to return all narratives
    """
async def getIdentityNarrative(details: IdentityNarrative):
    identityNarrative_ouputs = [] 
    
    try:
    
     detail_str_list= concated_inputNarrative(details)       
     for detail_str in detail_str_list:
           result = await excagentmain(detail_str)
           print(result)
           identityNarrative_ouputs.append(result)     
        
     return identityNarrative_ouputs       
    except Exception as e:
            print(f"Error: {e}")
            return {"error": str(e)}
    return {"received_data": details}
 