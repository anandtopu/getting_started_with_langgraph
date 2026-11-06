# Hints

## Hint 1

Check the tools in this workshop, not the tools in another building. Compare the first differing field with the task's required behavior.

## Hint 2

A missing provider is a problem only when live mode was requested. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: case["live"] and not case["provider_ready"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
