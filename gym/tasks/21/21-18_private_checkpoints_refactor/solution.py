"""Refactor private checkpoints: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

import secrets
from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.serde.encrypted import EncryptedSerializer
from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"note": "Synthetic customer phone 555-0100", "delete": True, "wrong_key": False}


class State(TypedDict):
    note: str


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
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


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
