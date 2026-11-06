# 10-10 — Trace middleware: Enforce the independent tool budget.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Middleware hooks surround agent operations. before_model can update declared middleware state; wrap_model_call controls the handler; after_model observes the result. Model and tool budgets are separate: limiting one does not automatically limit the other. Hook order belongs in an explicit test.

## Your task

Enforce the independent tool budget. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 10-10
uv run gym check 10-10
uv run gym hint 10-10
```

## Reading

[Module lesson](../../../../modules/10_prebuilt_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/middleware/overview)
