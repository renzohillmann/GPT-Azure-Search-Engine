from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI
from langchain_experimental.tools import PythonAstREPLTool


def create_csvsearch_agent(llm: AzureChatOpenAI, prompt: str):
    """Create a simple agent that can run Python code to query a CSV file."""
    return create_react_agent(llm, tools=[PythonAstREPLTool()], prompt=prompt)