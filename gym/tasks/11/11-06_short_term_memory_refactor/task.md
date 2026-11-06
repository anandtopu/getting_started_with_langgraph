# 11-06 — Refactor short term memory: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.

## Your task

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

The starter already satisfies the original behavior cases. It fails the separate structural requirement. Keep those original tests green while changing the design; a renamed function alone does not establish the required boundary.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-06
uv run gym check 11-06
uv run gym hint 11-06
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/short-term-memory)
