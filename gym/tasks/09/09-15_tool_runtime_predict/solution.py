"""Predict tool runtime across the declared cases. Run this file with Python. No live model or network."""

from dataclasses import dataclass

from langchain.tools import ToolRuntime, tool
from langchain_core.messages import AIMessage, ToolMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.store.memory import InMemoryStore
from langgraph.types import Command

from common.pretty import print_state

DEFAULT_CASE = {"customer_id": "CUS-0001", "preference": "email"}


@dataclass
class Context:
    customer_id: str


class State(MessagesState):
    saved_preference: str


@tool
def save_preference(preference: str, runtime: ToolRuntime[Context]) -> Command:
    """Save an allowed contact preference for the authenticated customer."""
    if preference not in {"email", "sms", "phone"}:
        raise ValueError("Unsupported preference")
    namespace = ("customers", runtime.context.customer_id, "preferences")
    runtime.store.put(namespace, "contact", {"value": preference})
    return Command(
        update={
            "saved_preference": preference,
            "messages": [
                ToolMessage(content="Preference saved", tool_call_id=runtime.tool_call_id)
            ],
        }
    )


def build_graph(store=None):
    graph = StateGraph(State, context_schema=Context)
    graph.add_node("tools", ToolNode([save_preference], handle_tool_errors=True))
    graph.add_edge(START, "tools")
    graph.add_edge("tools", END)
    return graph.compile(store=store if store is not None else InMemoryStore())


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    store = InMemoryStore()
    call = {"name": "save_preference", "args": {"preference": case["preference"]}, "id": "save-1"}
    result = (
        build_graph(store)
        .invoke(
            {"messages": [AIMessage(content="", tool_calls=[call])]},
            context=Context(case["customer_id"]),
            version="v2",
        )
        .value
    )
    saved = store.get(("customers", case["customer_id"], "preferences"), "contact")
    return {
        "saved": saved.value if saved else None,
        "state_preference": result.get("saved_preference"),
        "tool_call_id": result["messages"][-1].tool_call_id,
        "model_visible_fields": sorted(save_preference.tool_call_schema.model_fields),
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"customer_id": "CUS-0001", "preference": "email"},
        {"customer_id": "CUS-0020", "preference": "sms"},
        {"customer_id": "CUS-0001", "preference": "fax"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
