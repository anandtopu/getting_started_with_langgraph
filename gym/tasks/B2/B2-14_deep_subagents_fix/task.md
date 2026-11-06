# B2-14 — Fix deep subagents: Preserve a human rejection of delegation.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.

## Your task

Preserve a human rejection of delegation. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "decision": "approve",
    "specialist": "policy_expert"
  },
  {
    "decision": "reject",
    "specialist": "policy_expert"
  },
  {
    "decision": "approve",
    "specialist": "missing_specialist"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-14
uv run gym check B2-14
uv run gym hint B2-14
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/subagents)
