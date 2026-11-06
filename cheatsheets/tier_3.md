# Tier 3 | Compose and recover

## Subgraphs

Share only intended state fields. Use adapters for private schemas. Choose inherited or independent checkpoint ownership explicitly.

## Multiple agents

Use specialists for distinct contexts or capabilities. A supervisor adds latency and coordination work; compare a single-agent baseline.

## Handoffs

Command.PARENT transfers control to the parent. Preserve matched tool responses and keep state contracts compatible.

## Functional API

entrypoint orchestrates; task saves repeatable work results. Entry code may re-enter while a completed task result is reused.

## External calls

Use timeouts, bounded retries, cancellation cleanup, and a stable idempotency key tied to a canonical payload.

## MCP

Own the client session lifetime. Local stdio needs no network. Keep protocol stdout free of logs and expose read-only tools first.

## Fault recovery

Test a crash after effect commit but before task completion. A checkpoint and an external transaction are separate boundaries.

## Long waits

Persist before waiting; reopen the same thread after restart. Never keep a Python process asleep for days to represent a business wait.

## Practice

Modules 13-17; inject failures at boundaries. Checkpoint project: Fraud Investigation Team.

Verified course API family: 2026-11-06. See docs/VERIFICATION_NOTES.md and the lockfiles.
