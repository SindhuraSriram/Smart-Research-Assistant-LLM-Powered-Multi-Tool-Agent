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

## 🚀 Getting Started

### Step 1: Clone and Set Up Environment

```bash
git clone https://github.com/yourusername/ai_agent_assessment.git
cd ai_agent_assessment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
streamlit run app.py
```

## 💬 Example Query

Try this query to test all tools in action:

*Summarize this code:* `for i in range(3): print(i)`  
*Then calculate:* `12 * (5 + 7)`  
*Also, search for:* common applications of LLMs

## ✅ Expected Output

* 📝 Code summary  
* 🧮 Math result: 144  
* 🧑‍💻 Python output: 0 1 2  
* 🔍 Simulated search results for LLM applications

## 🧪 Evaluation & Testing

Run the evaluation suite:

```bash
python evaluation/evaluator.py
```

### ✅ Evaluation Metrics

* ✔️ Correctness of task planning
* ✔️ Tool accuracy and reliability
* ✔️ Clarity of final output
* ✔️ Fault tolerance and graceful failure handling

## 🧪 Example Benchmark Task Set

| Task                                  | Expected Result           |
|---------------------------------------|---------------------------|
| Calculate 8 * (2 + 3)                 | 40                        |
| Summarize a paragraph                 | Concise summary           |
| Execute for i in range(3): print(i)   | Printed output: 0 1 2     |
| Search for use cases of LLMs          | Simulated list of results |

![System Architecture](architecture%20diagram.png)


