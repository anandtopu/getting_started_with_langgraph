"""Trace store namespaces: Delete the actual memory key.. Run this file with Python. No live model or network."""

from dataclasses import dataclass
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.store.memory import InMemoryStore

from common.pretty import print_state

DEFAULT_CASE = {"customer_id": "CUS-0001", "preference": "email"}


@dataclass
class Context:
    customer_id: str


class State(TypedDict):
    preference: str
    remembered: str


def remember(state: State, runtime: Runtime[Context]) -> dict:
    namespace = ("customers", runtime.context.customer_id, "semantic")
    runtime.store.put(namespace, "contact", {"preference": state["preference"]})
    item = runtime.store.get(namespace, "contact")
    return {"remembered": item.value["preference"]}


def build_graph(store=None):
    graph = StateGraph(State, context_schema=Context)
    graph.add_node("remember", remember)
    graph.add_edge(START, "remember")
    graph.add_edge("remember", END)
    return graph.compile(store=store if store is not None else InMemoryStore())


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    store = InMemoryStore()
    graph = build_graph(store)
    graph.invoke(
        {"preference": case["preference"]}, context=Context(case["customer_id"]), version="v2"
    )
    graph.invoke({"preference": "phone"}, context=Context("CUS-OTHER"), version="v2")
    namespace = ("customers", case["customer_id"], "semantic")
    found = store.search(namespace)
    store.delete(namespace, "missing")
    other = store.get(("customers", "CUS-OTHER", "semantic"), "contact")
    return {
        "found": [item.value for item in found],
        "deleted": store.get(namespace, "contact") is None,
        "other": other.value,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
