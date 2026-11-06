"""Probe installed graph/model contracts without contacting a provider."""

import inspect
from importlib.metadata import version

from langgraph.graph import StateGraph
from langgraph.types import GraphOutput

from common.models import get_chat_model
from common.schemas import ClaimExtraction
from scripts.first_graph import build_graph


def main() -> None:
    for package in ("langgraph", "langchain", "langchain-core", "langgraph-checkpoint-sqlite"):
        print(f"{package} {version(package)}")
    parameters = inspect.signature(StateGraph.add_node).parameters
    for name in ("defer", "retry_policy", "cache_policy", "timeout", "error_handler"):
        assert name in parameters, f"Missing expected node option: {name}"
    graph = build_graph()
    output = graph.invoke({"claim": {"claim_id": "CLM-1"}, "steps": []}, version="v2")
    assert isinstance(output, GraphOutput)
    assert output.value["status"] == "needs_information"
    parts = list(graph.stream({"claim": {}, "steps": []}, stream_mode="updates", version="v2"))
    assert all({"type", "ns", "data"} <= part.keys() for part in parts)
    extraction = (
        get_chat_model(scenario="extract").with_structured_output(ClaimExtraction).invoke("claim")
    )
    assert extraction.amount_cents == 125_000
    print("Installed API contract probes passed.")


if __name__ == "__main__":
    main()
