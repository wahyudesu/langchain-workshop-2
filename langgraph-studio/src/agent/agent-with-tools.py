from typing import Annotated
from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


load_dotenv()

# Initialize LLM
llm = init_chat_model("openai:gpt-4.1")

# Initialize tools
tool = TavilySearch(max_results=2)
tools = [tool]
llm_with_tools = llm.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"]) ]}

workflow = StateGraph(State)

# Add nodes to the graph
# Node for chatbot
workflow.add_node("chatbot", chatbot)
# Node for tools
tool_node = ToolNode(tools=[tool])
workflow.add_node("tools", tool_node)

# Add edges and conditions
# Conditional edge from chatbot to tools
workflow.add_conditional_edges(
    "chatbot",
    tools_condition,
)
# Edge from tools back to chatbot
workflow.add_edge("tools", "chatbot")
# Start edge
workflow.add_edge(START, "chatbot")

# Compile the graph
graph = workflow.compile()