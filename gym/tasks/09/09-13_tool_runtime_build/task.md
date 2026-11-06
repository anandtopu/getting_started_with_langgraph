# 09-13 — Build tool runtime: Write only in the trusted customer namespace.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

ToolRuntime injects trusted context, graph state, the Store, and tool_call_id without exposing them as model-selectable fields. A tool returning Command can update graph state and acknowledge its own request. Customer identity belongs in authenticated context, not in an argument the model invents.

## Your task

Write only in the trusted customer namespace. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "customer_id": "CUS-0001",
    "preference": "email"
  },
  {
    "customer_id": "CUS-0020",
    "preference": "sms"
  },
  {
    "customer_id": "CUS-0001",
    "preference": "fax"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-13
uv run gym check 09-13
uv run gym hint 09-13
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/tools)
