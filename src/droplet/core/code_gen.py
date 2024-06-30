from models.llm import LLM
class CodeGenerator:
    def __init__(self):
        self.llm = LLM()

    def generate(self, description: str) -> str:
        prompt = f"""Generate Python code for the following task:

        {description}

        Please ensure the generated code:
        1. Is correctly indented
        2. Uses 4 spaces for indentation
        3. Follows PEP 8 style guidelines
        4. Does not use triple quotes (\"\"\") anywhere in the code

        Generated code:
        """
        return self.llm.generate(prompt)
    

