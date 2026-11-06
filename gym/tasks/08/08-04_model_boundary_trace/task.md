# 08-04 — Diagnose model boundary from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A model predicts text from messages; a prompt is its instruction and evidence. Structured output parses that text into a validated schema. Validation can reject an impossible amount, but cannot prove a claim is true. The deterministic router owns the decision after extraction.

## Your task

Diagnose model boundary from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_type": "water",
    "amount_cents": 125000,
    "confidence": 0.9
  },
  {
    "claim_type": "water",
    "amount_cents": 100000,
    "confidence": 0.9
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Send uncertain extractions to review."
- "Include exactly 100000 cents in fast-track routing."
- "Route an unknown category to review even with high confidence."
- "Preserve the validated amount across the model boundary."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-04
uv run gym check 08-04
uv run gym hint 08-04
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/models)
