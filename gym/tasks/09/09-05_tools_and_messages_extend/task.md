# 09-05 — Extend tools and messages: Cap the proposal at the synthetic coverage limit.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A tool's typed parameters become a schema the model can request. ToolNode runs the requested function and returns a ToolMessage with the original call ID. Expected lookup failures become error messages when error handling is enabled. A payout calculator proposes cents; it does not transfer money.

## Your task

Cap the proposal at the synthetic coverage limit. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001",
    "amount_cents": 125000
  },
  {
    "policy_id": "MISSING",
    "amount_cents": 125000
  },
  {
    "policy_id": "POL-0001",
    "amount_cents": 0
  },
  {
    "policy_id": "POL-0001",
    "amount_cents": 500000
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-05
uv run gym check 09-05
uv run gym hint 09-05
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/tools)
