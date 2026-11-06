# 08-02 — Fix model boundary: Include exactly 100000 cents in fast-track routing.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A model predicts text from messages; a prompt is its instruction and evidence. Structured output parses that text into a validated schema. Validation can reject an impossible amount, but cannot prove a claim is true. The deterministic router owns the decision after extraction.

## Your task

Include exactly 100000 cents in fast-track routing. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-02
uv run gym check 08-02
uv run gym hint 08-02
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/models)
