# B3-07 — Build mini reducers: Install the mini-runner reducer when parallel accumulation is required.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An overwrite channel accepts one update per superstep; multiple writers need a reducer. This comparison runs the same policy and estimate findings in the mini runner and real LangGraph, normalizing their different exception classes to one conflict observation. Canonical output order is separate from the algebra used to merge writes.

## Your task

Install the mini-runner reducer when parallel accumulation is required. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "use_reducer": true
  },
  {
    "use_reducer": false
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-07
uv run gym check B3-07
uv run gym hint B3-07
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
