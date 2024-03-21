from langchain_wrapper import LangChainWrapper
from utils import log_experiment



# Generate
def generate_subject_introduction(age, racial_background, location, parental_role, professional_role, community_roles):
    """
    Generates an introduction to the subject based on the provided details.
    """
    prompt = f"Introduction to the Subject:\n\n" \
            f"Generate a detailed introduction for a subject based on the following criteria:\n\n" \
            f"1. Basic Information:\n" \
            f"   - Age: {age}\n" \
            f"   - Racial or Ethnic Background: {racial_background}\n" \
            f"   - Geographical Location: {location}\n\n" \
            f"2. Key Roles in Life:\n" \
            f"   - Parental Role: {parental_role}\n" \
            f"   - Professional Role: {professional_role}\n" \
            f"   - Community Roles: {community_roles}\n\n" \
            "This introduction should offer a comprehensive overview of the subject's demographic background and their roles in life, providing insights into their daily responsibilities and contributions."
            
    introduction = llm.generate(prompt)
    return introduction
def main():
    # Initialize LangChain with your API key
    lc = LangChainWrapper(api_key='your_api_key_here')



    # Example usage with hypothetical subject details
age = "35"
racial_background = "Asian-American"
location = "San Francisco, CA"
parental_role = "Father of two, actively involved in their education and extracurricular activities"
professional_role = "Software Engineer in a tech company, specializing in AI development"
community_roles = "Volunteers at local coding bootcamps, participates in tech-for-good initiatives"

# Generate the introduction to the subject
subject_introduction = generate_subject_introduction(age, racial_background, location, parental_role, professional_role, community_roles)
print(subject_introduction)
    # Generate text using LangChain
prompt = "Example prompt"
generated_text = lc.generate_text(prompt)

print("Generated Text:", generated_text)

# Example metrics and parameters to log with MLflow
metrics = {"length": len(generated_text)}
params = {"prompt": prompt}
log_experiment(metrics, params, experiment_name="langchain_experiment")

if __name__ == "__main__":
    main()
