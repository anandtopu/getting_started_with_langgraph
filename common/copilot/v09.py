"""Version 09: progress events around the durable claims workflow."""

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer
from langgraph.graph import END, START, StateGraph
from langgraph.store.memory import InMemoryStore

from common.copilot import v06, v08


class StreamingClaimState(v08.DurableClaimState):
    processing_status: str


def build_builder(store=None):
    def announce(state: StreamingClaimState) -> dict:
        get_stream_writer()({"stage": "intake", "claim_id": state["claim"]["claim_id"]})
        return {"processing_status": "reviewing"}

    def complete(state: StreamingClaimState) -> dict:
        get_stream_writer()({"stage": "review_complete", "approved": state["approved"]})
        return {"processing_status": "review_complete"}

    graph = StateGraph(StreamingClaimState, context_schema=v06.CustomerContext)
    graph.add_node("announce", announce)
    graph.add_node("durable_review", v08.build_graph(checkpointer=True, store=store))
    graph.add_node("complete_review", complete)
    graph.add_edge(START, "announce")
    graph.add_edge("announce", "durable_review")
    graph.add_edge("durable_review", "complete_review")
    return graph


def build_graph(checkpointer=None, store=None):
    graph = build_builder(store)
    graph.add_edge("complete_review", END)
    return graph.compile(
        checkpointer=checkpointer if checkpointer is not None else InMemorySaver(),
        store=store if store is not None else InMemoryStore(),
    )
