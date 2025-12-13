from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
import asyncio

async def main():
    print("Starting client...")
    
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                "command": "python",
                "args": ["weather_stdio.py"],
                "transport": "stdio",
            }
        }
    )

    print("Getting tools...")
    tools = await client.get_tools()
    print(f"Got {len(tools)} tools: {[tool.name for tool in tools]}")
    
    print("Creating agent...")
    model = ChatOllama(model="gpt-oss:20b-cloud")
    agent = create_react_agent(model, tools)

    print("\nAsking math question...")
    math_response = await agent.ainvoke(
        {"messages": [("user", "what is (3+5) x 12?")]}
    )
    print("Math Response:", math_response["messages"][-1].content)

    print("\nAsking weather question...")
    weather_response = await agent.ainvoke(
        {"messages": [("user", "what's the weather in New York?")]}
    )
    print("Weather Response:", weather_response["messages"][-1].content)

asyncio.run(main())