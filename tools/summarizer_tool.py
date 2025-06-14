# tools/summarizer_tool.py
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Initialize LLM (you can replace with Claude, Mistral, etc., if needed)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Define a prompt template for summarization
summarization_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in a concise and informative manner:\n\n{text}\n\nSummary:"
)

# Create an LLM chain
summarization_chain = LLMChain(llm=llm, prompt=summarization_prompt)

def summarize(text: str) -> str:
    try:
        response = summarization_chain.run(text)
        return f"Summary: {response.strip()}"
    except Exception as e:
        return f"Summarization error: {str(e)}"

print("✅ summarize() loaded")