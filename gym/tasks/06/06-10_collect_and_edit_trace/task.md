# 06-10 — Diagnose collect and edit from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.

## Your task

Diagnose collect and edit from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "loss_date": "2026-01-01",
    "approved_cents": 125000
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": 0
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "A zero approved amount is a valid edited decision."
- "Each interrupt must receive the response for its own request kind."
- "Python booleans must not pass an integer money check."
- "Date input must be validated before becoming graph state."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-10
uv run gym check 06-10
uv run gym hint 06-10
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
