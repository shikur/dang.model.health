import mlflow

from app.nlp.mlflow_tracking.evaluation import calculate_metrics

def setup_mlflow_experiment(experiment_name):
    mlflow.set_experiment(experiment_name)

def log_experiment(question, answer, reference_answer, parameters):
    with mlflow.start_run():
        mlflow.log_params(parameters)
        
        # Calculate metrics
        accuracy, f1_score = calculate_metrics(answer, reference_answer)
        
        mlflow.log_metrics({"accuracy": accuracy, "f1_score": f1_score})
        
        # Log other components as needed, e.g., model version

        mlflow.log_param("question", question)
        mlflow.log_param("answer", answer)
        mlflow.log_param("reference_answer", reference_answer)