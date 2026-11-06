# 11-04 — Trace short term memory: Use a new message ID for a new turn instead of overwriting the previous turn.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.

## Your task

Use a new message ID for a new turn instead of overwriting the previous turn. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-04
uv run gym check 11-04
uv run gym hint 11-04
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/short-term-memory)
