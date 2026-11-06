# Why the refactor works

Input and output schemas define an API boundary; private channels can still exist inside the graph. Messages are records with roles, text, and IDs. add_messages appends new IDs and replaces an existing ID, so correcting one message need not duplicate it.

Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.

The starter is a working behavioral baseline. The reference changes its design, then runs the same case fixtures and a separate structural check. Inspect both test groups: matching one happy-path output does not prove equivalence. Preserve rejection/error behavior and input ownership as well as successful results.

Run the selected workspace file through gym check. Viewing the reference is recorded as assisted study.
