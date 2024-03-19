import mlflow

model_uri = "runs:/<RUN_ID>/model"
model_name = "MyQAModel"
mlflow.register_model(model_uri, model_name)


# -- end_model_registration_code --
# mlflow models serve -m "models:/MyQAModel/Production" -p 1234
