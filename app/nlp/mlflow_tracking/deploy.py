from mlflow.tracking import MlflowClient

def register_and_deploy_model(run_id, model_name="best_qa_model"):
    client = MlflowClient()
    model_uri = f"runs:/{run_id}/model"
    model_version = client.create_model_version(name=model_name, source=model_uri, run_id=run_id)
    # Transition the model version to "Production"
    client.transition_model_version_stage(name=model_name, version=model_version.version, stage="Production")

# Example: Register and deploy the best model
# You would typically select the 'run_id' of your best performing model based on your evaluation criteria
register_and_deploy_model("your_run_id_here")
