"""Diagnose retry and cache from execution evidence. Run this file with Python. No live model or network."""

import json
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import CachePolicy, RetryPolicy

from common.cache import ClockCache
from common.pretty import print_state

DEFAULT_CASE = {
    "customer_id": "CUS-0001",
    "policy_version": 1,
    "amount_cents": 125000,
    "ttl": 10,
    "advance": 10,
}


class State(TypedDict):
    customer_id: str
    policy_version: int
    amount_cents: int
    covered: bool


def cache_key(state: State) -> str:
    return json.dumps([state["policy_version"], state["amount_cents"]])


def build_graph(lookup, cache, ttl: int = 10):
    graph = StateGraph(State)
    graph.add_node(
        "lookup_policy",
        lookup,
        retry_policy=RetryPolicy(
            max_attempts=2, initial_interval=0, jitter=False, retry_on=ConnectionError
        ),
        cache_policy=CachePolicy(key_func=cache_key, ttl=ttl),
    )
    graph.add_edge(START, "lookup_policy")
    graph.add_edge("lookup_policy", END)
    return graph.compile(cache=cache)


def scenario(case: dict | None = None) -> dict:
    values = dict(DEFAULT_CASE if case is None else case)
    clock = [0.0]
    calls = []

    def lookup(state: State) -> dict:
        calls.append(cache_key(state))
        if len(calls) == 1:
            raise ConnectionError("Synthetic transient policy read")
        return {"covered": state["customer_id"] == "CUS-0001" and state["amount_cents"] <= 200000}

    graph = build_graph(lookup, ClockCache(lambda: clock[0]), values["ttl"])
    payload = {key: values[key] for key in ("customer_id", "policy_version", "amount_cents")}
    results = [graph.invoke(payload, version="v2").value["covered"]]
    results.append(graph.invoke(payload, version="v2").value["covered"])
    clock[0] += values["advance"]
    results.append(graph.invoke(payload, version="v2").value["covered"])
    other = {**payload, "customer_id": "CUS-0002"}
    results.append(graph.invoke(other, version="v2").value["covered"])
    return {"covered": results, "lookup_calls": len(calls)}


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {
            "advance": 10,
            "amount_cents": 125000,
            "customer_id": "CUS-0001",
            "policy_version": 1,
            "ttl": 10,
        },
        {
            "advance": 0,
            "amount_cents": 125000,
            "customer_id": "CUS-0001",
            "policy_version": 1,
            "ttl": 10,
        },
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": "Customer identity belongs in the cache key."}


if __name__ == "__main__":
    main()
