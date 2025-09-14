graph.add_edge("node_a", "node_b")

def route_based_on_step(state: ConversationState) -> str:
    if state["current_step"] == "response_generated":
        return "check_if_done"
    else:
        return "respond_to_user"

graph.add_conditional_edges(
    "respond_to_user",
    route_based_on_step,
    {
        "check_if_done": "check_if_done",
        "respond_to_user": "respond_to_user"
    }
)