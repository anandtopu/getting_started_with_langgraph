# Hints

## Hint 1

A rejected form still receives a reason stamp before leaving the queue. Compare the first differing field with the task's required behavior.

## Hint 2

Rejected claims must stop before assignment. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "assign" if state["reason"] == "eligible" else END. Check every boundary input after the repair; a default-case pass alone is insufficient.
