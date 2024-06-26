import re
from typing import List, Dict
from code_gen import CodeGenerator
from test_gen import TestGenerator
from dependency_analyzer import DependencyAnalyzer
from code_replacer import CodeReplacer


class Processor:
    def __init__(self) -> None:
        self.code_generator = CodeGenerator()
        self.test_generator = TestGenerator()
        self.dependency_analyzer = DependencyAnalyzer()
        self.code_replacer = CodeReplacer()

    def process_file(self, file_path: str) -> Dict[str, str]:
        with open(file_path, 'r') as file:
            content = file.read()

        placeholders = self._extract_placeholders(content)
        generated_code = {}
        tests = {}
        dependencies = set()

        for placeholder, description in placeholders.items():
            code = self.code_generator.generate(description)
            generated_code[placeholder] = code
            tests[placeholder] = self.test_generator.generate(code, description)
            dependencies.update(self.dependency_analyzer.analyze(code))

        new_content = self.code_replacer.replace(content, generated_code)

        return {
            'original_content': content,
            'new_content': new_content,
            'generated_code': generated_code,
            'tests': tests,
            'dependencies': list(dependencies)
        }

    def _extract_placeholders(self, content: str) -> Dict[str, str]:
        pattern = r'droplet\.execute\("""(.*?)"""\)'
        matches = re.findall(pattern, content, re.DOTALL)
        return {f"placeholder_{i}": match.strip() for i, match in enumerate(matches)}
