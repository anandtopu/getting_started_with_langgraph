# 03-18 — Design early exit and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Termination is a routing outcome, not an exceptional Python crash. Screen invalid and duplicate claims before assigning work. The returned state should still explain why a claim ended so an adjuster can inspect it.

## Your task

Design early exit and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "amount_cents": 0,
    "duplicate_of": null
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": -1,
    "duplicate_of": null
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": true,
    "duplicate_of": null
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": 0,
    "duplicate_of": "CLM-0021"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-18
uv run gym check 03-18
uv run gym hint 03-18
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
