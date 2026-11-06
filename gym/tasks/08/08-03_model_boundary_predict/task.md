# 08-03 — Predict model boundary across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A model predicts text from messages; a prompt is its instruction and evidence. Structured output parses that text into a validated schema. Validation can reject an impossible amount, but cannot prove a claim is true. The deterministic router owns the decision after extraction.

## Your task

Predict model boundary across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "claim_type": "water",
    "amount_cents": 125000,
    "confidence": 0.7
  },
  {
    "claim_type": "unknown",
    "amount_cents": 125000,
    "confidence": 0.9
  },
  {
    "claim_type": "water",
    "amount_cents": true,
    "confidence": 0.9
  },
  {
    "claim_type": "water",
    "amount_cents": 125000,
    "confidence": 2
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-03
uv run gym check 08-03
uv run gym hint 08-03
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/models)
