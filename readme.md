# 🤖 Smart Research Assistant – LLM-Powered Multi-Tool Agent

The **Smart Research Assistant** is an AI-powered system designed to autonomously interpret, plan, and solve complex natural language queries by leveraging multiple specialized tools. It showcases the power of modular, tool-augmented Large Language Model (LLM) agents in real-world task orchestration—such as performing calculations, running Python code, summarizing content, and retrieving relevant information via search.

---

## 🧠 What It Does

When a user inputs a multi-part natural language query (e.g.,  
> _“Summarize this code, calculate an expression, run some Python, and search a topic”_)

the assistant:

- Parses and understands the intent behind the full query  
- Decomposes the query into subtasks using rule-based planning  
- Selects and routes each subtask to the appropriate tool  
- Executes each subtask and logs all interactions  
- Returns a structured, final response combining all the outputs  

---

## 🧱 Key Features

### ✅ Task Planning
- Breaks compound queries into discrete, logically ordered subtasks  
- Determines which tool should handle each subtask (e.g., summarization, computation)  

### 🧰 Integrated Tools
- **Calculator**: Safely evaluates math expressions (e.g., `8 * (3 + 2)`)  
- **Code Executor**: Runs lightweight Python snippets securely  
- **Summarizer**: Provides concise summaries of input text  
- **Search Module**: Simulates fetching contextual search results  

### 🔄 Tool Router
- Dynamically routes subqueries to the correct tool based on keyword patterns  
- Uses pattern matching and context parsing to extract relevant segments  

### 🧠 Memory Management
- Logs every step: original query, tool outputs, final response  
- Enables transparency and future context-aware improvements  

### 🧪 Evaluation Suite
- Benchmarks the assistant’s reasoning, tool usage, and accuracy  
- Measures success via task-by-task verification and scores  

---

## 🛠️ Architecture Overview

```bash
ai_agent_assessment/
├── app.py                  # Streamlit frontend
├── agent.py                # Core agent logic (planner, router, memory)
├── chains/
│   └── agent_chain.py      # Orchestration controller
├── tools/                  # Tool-specific logic
│   ├── calculator_tool.py
│   ├── code_tool.py
│   ├── summarizer_tool.py
│   └── search_tool.py
├── memory/
│   └── memory_handler.py   # Logs and short-term memory
├── evaluation/
│   └── evaluator.py        # Benchmarking suite
├── logs/
│   └── sample_logs.txt     # Interaction logs
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
