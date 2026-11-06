# 11-09 — Predict store namespaces across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The Store holds cross-thread memories under tuple namespaces. Semantic memory stores facts, episodic memory stores events, and procedural memory stores instructions; these are application conventions rather than special database types. Customer-scoped namespaces must be enforced from trusted context. Deleting a memory is an explicit operation.

## Your task

Predict store namespaces across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "customer_id": "CUS-0001",
    "preference": "email"
  },
  {
    "customer_id": "CUS-0033",
    "preference": "sms"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-09
uv run gym check 11-09
uv run gym hint 11-09
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/stores)
