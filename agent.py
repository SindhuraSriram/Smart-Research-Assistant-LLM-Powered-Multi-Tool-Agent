from tools.search_tool import search
from tools.calculator_tool import calculate
from tools.code_tool import execute_code
from tools.summarizer_tool import summarize
from memory.memory_handler import Memory
from datetime import datetime
import re

memory = Memory()

def task_planner(task: str) -> list:
    """Breaks a query into subqueries by comma and maps them to appropriate tools."""
    #sub_tasks = [t.strip() for t in re.split(r",\s*(?=(?:[^']*'[^']*')*[^']*$)", task) if t.strip()]
    sub_tasks = [t.strip() for t in re.split(r"[.,]|then|also", task, flags=re.IGNORECASE) if t.strip()]
    steps = []

    for sub in sub_tasks:
        lowered = sub.lower()
        if re.search(r"run\s+this\s+python", lowered):
            steps.append(("Use code executor to run the Python snippet.", sub))
        elif "calculate" in lowered or re.search(r"\d+\s*[*+/\-^]\s*\d+", sub):
            steps.append(("Use calculator to solve expression.", sub))
        elif "summarize" in lowered or "summarise" in lowered:
            steps.append(("Use summarizer to generate a concise explanation.", sub))
        elif "search" in lowered or "find" in lowered:
            steps.append(("Use search to find relevant information.", sub))
        else:
            steps.append(("Use summarizer to generate a concise explanation.", sub))

    return steps

def tool_router(step: str, query: str) -> str:
    """Routes a given step to the appropriate tool with improved parsing and normalization."""
    try:
        if "calculator" in step:
            match = re.search(r"calculate[:\-]*\s*(.*)", query, re.IGNORECASE)
            expression = match.group(1).strip() if match else query
            return calculate(expression)

        elif "summarizer" in step:
            match = re.search(r"(?:summarize|summarise)[:\-]*\s*(.*)", query, re.IGNORECASE)
            summary_input = match.group(1).strip() if match else query
            return summarize(summary_input)

        elif "code" in step or "executor" in step:
            match = re.search(r"run this python[:\-]*\s*(.*)", query, re.IGNORECASE)
            code = match.group(1).strip() if match else query
            return execute_code(code)

        elif "search" in step:
            match = re.search(r"(?:search for|search|find)[:\-]*\s*(.*)", query, re.IGNORECASE)
            query_str = match.group(1).strip() if match else query
            return search(query_str)

        else:
            return "No matching tool found."
    except Exception as e:
        return f"Error during tool execution: {str(e)}"

def run_agent(query: str) -> dict:
    timestamp = datetime.now()
    steps_with_tasks = task_planner(query)
    memory.store(f"[{timestamp}] User query: {query}")
    memory.store(f"[{timestamp}] Planned steps: {[step for step, _ in steps_with_tasks]}")

    results = []
    formatted_response = "🔍 **Smart Research Assistant Result**\n\n"

    for step, task in steps_with_tasks:
        result = tool_router(step, task)
        formatted_response += f"### ➤ {step}\n{result}\n\n"
        memory.store(f"[{datetime.now()}] {step} → {result}")

    memory.store(f"[{datetime.now()}] Final response: {formatted_response}")

    return {
        "steps": [s for s, _ in steps_with_tasks],
        "response": formatted_response,
        "memory": memory.recall()
    }
