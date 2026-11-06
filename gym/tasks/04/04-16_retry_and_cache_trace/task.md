# 04-16 — Diagnose retry and cache from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Retry a transient failure only when repeating the operation is safe. A cache stores a node result under a key; the key must include every input that changes that result. TTL expires a result after a duration, and an injected clock makes that behavior testable without sleeping.

## Your task

Diagnose retry and cache from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "customer_id": "CUS-0001",
    "policy_version": 1,
    "amount_cents": 125000,
    "ttl": 10,
    "advance": 10
  },
  {
    "customer_id": "CUS-0001",
    "policy_version": 1,
    "amount_cents": 125000,
    "ttl": 10,
    "advance": 0
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "A bounded retry must recover from the injected transient read failure."
- "Customer identity belongs in the cache key."
- "The cache must observe the injected clock advancing."
- "A refactor must preserve expiration, not silently make cached results permanent."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-16
uv run gym check 04-16
uv run gym hint 04-16
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-nodes)
