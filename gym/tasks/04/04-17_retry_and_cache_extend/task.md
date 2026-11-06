# 04-17 — Extend retry and cache: The cache must observe the injected clock advancing.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Retry a transient failure only when repeating the operation is safe. A cache stores a node result under a key; the key must include every input that changes that result. TTL expires a result after a duration, and an injected clock makes that behavior testable without sleeping.

## Your task

The cache must observe the injected clock advancing. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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
  },
  {
    "customer_id": "CUS-0001",
    "policy_version": 1,
    "amount_cents": 300000,
    "ttl": 10,
    "advance": 10
  },
  {
    "customer_id": "CUS-0001",
    "policy_version": 2,
    "amount_cents": 125000,
    "ttl": 10,
    "advance": 10
  },
  {
    "customer_id": "CUS-0003",
    "policy_version": 1,
    "amount_cents": 125000,
    "ttl": 10,
    "advance": 10
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-17
uv run gym check 04-17
uv run gym hint 04-17
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-nodes)
