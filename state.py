from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END

class ConversationState(TypedDict):
    messages: Annotated[Sequence[HumanMessage | AIMessage], "Conversation history"]
    current_step: Annotated[str, "Current conversation step"]

graph = StateGraph(ConversationState)