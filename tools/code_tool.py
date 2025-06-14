# tools/code_tool.py
import io
import contextlib

def execute_code(code: str) -> str:
    try:
        local_vars = {}
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code, {}, local_vars)
        return f"Code executed successfully.\nOutput:\n{output.getvalue()}"
    except Exception as e:
        return f"Code execution error: {str(e)}"

