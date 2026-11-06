# 11-04 — Diagnose short term memory from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.

## Your task

Diagnose short term memory from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "max_messages": 2,
    "second_text": "An estimate is now attached."
  },
  {
    "max_messages": 4,
    "second_text": "An estimate is now attached."
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Bound the messages sent to the model."
- "Use a new message ID for a new turn instead of overwriting the previous turn."
- "Include newly supplied evidence in the summary."
- "Retain the summarization step after responding."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-04
uv run gym check 11-04
uv run gym hint 11-04
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/short-term-memory)
