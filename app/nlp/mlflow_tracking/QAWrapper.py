import mlflow.pyfunc

from models.langchain import QAModule

class QAWrapper(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = QAModule()  # Load your model here

    def predict(self, context, model_input):
        return self.model.answer_question(model_input['question'], model_input['context'])

# Register the model
mlflow.pyfunc.log_model(
    artifact_path="qa_model",
    python_model=QAWrapper(),
    registered_model_name="QA_Model"
)
