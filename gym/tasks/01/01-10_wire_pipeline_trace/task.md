# 01-10 — Trace wire pipeline: Validation must occur before acknowledging the claim.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Edges declare which node can run next. START is the entry point and END marks termination. compile checks the graph and creates an executable object. Explicit v2 invoke returns GraphOutput; its value is the final state.

## Your task

Validation must occur before acknowledging the claim. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": " Water leak ",
    "steps": []
  },
  {
    "claim_id": "CLM-0001",
    "description": " ",
    "steps": []
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-10
uv run gym check 01-10
uv run gym hint 01-10
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
