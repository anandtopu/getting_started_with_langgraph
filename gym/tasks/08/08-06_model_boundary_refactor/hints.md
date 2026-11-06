# Hints

## Hint 1

An intake clerk transcribes a form; a separate rulebook decides which desk receives it. Compare the first differing field with the task's required behavior.

## Hint 2

Preserve the validated amount across the model boundary. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: return {"facts": facts.model_dump()}. Check every boundary input after the repair; a default-case pass alone is insufficient.
