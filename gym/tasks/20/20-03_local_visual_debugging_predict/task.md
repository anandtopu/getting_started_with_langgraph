# 20-03 — Predict local visual debugging across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

langgraph.json maps a public graph name to a Python export. The local Agent Server hosts that graph; Studio adds a visual client and may require an account. Without Studio, draw_mermaid, updates, and checkpoint snapshots still reveal the route and pause. The export leaves persistence to the server instead of constructing its own competing saver.

## Your task

Predict local visual debugging across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-03
uv run gym check 20-03
uv run gym hint 20-03
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/local-server)
