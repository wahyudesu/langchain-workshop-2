from langchain_openai import ChatOpenAI

def respond_to_user(state: ConversationState) -> ConversationState:
    messages = state["messages"]
    model = ChatOpenAI()
    response = model.invoke(messages)
    new_messages = list(messages)
    new_messages.append(response)
    return {
        "messages": new_messages,
        "current_step": "response_generated"
    }

graph.add_node("respond_to_user", respond_to_user)