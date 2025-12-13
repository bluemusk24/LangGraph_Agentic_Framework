
# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent  
import asyncio

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["math_server.py"],
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            model = ChatOllama(model="gpt-oss:20b-cloud")
            agent = create_react_agent(model, tools)  
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})

            print("Agent Response:", agent_response["messages"][-1].content)
            #print(agent_response)
            
asyncio.run(main())