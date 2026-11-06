# 08-04 — Trace model boundary: Include exactly 100000 cents in fast-track routing.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A model predicts text from messages; a prompt is its instruction and evidence. Structured output parses that text into a validated schema. Validation can reject an impossible amount, but cannot prove a claim is true. The deterministic router owns the decision after extraction.

## Your task

Include exactly 100000 cents in fast-track routing. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-04
uv run gym check 08-04
uv run gym hint 08-04
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/models)
