🤖 Smart Research Assistant – LLM-Powered Multi-Tool Agent
The Smart Research Assistant is an AI-powered system designed to autonomously interpret, plan, and solve complex natural language queries by leveraging multiple specialized tools. It showcases the power of modular, tool-augmented Large Language Model (LLM) agents in real-world task orchestration, such as performing calculations, running Python code, summarizing content, and retrieving relevant information via search.

🧠 What It Does
When a user inputs a multi-part natural language query (e.g., “Summarize this code, calculate an expression, run some Python, and search a topic”), the assistant:

Parses and understands the intent behind the full query.

Decomposes the query into subtasks using rule-based planning.

Selects and routes each subtask to the appropriate tool.

Executes each subtask and logs all interactions.

Returns a structured, final response combining all the outputs.

🧱 Key Features
✅ Task Planning
Breaks a compound query into discrete, logically ordered subtasks.

Determines which tool should handle each subtask (e.g., summarization, computation).

🧰 Integrated Tools
Calculator: Safely evaluates math expressions (e.g., 8 \* (3 + 2)).

Code Executor: Runs lightweight Python snippets securely and returns outputs.

Summarizer: Provides concise and meaningful summaries of input text.

Search Module: Simulates fetching contextual search results for user-provided topics.

🔄 Tool Router
Dynamically routes subqueries to the correct tool based on keyword patterns.

Uses pattern matching and context parsing to extract relevant segments from the input.

🧠 Memory Management
Logs every step including the original query, tool outputs, and final response.

Enables transparency and potential for future context-aware improvements.

🧪 Evaluation Suite
Allows benchmarking of the assistant’s reasoning, tool usage, and accuracy across various predefined tasks.

Measures success via task-by-task verification and scores.

🛠️ Architecture Overview
The system is modular, comprising the following components:

bash
Copy
Edit
ai_agent_assessment/
├── app.py # Streamlit frontend
├── agent.py # Core agent logic (planner, router, memory)
├── chains/
│ └── agent_chain.py # Orchestration controller
├── tools/ # Tool-specific logic
│ ├── calculator_tool.py
│ ├── code_tool.py
│ ├── summarizer_tool.py
│ └── search_tool.py
├── memory/
│ └── memory_handler.py # Logs and short-term memory
├── evaluation/
│ └── evaluator.py # Benchmarking suite
├── logs/
│ └── sample_logs.txt # Interaction logs
├── requirements.txt # Python dependencies
└── README.md # Project documentation
🚀 Getting Started
Step 1: Clone and Set Up Environment
git clone https://github.com/yourusername/ai_agent_assessment.git
cd ai_agent_assessment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run the Application
streamlit run app.py
💬 Example Query
Try this to see all tools in action:

Summarize this code: for i in range(3): print(i). Then calculate 12 \* (5 + 7). Also, search for common applications of LLMs.
Expected Output
📝 Summary of the code snippet.

🧮 Result of the math expression: 144.

🧑‍💻 Output of the Python snippet: printed 0 1 2.

🔍 Simulated search results for LLM applications.

🧪 Evaluation & Testing
Run the evaluation/evaluator.py to benchmark performance.

Evaluation Metrics
✔️ Correctness of task planning

✔️ Tool accuracy and reliability

✔️ Clarity of returned outputs

✔️ Fault tolerance and graceful error handling

Example Benchmark Task Set
Task Expected Result
Calculate 8 \* (2 + 3) 40
Summarize a paragraph Concise summary
Execute code: for i in range(3): print(i) Printed output
Search for use cases of LLMs Simulated list of sources

📌 Notes
Summarization and search are mocked tools for demonstration.

Safe execution environment limits scope of Python code runner.

Easily extendable for real APIs like OpenAI, SerpAPI, WolframAlpha, etc.
