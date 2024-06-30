import re

class CodeReplacer:
    def replace(self, content: str, generated_code: dict) -> str:
        def replacement_func(match):
            placeholder = match.group(2).strip()
            if placeholder in generated_code:
                code = generated_code[placeholder]
                indent = match.group(1)
                indented_code = '\n'.join(indent + line for line in code.splitlines())
                return f"{indent}# Droplet-generated code\n{indented_code}\n{indent}# End Droplet-generated code"
            return match.group(0)

        pattern = r'(\s*)droplet\.execute\("""(.*?)"""\)'
        return re.sub(pattern, replacement_func, content, flags=re.DOTALL)