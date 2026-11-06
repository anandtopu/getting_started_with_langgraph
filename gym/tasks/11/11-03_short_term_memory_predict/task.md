# 11-03 — Predict short term memory across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.

## Your task

Predict short term memory across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "max_messages": 2,
    "second_text": "A contractor supplied photos."
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-03
uv run gym check 11-03
uv run gym hint 11-03
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/short-term-memory)
