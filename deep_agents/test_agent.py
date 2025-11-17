import os
from typing import Literal
from dotenv import load_dotenv, find_dotenv

from langchain.tools import tool
from langchain.chat_models import init_chat_model

from tavily import TavilyClient
from deepagents import create_deep_agent

_ = load_dotenv(find_dotenv())
model = init_chat_model(model="ollama:gpt-oss:20b-cloud", temperature=0)
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=tavily_api_key)

# Search tool to use to do research
@tool
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    search_docs = tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
    return search_docs

INSTRUCTIONS = """You are an an expert researcher."""

agent = create_deep_agent(model=model,
                          instructions=INSTRUCTIONS, 
                          tools=[internet_search])