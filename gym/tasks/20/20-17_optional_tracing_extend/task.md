# 20-17 — Extend optional tracing: Keep the original route distinct from the corrected branch.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.

## Your task

Keep the original route distinct from the corrected branch. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-17
uv run gym check 20-17
uv run gym hint 20-17
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/langsmith/observability)
