# 20-02 — Fix local visual debugging: Debug the supplied claim amount rather than a substituted value.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

langgraph.json maps a public graph name to a Python export. The local Agent Server hosts that graph; Studio adds a visual client and may require an account. Without Studio, draw_mermaid, updates, and checkpoint snapshots still reveal the route and pause. The export leaves persistence to the server instead of constructing its own competing saver.

## Your task

Debug the supplied claim amount rather than a substituted value. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "amount_cents": 600000,
    "reported_route": "fast_track"
  },
  {
    "amount_cents": 100000,
    "reported_route": "fast_track"
  },
  {
    "amount_cents": 600000,
    "reported_route": "specialist"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-02
uv run gym check 20-02
uv run gym hint 20-02
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/local-server)
