# Tier 2 | Add models without losing control

## Model factory

Use common.models.get_chat_model(). Graded runs use scripted responses, temperature zero, no credentials, and no network.

## Message history

Preserve AI tool-call IDs and matching tool responses. Use add_messages for message identity-aware updates.

## Structured output

Validate fields with Pydantic and explicit constraints. Model text cannot grant approval or establish ownership.

## Tools

Expose the smallest capability. Validate arguments and trust runtime context, not a model-supplied customer ID.

## Agent loop

Use create_agent for a standard model/tool loop. Use an explicit graph when routing or authorization must be fixed.

## Middleware

Place limits and hooks at the boundary they control. Bound model calls, tool calls, and recursion separately.

## Memory

Checkpoints retain a thread. Store namespaces retain cross-thread facts. Trim or summarize deliberately; do not erase pending tool pairs.

## RAG

Retrieve evidence, retain source IDs, answer only from support, and abstain when the corpus does not answer the question.

## Practice

Modules 08-12; compare default, missing, malformed, and rejection cases. Checkpoint project: Policy Q&A with Memory.

Verified course API family: 2026-11-06. See docs/VERIFICATION_NOTES.md and the lockfiles.
