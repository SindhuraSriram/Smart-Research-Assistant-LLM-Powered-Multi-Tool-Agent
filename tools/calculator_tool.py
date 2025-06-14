# tools/calculator_tool.py
import math

def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return f"Result of calculation: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"
