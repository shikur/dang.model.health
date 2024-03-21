from openai import OpenAI



class IdenitityNarrativeagent:
    def __init__(self, api_key):
        """
        Initialize the agent with the OpenAI API key.
        """
        self.api_key = api_key

    def generate_text(self, detail_str):
        """
        Generates text using OpenAI's Completion API.
        
        :param detail_str: String containing the details or prompt for generation.
        :return: Generated text as a string.
        """
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.completions.create(model="gpt-3.5-turbo-instruct",  # Adjust model as needed
            prompt=f"Please generate a paragraph using these words:\n{detail_str}",
            temperature=0.7,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0)
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


