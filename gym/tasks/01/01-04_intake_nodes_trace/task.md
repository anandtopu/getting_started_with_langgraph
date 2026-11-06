# 01-04 — Diagnose intake nodes from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

State is the information available to a graph. TypedDict documents its keys. A node is a function that reads state and returns only the keys it changes; the graph merges those updates instead of replacing the whole state.

## Your task

Diagnose intake nodes from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": "125000"
  },
  {
    "claim_id": "CLM-0099",
    "description": "  Pipe burst  ",
    "amount_cents": "250"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Normalize the description while preserving unrelated state."
- "A graph node must return a mapping of state updates."
- "An amount update must not erase the claim identifier."
- "Refactor mutation into a pure partial update."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-04
uv run gym check 01-04
uv run gym hint 01-04
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
