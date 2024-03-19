import mlflow
from mlflow.tracking import MlflowClient

def log_metrics(metrics: dict):
    for key, value in metrics.items():
        mlflow.log_metric(key, value)

def log_params(params: dict):
    for key, value in params.items():
        mlflow.log_param(key, value)

def register_model(model_name: str, model_uri: str):
    client = MlflowClient()
    client.create_registered_model(model_name)
    result = client.create_model_version(model_name, model_uri, mlflow.active_run().info.run_id)
    return result
