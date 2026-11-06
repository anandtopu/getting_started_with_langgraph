# B1-18 — Refactor typescript agents: Register the same evidence tool in the prebuilt implementation.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

The TypeScript model factory returns a scripted LangChain fake with tool calls. A manual StateGraph loop and createAgent consume the same trajectory, making their roles and call identities directly comparable. The Python gym bridge executes the selected TypeScript file in Node; it never supplies the business answer itself.

## Your task

Register the same evidence tool in the prebuilt implementation. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001",
    "recursion_limit": 12
  },
  {
    "policy_id": "POL-0001",
    "recursion_limit": 1
  },
  {
    "policy_id": "MISSING",
    "recursion_limit": 12
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-18
uv run gym check B1-18
uv run gym hint B1-18
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langchain/agents)
