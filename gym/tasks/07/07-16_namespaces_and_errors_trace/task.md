# 07-16 — Trace namespaces and errors: Keep parent and child scopes distinct.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A subgraph namespace identifies nested work. Sibling parallel events can arrive in either order; causal requirements, such as summary after both checks, are stable. A live event trace is not itself the durable checkpoint history.

## Your task

Keep parent and child scopes distinct. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001"
  },
  {
    "claim_id": "CLM-0101"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-16
uv run gym check 07-16
uv run gym hint 07-16
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
