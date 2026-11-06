# 21-03 — Predict untrusted input across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.

## Your task

Predict untrusted input across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "extra_authority": false,
    "amount_cents": 600000
  },
  {
    "extra_authority": true,
    "amount_cents": 600000
  },
  {
    "extra_authority": false,
    "amount_cents": 100000
  },
  {
    "extra_authority": false,
    "amount_cents": -1
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-03
uv run gym check 21-03
uv run gym hint 21-03
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/guardrails)
