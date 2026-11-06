# 05-02 — Fix thread identity: A persisted invocation needs an explicit thread identifier.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpointer saves graph state under a thread ID. New input on that thread starts another run against its saved state. Resuming a pending operation is different: use the saved continuation or an interrupt response rather than pretending it is a new claim.

## Your task

A persisted invocation needs an explicit thread identifier. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "first_id": "CLM-0001",
    "second_id": "CLM-0002"
  },
  {
    "first_id": "CLM-A",
    "second_id": "CLM-B"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-02
uv run gym check 05-02
uv run gym hint 05-02
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
