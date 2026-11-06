# B1-12 — Refactor typescript durable: Extract reusable graph construction into buildGraph; keep invocation, saver lifetime, stream counts, and all old behavior unchanged.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

JavaScript Send fans out document work, SqliteSaver retains the approval pause, and Command resumes it. The saver connection is explicitly closed. JavaScript uses camelCase options such as streamMode and returns its documented update shape; this lesson intentionally does not copy Python invocation parameters.

## Your task

Extract reusable graph construction into buildGraph; keep invocation, saver lifetime, stream counts, and all old behavior unchanged. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "documents": [
      "estimate",
      "receipt"
    ],
    "approved": false
  },
  {
    "documents": [],
    "approved": true
  },
  {
    "documents": [
      "police_report"
    ],
    "approved": false
  },
  {
    "documents": [
      "estimate",
      "receipt"
    ],
    "approved": "yes"
  }
]
```

The starter already satisfies the original behavior cases. It fails the separate structural requirement. Keep those original tests green while changing the design; a renamed function alone does not establish the required boundary.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-12
uv run gym check B1-12
uv run gym hint B1-12
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langgraph/interrupts)
