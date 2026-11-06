"""Extend semantic and privacy: Delete the requested memory while preserving unrelated evidence.. Run this file with Python. No live model or network."""

from typing import TypedDict

from langchain_core.embeddings import Embeddings
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.store.memory import InMemoryStore

from common.pretty import print_state

DEFAULT_CASE = {"query": "water leak", "customer_id": "CUS-0001"}


class MemoryState(TypedDict):
    note: str


class ClaimEmbeddings(Embeddings):
    """Tiny transparent word vectors for teaching; not a production semantic model."""

    words = ("water", "theft", "fire", "receipt")

    def embed_query(self, text: str) -> list[float]:
        tokens = set(text.lower().split())
        vector = [float(word in tokens) for word in self.words]
        # A fallback dimension avoids zero-vector cosine differences with optional NumPy.
        return [*vector, float(not any(vector))]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_query(text) for text in texts]


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    store = InMemoryStore(index={"dims": 5, "embed": ClaimEmbeddings(), "fields": ["text"]})
    namespace = ("customers", case["customer_id"], "episodes")
    store.put(namespace, "water", {"text": "water receipt"})
    store.put(namespace, "theft", {"text": "theft report"})
    store.put(("customers", "OTHER", "episodes"), "private", {"text": "water private"})
    results = store.search(namespace, query=case["query"], limit=2)
    ranking = [
        item.key for item in sorted(results, key=lambda item: (-(item.score or 0), item.key))
    ]
    saver = InMemorySaver()
    builder = StateGraph(MemoryState)
    builder.add_node("remember", lambda state: {"note": state["note"]})
    builder.add_edge(START, "remember")
    builder.add_edge("remember", END)
    graph = builder.compile(checkpointer=saver)
    config = {"configurable": {"thread_id": "retention-demo"}}
    graph.invoke({"note": "water receipt"}, config, version="v2")
    store.delete(namespace, "theft")
    checkpoint_retains_fact = bool(graph.get_state(config).values)
    saver.delete_thread("retention-demo")
    return {
        "ranking": ranking,
        "remaining": sorted(item.key for item in store.search(namespace)),
        "other_customer_visible": any(item.key == "private" for item in results),
        "checkpoint_retains_fact_after_store_delete": checkpoint_retains_fact,
        "checkpoint_deleted_separately": not graph.get_state(config).values,
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
