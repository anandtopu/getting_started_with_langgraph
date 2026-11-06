# Hints

## Hint 1

A form template, a filled form object, and a clerk checking the form are different services. Compare the first differing field with the task's required behavior.

## Hint 2

Use Pydantic field access or model_dump instead of losing validated values. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: return state.model_dump(). Check every boundary input after the repair; a default-case pass alone is insufficient.
