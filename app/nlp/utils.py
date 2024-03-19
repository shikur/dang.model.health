import mlflow

def log_experiment(metrics: dict, params: dict, experiment_name: str = "default_experiment"):
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run():
        for key, value in metrics.items():
            mlflow.log_metric(key, value)
        for key, value in params.items():
            mlflow.log_param(key, value)
