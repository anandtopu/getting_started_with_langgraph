# Hints

## Hint 1

Inspect the waiting shelf before and after an approval rather than checking only the final receipt. Compare the first differing field with the task's required behavior.

## Hint 2

Read the completed snapshot after resumption. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "pending_after": list(graph.get_state(config).next). Check every boundary input after the repair; a default-case pass alone is insufficient.
