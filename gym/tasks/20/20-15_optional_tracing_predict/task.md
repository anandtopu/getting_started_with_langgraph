# 20-15 — Predict optional tracing across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.

## Your task

Predict optional tracing across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "corrected_cents": 50000
  },
  {
    "corrected_cents": 600000
  },
  {
    "corrected_cents": 100001
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-15
uv run gym check 20-15
uv run gym hint 20-15
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/langsmith/observability)
