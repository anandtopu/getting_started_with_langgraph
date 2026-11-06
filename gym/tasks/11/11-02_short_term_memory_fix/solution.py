"""Fix short term memory: Use a new message ID for a new turn instead of overwriting the previous turn.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, trim_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"max_messages": 2, "second_text": "An estimate is now attached."}


class State(MessagesState):
    summary: str


def build_graph(seen: list[int], max_messages: int = 2):
    model = get_chat_model(
        responses=[
            AIMessage(content="Please attach an estimate."),
            AIMessage(content="Estimate received."),
        ]
    )

    def respond(state: State) -> dict:
        history = (
            [SystemMessage(content=state["summary"])] if state.get("summary") else []
        ) + state["messages"]
        context = trim_messages(
            history,
            max_tokens=max_messages,
            token_counter=len,
            strategy="last",
            start_on="human",
            include_system=True,
        )
        seen.append(len(context))
        response = model.invoke(context)
        return {"messages": [response]}

    def summarize(state: State) -> dict:
        facts = [message.content for message in state["messages"] if message.type == "human"]
        return {"summary": " | ".join(facts[-2:])[:160]}

    graph = StateGraph(State)
    graph.add_node("respond", respond)
    graph.add_node("summarize", summarize)
    graph.add_edge(START, "respond")
    graph.add_edge("respond", "summarize")
    graph.add_edge("summarize", END)
    return graph.compile(checkpointer=InMemorySaver())


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    seen = []
    graph = build_graph(seen, case["max_messages"])
    config = {"configurable": {"thread_id": "claim-memory"}}
    graph.invoke(
        {"messages": [HumanMessage(content="A pipe burst.", id="human-1")]}, config, version="v2"
    )
    result = graph.invoke(
        {"messages": [HumanMessage(content=case["second_text"], id="human-2")]},
        config,
        version="v2",
    ).value
    return {
        "saved_messages": len(result["messages"]),
        "model_context_sizes": seen,
        "summary": result["summary"],
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
