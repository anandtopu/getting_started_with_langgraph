# B1-07 — Build typescript durable: Review every document before the approval step.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

JavaScript Send fans out document work, SqliteSaver retains the approval pause, and Command resumes it. The saver connection is explicitly closed. JavaScript uses camelCase options such as streamMode and returns its documented update shape; this lesson intentionally does not copy Python invocation parameters.

## Your task

Review every document before the approval step. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-07
uv run gym check B1-07
uv run gym hint B1-07
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langgraph/interrupts)
