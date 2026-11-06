"""Version 11: deployment entry point with a deliberately small customer-facing summary."""

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.store.memory import InMemoryStore

from common.copilot import v10


class DeployedClaimState(v10.SecureClaimState):
    public_summary: dict


def build_graph(checkpointer=None, store=None):
    def publish_summary(state: DeployedClaimState) -> dict:
        return {
            "public_summary": {
                "claim_id": state["claim"]["claim_id"],
                "status": state["payment_status"],
                "letter": state["letter"],
                "contact_preference": state["preference"],
            }
        }

    graph = StateGraph(DeployedClaimState, context_schema=v10.AuthorizedContext)
    graph.add_node("secure_claim", v10.build_graph(checkpointer=True, store=store))
    graph.add_node("publish_summary", publish_summary)
    graph.add_edge(START, "secure_claim")
    graph.add_edge("secure_claim", "publish_summary")
    graph.add_edge("publish_summary", END)
    return graph.compile(
        checkpointer=checkpointer if checkpointer is not None else InMemorySaver(),
        store=store if store is not None else InMemoryStore(),
    )
