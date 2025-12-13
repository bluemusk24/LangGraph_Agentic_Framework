# Use server from examples/servers/streamable-http-stateless/

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent  
import asyncio


async def main():
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)
            
            # Create and run the agent
            model = ChatOllama(model="gpt-oss:20b-cloud")
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})

            print("Agent Response:", agent_response["messages"][-1].content)
            #print(agent_response)
            
asyncio.run(main())