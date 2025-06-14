# tools/search_tool.py

from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Prompt template to simulate semantic web search results
search_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are a smart search engine. Return two informative and relevant bullet points for the following search query:

Query: {query}

Search Results:
1.
2:
"""
)

# Build LLM chain
search_chain = LLMChain(llm=llm, prompt=search_prompt)

def search(query: str) -> str:
    try:
        result = search_chain.run(query)
        return f"Simulated search results for '{query}':\n{result.strip()}"
    except Exception as e:
        return f"Search tool error: {str(e)}"

print("✅ search() loaded successfully")

# This function is a placeholder and should be replaced with actual API calls to fetch news articles.