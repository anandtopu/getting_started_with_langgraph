# Tier 1 | Predict graph execution

## State and updates

Nodes read state and return only changed fields. TypedDict describes shape; it does not enforce input validity at runtime.

## Reducers

Use Annotated[field_type, reducer] for accumulation. Parallel overwrite writes conflict. Test associativity and boundary cases.

## Routing

Use conditional edges for a pure destination decision, Command for update plus routing, and Send for per-item work.

## Supersteps

Siblings read the same previous snapshot. Merge their writes before downstream nodes run. Add an explicit loop exit.

## Persistence

Compile with a saver. Invoke with configurable.thread_id. SQLite contexts must close before reopening on Windows.

## Approval

Call interrupt(request). Resume the same thread with Command(resume=answer). Validate the answer; the node restarts.

## Replay

Inspect get_state and get_state_history. Fork a checkpoint deliberately. External effects need independent idempotency.

## Read output

invoke(..., version='v2') returns GraphOutput: use .value and .interrupts. Stream parts contain type, ns, data.

## Practice

Modules 00-07; guided tasks end in 01, 02, 09, 10, 17, 18. Checkpoint project: Claims Intake Engine.

Verified course API family: 2026-11-06. See docs/VERIFICATION_NOTES.md and the lockfiles.
