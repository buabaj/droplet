import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

class LLM:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o", 
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates Python code. Provide only the code without any additional formatting or markdown or backticks."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred while generating code: {str(e)}")
            return ""