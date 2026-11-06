# 21-06 — Refactor untrusted input: Keep model-visible tool capabilities read-only.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.

## Your task

Keep model-visible tool capabilities read-only. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-06
uv run gym check 21-06
uv run gym hint 21-06
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/guardrails)
