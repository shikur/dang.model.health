import mlflow
from sklearn.metrics import accuracy_score, f1_score
from qa_model import answer_question

# Example data
questions = ["What is the capital of France?"]
true_answers = ["Paris"]  # Example true answers
predicted_answers = [answer_question(q) for q in questions]

# Calculate metrics
accuracy = accuracy_score(true_answers, predicted_answers)
f1 = f1_score(true_answers, predicted_answers, average='macro')

# Track experiment
mlflow.set_experiment("Q&A_LangChain")
with mlflow.start_run():
    mlflow.log_param("Model", "GPT-3")
    mlflow.log_metric("Accuracy", accuracy)
    mlflow.log_metric("F1 Score", f1)
