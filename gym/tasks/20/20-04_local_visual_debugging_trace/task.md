# 20-04 — Diagnose local visual debugging from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

langgraph.json maps a public graph name to a Python export. The local Agent Server hosts that graph; Studio adds a visual client and may require an account. Without Studio, draw_mermaid, updates, and checkpoint snapshots still reveal the route and pause. The export leaves persistence to the server instead of constructing its own competing saver.

## Your task

Diagnose local visual debugging from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Resolve the graph name declared in the server configuration."
- "Debug the supplied claim amount rather than a substituted value."
- "Report a discrepancy only when observed and reported routes differ."
- "Inspect the actual approval node in the generated graph diagram."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-04
uv run gym check 20-04
uv run gym hint 20-04
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/local-server)
