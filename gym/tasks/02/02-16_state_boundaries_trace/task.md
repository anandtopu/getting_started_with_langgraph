# 02-16 — Diagnose state boundaries from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Input and output schemas define an API boundary; private channels can still exist inside the graph. Messages are records with roles, text, and IDs. add_messages appends new IDs and replaces an existing ID, so correcting one message need not duplicate it.

## Your task

Diagnose state boundaries from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "text": "  Pipe burst  "
  },
  {
    "claim_id": "CLM-0022",
    "text": " theft "
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Internal channels must not become public output."
- "Use the same message ID to replace the original message."
- "Customer-facing correction must normalize text."
- "A refactored input boundary must still supply the fields its nodes read."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-16
uv run gym check 02-16
uv run gym hint 02-16
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
