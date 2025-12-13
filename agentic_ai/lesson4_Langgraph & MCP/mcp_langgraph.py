from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition

from langchain.chat_models import init_chat_model
import asyncio

model = init_chat_model("ollama:gpt-oss:20b-cloud")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
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

    tools = await client.get_tools()

    def call_model(state: MessagesState):
        response = model.bind_tools(tools).invoke(state["messages"])
        return {"messages": response}

    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")
    graph = builder.compile()
    
    math_response = await graph.ainvoke({"messages": "what's (3 + 5) x 12?"})
    print("Math Response:", math_response["messages"][-1].content)

    weather_response = await graph.ainvoke({"messages": "what is the weather in nyc?"})
    print("Weather Response:", weather_response["messages"][-1].content)

asyncio.run(main())