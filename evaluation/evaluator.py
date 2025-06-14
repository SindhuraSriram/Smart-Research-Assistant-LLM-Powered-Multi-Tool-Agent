from agent import run_agent

benchmarks = [
    "Calculate 8 * (2 + 3)",
    "Summarize: Artificial Intelligence is the simulation of human intelligence in machines.",
    "Run code: for i in range(3): print(i)",
    "Search for applications of LLMs"
]

def evaluate_agent():
    results = []
    success = 0

    for task in benchmarks:
        result = run_agent(task)
        output = result["response"]
        if "error" not in output.lower():
            success += 1
        results.append({
            "query": task,
            "steps": result["steps"],
            "output": output
        })

    return {
        "total": len(benchmarks),
        "successful": success,
        "score (%)": round((success / len(benchmarks)) * 100, 2),
        "details": results
    }
