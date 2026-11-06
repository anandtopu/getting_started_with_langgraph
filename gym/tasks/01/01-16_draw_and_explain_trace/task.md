# 01-16 — Diagnose draw and explain from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A generated diagram shows the compiled edges rather than a hand-drawn guess. In a sequential graph each node runs in a later superstep, a batch of work that sees the previous batch's committed updates. Updates reveal which node actually ran.

## Your task

Diagnose draw and explain from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "The diagram must include validation on the executed route."
- "The intended final node must be connected."
- "Eligibility evidence must affect the validation result."
- "The final update must reflect earlier state."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 01-16
uv run gym check 01-16
uv run gym hint 01-16
```

## Reading

[Module lesson](../../../../modules/01_your_first_graph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
