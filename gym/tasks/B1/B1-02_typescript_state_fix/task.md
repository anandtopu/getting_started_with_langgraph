# B1-02 — Fix typescript state: Preserve Python's inclusive fast-track boundary.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

TypeScript adds static types to JavaScript; StateSchema uses Zod schemas for graph state and ReducedValue declares merges. Nodes return partial objects, await obtains a Promise result, and integer cents preserve Python parity. The JavaScript API returns state directly here; do not assume Python's v2 result wrapper exists in another language.

## Your task

Preserve Python's inclusive fast-track boundary. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": 125000
  },
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": 100000
  },
  {
    "claim_id": "CLM-0001",
    "description": " ",
    "amount_cents": 125000
  },
  {
    "claim_id": "CLM-0001",
    "description": "  Pipe burst  ",
    "amount_cents": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-02
uv run gym check B1-02
uv run gym hint B1-02
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langgraph/overview)
