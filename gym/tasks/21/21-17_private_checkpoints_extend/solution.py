"""Extend private checkpoints: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import secrets
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.serde.encrypted import EncryptedSerializer
from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"note": "Synthetic customer phone 555-0100", "delete": True, "wrong_key": False}


class State(TypedDict):
    note: str


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    key = secrets.token_bytes(32)
    serializer = EncryptedSerializer.from_pycryptodome_aes(key=key)
    encoded = serializer.dumps_typed({"note": case["note"]})
    reader = (
        EncryptedSerializer.from_pycryptodome_aes(key=secrets.token_bytes(32))
        if case["wrong_key"]
        else serializer
    )
    restored = reader.loads_typed(encoded)
    saver = InMemorySaver(serde=serializer)
    graph = (
        StateGraph(State)
        .add_node("retain", lambda state: {"note": state["note"]})
        .add_edge(START, "retain")
        .add_edge("retain", END)
        .compile(checkpointer=saver)
    )
    config = {"configurable": {"thread_id": "private-claim"}}
    graph.invoke({"note": case["note"]}, config, version="v2")
    checkpoint_plaintext = case["note"] in repr((saver.storage, saver.blobs))
    if case["delete"]:
        saver.delete_thread("private-claim")
    return {
        "plaintext_visible": case["note"].encode() in encoded[1],
        "roundtrip": restored["note"] == case["note"],
        "checkpoint_plaintext_visible": checkpoint_plaintext,
        "retained": bool(graph.get_state(config).values),
        "key_logged": False,
    }


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
