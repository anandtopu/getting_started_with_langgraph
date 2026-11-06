# B2-01 — Build deep agent planning: Install the explicit planning middleware when requested.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.

## Your task

Install the explicit planning middleware when requested. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "first_status": "in_progress",
    "include_planning": true
  },
  {
    "first_status": "completed",
    "include_planning": true
  },
  {
    "first_status": "in_progress",
    "include_planning": false
  },
  {
    "first_status": "invalid",
    "include_planning": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-01
uv run gym check B2-01
uv run gym hint B2-01
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/overview)
