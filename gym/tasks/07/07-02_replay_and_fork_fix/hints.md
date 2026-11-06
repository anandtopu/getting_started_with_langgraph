# Hints

## Hint 1

Copy the case file at a chosen revision, attach corrected evidence, and send the copy through review. Compare the first differing field with the task's required behavior.

## Hint 2

Replay the new fork configuration, not its uncorrected parent. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: graph.invoke(None, fork_config, version="v2"). Check every boundary input after the repair; a default-case pass alone is insufficient.
