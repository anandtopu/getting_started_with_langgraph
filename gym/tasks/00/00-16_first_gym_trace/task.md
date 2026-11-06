# 00-16 — Diagnose first gym from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

## Your task

Diagnose first gym from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_type": " Water ",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "THEFT",
    "claim_id": "CLM-0001"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Unknown claim categories need an explicit label."
- "Labels need case normalization before comparison."
- "Leading and trailing spaces are not claim categories."
- "The output must retain the input claim identity."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-16
uv run gym check 00-16
uv run gym hint 00-16
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
