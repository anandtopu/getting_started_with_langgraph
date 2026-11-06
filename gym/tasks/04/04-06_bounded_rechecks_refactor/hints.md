# Hints

## Hint 1

A clerk can request missing evidence three times; the building's emergency stop is a different control. Compare the first differing field with the task's required behavior.

## Hint 2

Equivalent loops must preserve the exact attempt budget. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: index + 1 >= state["budget"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
