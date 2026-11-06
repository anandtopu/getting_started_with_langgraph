# Hints

## Hint 1

A specialist sends a signed conclusion back to intake, not the entire scratch notebook. Compare the first differing field with the task's required behavior.

## Hint 2

Map the specialist answer into the parent explanation field. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: return {"explanation": result.value["messages"][-1].content}. Check every boundary input after the repair; a default-case pass alone is insufficient.
