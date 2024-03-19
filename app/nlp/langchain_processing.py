from langchain.llms import OpenAI
import mlflow
import openai

import os

from dotenv import load_dotenv, find_dotenv

from models.identityNarrativeBaseModel import IdentityNarrative
_ = load_dotenv(find_dotenv())

openai.api_key=os.getenv("OPENAI_API_KEY")
# openai = OpenAI(api_key=openai_api_key)

def session_query_task(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt- .5-turbo",  # Use the appropriate chat model
            messages=[{"role": "system", "content": "Your system message here, if any"},
                      {"role": "user", "content": prompt}]
        )
        flag_on_experiment = True
        modellist = response.choices[0].message['content'].split(" ")
        if flag_on_experiment:
            for modecurrent in modellist:
                return {"session_query": response.choices[0].message['content']}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
  

def session_query(prompt: str):
    # Start MLflow tracking
    mlflow.start_run()
    
    # Example prompt for Q&A task
    prompt = "What is the capital of France?"
    
    # Get the model's answer
    response = session_query_task(prompt)
    
    # Here you would compare the model's answer to a known correct answer
    # and compute metrics such as accuracy, F1 score, etc.
    # For demonstration, let's assume these are your computed metrics
    accuracy = 0.95  # Dummy value
    f1_score = 0.96  # Dummy value
    
    # Log metrics to MLflow
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1_score)
    
    
    # Here you could save your model or any artifacts
    # For Langchain and LLM models, this step may involve saving configuration or metadata
    # as the actual models are API-based and not saved directly
    
    # End the MLflow run
    mlflow.end_run()

def getIdentityNarrative(details: IdentityNarrative):

    return {"received_data": details}



# if __name__ == "__main__":
#     main()  