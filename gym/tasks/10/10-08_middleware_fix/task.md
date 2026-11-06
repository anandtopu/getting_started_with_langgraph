# 10-08 — Fix middleware: Enforce the independent tool budget.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Middleware hooks surround agent operations. before_model can update declared middleware state; wrap_model_call controls the handler; after_model observes the result. Model and tool budgets are separate: limiting one does not automatically limit the other. Hook order belongs in an explicit test.

## Your task

Enforce the independent tool budget. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "model_limit": 3,
    "tool_limit": 1
  },
  {
    "model_limit": 1,
    "tool_limit": 1
  },
  {
    "model_limit": 3,
    "tool_limit": 0
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 10-08
uv run gym check 10-08
uv run gym hint 10-08
```

## Reading

[Module lesson](../../../../modules/10_prebuilt_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/middleware/overview)
