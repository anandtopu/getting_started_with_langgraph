# Hints

## Hint 1

Open the service counter only after the archive is ready, then open the waiting room. Compare the first differing field with the task's required behavior.

## Hint 2

Reject a database without a readiness check. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: if "healthcheck" not in services["postgres"]:. Check every boundary input after the repair; a default-case pass alone is insufficient.
