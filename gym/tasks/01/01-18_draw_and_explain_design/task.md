# 01-18 — Design draw and explain and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A generated diagram shows the compiled edges rather than a hand-drawn guess. In a sequential graph each node runs in a later superstep, a batch of work that sees the previous batch's committed updates. Updates reveal which node actually ran.

## Your task

Design draw and explain and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "Pipe burst"
  },
  {
    "claim_id": "CLM-0001",
    "description": ""
  },
  {
    "claim_id": "CLM-0042",
    "description": " stolen watch "
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-18
uv run gym check 01-18
uv run gym hint 01-18
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
