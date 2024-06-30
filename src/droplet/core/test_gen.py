from models.llm import LLM

class TestGenerator:
    def __init__(self):
        self.llm = LLM()

    def generate(self, code: str, description: str) -> str:
        prompt = f"""Generate pytest code for the following Python code and description:

                Python Code:
                {code}

                Description:
                {description}

                Requirements for the test code:
                1. Use pytest framework
                2. Include necessary imports
                3. Provide comprehensive test cases covering different scenarios
                4. Use descriptive test function names
                5. Include brief comments explaining the purpose of each test
                6. Do not include any markdown formatting or code block indicators

                Generate only the test code:
                """
        return self.llm.generate(prompt)

    def format_test_file(self, generated_tests: dict) -> str:
        formatted_tests = []
        for placeholder, test_code in generated_tests.items():
            formatted_tests.append(f"# Tests for {placeholder}\n{test_code}\n")
        
        return "\n".join([
            "import pytest",
            "from droplet_util import *  # Import all generated functions",
            "",
            "\n".join(formatted_tests)
        ])