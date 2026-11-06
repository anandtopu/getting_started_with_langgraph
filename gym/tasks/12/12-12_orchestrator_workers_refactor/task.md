# 12-12 — Refactor orchestrator workers: Run every approved worker in the plan.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

An orchestrator proposes a structured plan, then Send creates one worker invocation per section. Validate allowed section names, uniqueness, and size before fan-out. The reducer accumulates independent reports and a deferred assembler produces a canonical order rather than relying on worker completion timing.

## Your task

Run every approved worker in the plan. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "sections": [
      "coverage",
      "deductible",
      "exclusions"
    ]
  },
  {
    "sections": []
  },
  {
    "sections": [
      "deductible"
    ]
  },
  {
    "sections": [
      "coverage",
      "coverage"
    ]
  },
  {
    "sections": [
      "payments"
    ]
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-12
uv run gym check 12-12
uv run gym hint 12-12
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
