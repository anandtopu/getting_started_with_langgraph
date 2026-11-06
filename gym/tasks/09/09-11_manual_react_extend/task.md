# 09-11 — Extend manual react: Respect the caller's execution budget.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A manual agent loop alternates a model node and ToolNode. tools_condition checks the newest AI message: tool calls continue the loop, a final answer ends it. A recursion budget catches nontermination, but does not authorize tool effects or guarantee a useful answer.

## Your task

Respect the caller's execution budget. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001",
    "recursion_limit": 12
  },
  {
    "policy_id": "MISSING",
    "recursion_limit": 12
  },
  {
    "policy_id": "POL-0001",
    "recursion_limit": 1
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-11
uv run gym check 09-11
uv run gym hint 09-11
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
