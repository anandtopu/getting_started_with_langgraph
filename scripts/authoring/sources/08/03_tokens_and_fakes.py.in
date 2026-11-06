"""Read fake text chunks through the graph's messages stream. Zero model cost.

Run: uv run python modules/08_llms_inside_nodes/examples/03_tokens_and_fakes.py
Expected: chunks reconstruct the scripted acknowledgment and identify its graph node.
"""

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, START, MessagesState, StateGraph

from common.models import get_chat_model
from common.pretty import print_state
from common.schemas import ClaimExtraction

DEFAULT_CASE = {"text": "Larkspur received your synthetic claim.", "structured": False}


def build_graph(text: str = DEFAULT_CASE["text"]):
    model = get_chat_model(responses=[AIMessage(content=text, id="ack-1")])

    def acknowledge(state: MessagesState) -> dict:
        return {"messages": [model.invoke(state["messages"])]}

    graph = StateGraph(MessagesState)
    graph.add_node("acknowledge", acknowledge)
    graph.add_edge(START, "acknowledge")
    graph.add_edge("acknowledge", END)
    return graph.compile()


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    chunks, nodes = [], set()
    for part in build_graph(case["text"]).stream(
        {"messages": [HumanMessage(content="A pipe burst.")]}, stream_mode="messages", version="v2"
    ):
        chunk, metadata = part["data"]
        chunks.append(chunk.content)
        nodes.add(metadata["langgraph_node"])
    text = "".join(chunks)
    invoked = (
        get_chat_model(responses=[AIMessage(content=case["text"])]).invoke("A pipe burst.").content
    )
    parsed = ClaimExtraction.model_validate_json(text).model_dump() if case["structured"] else None
    return {
        "text": text,
        "matches_invoke": text == invoked,
        "structured": parsed,
        "nodes": sorted(nodes),
        "nonempty_chunks": sum(bool(chunk) for chunk in chunks),
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
