"""Refactor handoffs: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.types import Command

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "question": "Explain the deductible."}


class State(MessagesState):
    claim_id: str
    active_agent: str


def build_graph():
    def transfer(state: State) -> Command:
        request = AIMessage(
            content="",
            id="handoff-request",
            tool_calls=[{"name": "transfer_to_policy", "args": {}, "id": "handoff-1"}],
        )
        response = ToolMessage(
            content="Transferred to policy", tool_call_id="handoff-1", id="handoff-result"
        )
        # KEY IDEA: the destination belongs to the enclosing graph, not this child.
        return Command(
            graph=Command.PARENT,
            goto="policy",
            update={"messages": [request, response], "active_agent": "policy"},
        )

    def policy(state: State) -> dict:
        model = get_chat_model(
            responses=[AIMessage(content="The deductible is 100000 cents.", id="policy-answer")]
        )
        return {"messages": [model.invoke(state["messages"])]}

    intake = StateGraph(State)
    intake.add_node("transfer", transfer)
    intake.add_edge(START, "transfer")
    parent = StateGraph(State)
    parent.add_node("intake", intake.compile())
    parent.add_node("policy", policy)
    parent.add_edge(START, "intake")
    parent.add_edge("policy", END)
    return parent.compile()


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    value = (
        build_graph()
        .invoke(
            {
                "claim_id": case["claim_id"],
                "active_agent": "intake",
                "messages": [HumanMessage(content=case["question"], id="customer-1")],
            },
            version="v2",
        )
        .value
    )
    messages = value["messages"]
    requests = {
        call["id"] for message in messages if message.type == "ai" for call in message.tool_calls
    }
    results = {message.tool_call_id for message in messages if message.type == "tool"}
    return {
        "active_agent": value["active_agent"],
        "claim_id": value["claim_id"],
        "paired": requests == results,
        "roles": [message.type for message in messages],
        "answer": messages[-1].content,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
