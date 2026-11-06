# Why the refactor works

A supervisor may call specialists as tools. Each specialist gets a narrow evidence prompt and a private message history; the supervisor receives only the returned conclusion. This direct create_agent pattern avoids an extra helper package. More agents add calls and failure boundaries, so compare them against a single-agent baseline.

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.

The starter is a working behavioral baseline. The reference changes its design, then runs the same case fixtures and a separate structural check. Inspect both test groups: matching one happy-path output does not prove equivalence. Preserve rejection/error behavior and input ownership as well as successful results.

Run the selected workspace file through gym check. Viewing the reference is recorded as assisted study.
