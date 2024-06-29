import re


class CodeReplacer:
    def replace(self, content: str, generated_code: dict) -> str:
        for placeholder, code in generated_code.items():
            pattern = f'droplet.execute("""{re.escape(placeholder)}""")'
            replacement = f"# Droplet-generated code\n{code}\n# End Droplet-generated code"
            content = re.sub(pattern, replacement, content)
        return content