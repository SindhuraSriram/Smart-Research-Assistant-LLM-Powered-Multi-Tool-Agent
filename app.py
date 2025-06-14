import streamlit as st
from chains.agent_chain import run_agent_chain
from evaluation.evaluator import evaluate_agent
from memory.memory_handler import Memory
import time

memory = Memory()

# ---- Page Config (must be first Streamlit call) ---- #
st.set_page_config(page_title="🧠 AI Agent", layout="wide")

# ---- Theme Toggle ---- #
# ---- Theme Toggle ---- #
theme = st.sidebar.radio("🎨 Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
        /* Overall Background and Text */
        html, body, .stApp, .block-container {
            background-color: #0e1117 !important;
            color: #ffffff !important;
        }

        /* Sidebar background and text */
        .stSidebar, .stSidebarContent, section[data-testid="stSidebar"] {
            background-color: #1f1f27 !important;
            color: #ffffff !important;
        }

        /* Sidebar headings and labels */
        .stSidebar h1, .stSidebar h2, .stSidebar h3,
        .stSidebar label, .stSidebar p, .stSidebar div,
        .stRadio > div > label > div[data-testid="stMarkdownContainer"] > p {
            color: #ffffff !important;
        }

        /* Sidebar radio text */
        .stRadio > div > label {
            color: #ffffff !important;
        }

        /* Radio buttons (fix for both sidebar and main) */
        .stRadio label span, .stRadio label div {
            color: #ffffff !important;
        }

        /* Input fields, buttons, and text area */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div,
        .stExpanderHeader,
        .stExpanderContent,
        .stMarkdown {
            color: #ffffff !important;
        }

        /* Buttons */
        .stButton button,
        .stDownloadButton button {
            background-color: #2c2f3a !important;
            color: #ffffff !important;
            border: 1px solid #555 !important;
        }

        /* Code blocks */
        code {
            color: #d2ffd2 !important;
            background-color: #1e1e1e !important;
        }

        pre code {
            background-color: #1e1e1e !important;
        }

        /* Headings */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

st.title("🧠 Smart Multi-Tool LLM Agent")
st.markdown("Ask a complex question. The agent will plan, choose tools, and execute subtasks.")

# ---- Sample Examples ---- #
examples = [
    "Summarize the code 'for i in range(3): print(i)', calculate 12 * (5 + 7), search for common applications of LLMs",
    "Calculate 200 / 6, summarize importance of human life, run this Python: print(10 ** 3), search for applications of computer vision",
    "Summarize benefits of AI in healthcare, calculate 22 * 3, run Python: x = 5; print(x * 2), search: top AI companies"
]

with st.expander("💡 Example Queries"):
    for i, ex in enumerate(examples):
        if st.button(f"Example {i+1}"):
            st.session_state.query = ex

# ---- User Instructions ---- #
st.markdown("""
### 📝 Input Format Instructions
- Separate subtasks using commas (`,`) such as:
  - `summarize benefits of X`, `calculate 5 + 3`, `run Python: print(123)`, `search: AI in medicine`
- Use the following formats for each tool:
  - **Summarizer**: `summarize [text or topic]`
  - **Calculator**: `calculate [expression]`
  - **Code Executor**: `run Python: [your Python code]`
  - **Search**: `search: [query]` or `find [query]`
- Avoid mixing natural sentences and code in a single subtask.
- Periods (`.`) or other punctuation may affect parsing. Prefer using clear comma-separated phrasing.
""")

query = st.text_input("💬 Enter your query:", value=st.session_state.get("query", ""), placeholder="Try: summarize X, calculate Y, run Python: Z, search for A")

# ---- Run Agent Button ---- #
if st.button("🚀 Run Agent") and query:
    with st.spinner("Thinking..."):
        result = run_agent_chain(query)
        time.sleep(1)
        st.session_state["last_result"] = result
        st.success("Agent completed the task ✅")
        st.experimental_rerun()

# ---- Output Display ---- #
if "last_result" in st.session_state:
    result = st.session_state["last_result"]

    st.markdown("## 🔍 Final Response")
    st.code(result["response"], language="markdown")

    with st.expander("📜 Task Breakdown (Agent Plan)", expanded=False):
        for step in result["steps"]:
            st.markdown(f"- {step}")

    with st.expander("🧠 Memory (Query History)", expanded=False):
        for entry in result["memory"]:
            st.markdown(f"- {entry}")

        # Enable download
        memory_text = "\n".join(result["memory"])
        st.download_button("📥 Download Memory Log", memory_text, file_name="memory_log.txt")

        if st.button("🧹 Clear Memory"):
            memory.clear()
            st.session_state.pop("last_result", None)
            st.success("Memory cleared successfully.")
            st.experimental_rerun()

st.divider()

# ---- Evaluation Suite ---- #
if st.button("🧪 Run Evaluation Suite"):
    with st.spinner("Evaluating agent with benchmark tasks..."):
        summary = evaluate_agent()
        time.sleep(1)
        st.markdown("### ✅ Evaluation Results")
        st.json(summary)
