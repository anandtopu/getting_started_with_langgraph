# 21-18 — Refactor private checkpoints: Check exact restoration after successful authenticated decryption.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.

## Your task

Check exact restoration after successful authenticated decryption. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "note": "Synthetic customer phone 555-0100",
    "delete": true,
    "wrong_key": false
  },
  {
    "note": "Synthetic customer phone 555-0100",
    "delete": false,
    "wrong_key": false
  },
  {
    "note": "Synthetic customer phone 555-0100",
    "delete": true,
    "wrong_key": true
  },
  {
    "note": "Another synthetic private note",
    "delete": true,
    "wrong_key": false
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-18
uv run gym check 21-18
uv run gym hint 21-18
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
