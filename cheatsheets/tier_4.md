# Tier 4 | Operate a bounded application

## Streaming

Project public updates and tokens. Keep internal checkpoints private. On reconnect fetch a snapshot; do not duplicate the initial input.

## HTTP boundary

Authenticate each request, verify thread ownership, validate inputs, and recheck the current interrupt inside the execution lease.

## Testing

Test nodes, reducers, graph routes, recovery, and API behavior. Use independent expected answers instead of copying observed outputs blindly.

## Evaluation

Measure routing and tool trajectories. Distinguish strict ordering from acceptable unordered parallel calls.

## Observability

Log allowlisted identifiers, nodes, status, and durations. Tracing is opt-in; credentials and customer text do not belong in logs.

## Security

Treat retrieved documents and model output as untrusted. Use trusted roles, strict schemas, scoped tools, and explicit approvals.

## Persistence

SQLite serves a local single process. Postgres supports shared checkpoints, Store, ownership, leases, and payload-bound effect keys.

## Deployment

Health-check dependencies, close resources on shutdown, preserve durable volumes, and test restoring a paused claim.

## Practice

Modules 18-22; finish the Claims Copilot and Design Your Own capstones. Live providers and hosted deployment are separate checks.

Verified course API family: 2026-11-06. See docs/VERIFICATION_NOTES.md and the lockfiles.
