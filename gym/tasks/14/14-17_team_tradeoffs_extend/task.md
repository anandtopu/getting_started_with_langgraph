# 14-17 — Extend team tradeoffs: Count every specialist operation against the budget.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A swarm-style team routes according to the active specialist, without requiring a central supervisor on every transition. Its business budget is distinct from the graph recursion limit. This controlled four-role comparison measures calls and completion; scripted answers do not establish that the team is smarter than the one-call baseline.

## Your task

Count every specialist operation against the budget. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "budget": 4,
    "start_agent": "intake"
  },
  {
    "budget": 2,
    "start_agent": "intake"
  },
  {
    "budget": 0,
    "start_agent": "intake"
  },
  {
    "budget": 4,
    "start_agent": "fraud"
  },
  {
    "budget": -1,
    "start_agent": "intake"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-17
uv run gym check 14-17
uv run gym hint 14-17
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent)
