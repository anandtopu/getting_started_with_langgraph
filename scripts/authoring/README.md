# Maintaining course exercises

The authored contracts live in the tier modules and `bonuses.py`. They specify normal and boundary cases, independent result checks, four deliberate faults, and design policies. `extensions.py` supplies exercises that add new behavior.

The corresponding `sources/<module>/<example>.py.in` and `.ts.in` templates retain the exact fault anchors. Edit these templates when changing an authored example, then update its contract and fault anchors together. Published examples and gym files are generated and formatted; editing only a published copy will be overwritten on regeneration. The `.in` files are complete programs used as source text, not unfinished learner placeholders. The generated versions are exercised by the ordinary tests and gym validator.

```text
uv run --no-sync python scripts/build_course.py --through 22 --bonuses
uv run --no-sync python scripts/build_capstones.py
uv run --no-sync python scripts/build_reference_docs.py
uv run --no-sync ruff check . --fix
uv run --no-sync ruff format .
uv run --no-sync pytest
uv run --no-sync python scripts/validate_gym.py --release --jobs 4
```

The builder captures behavioral fixtures only after checking independently authored assertions. Review additional cases against the requirement; a captured value is not automatically a correct requirement. The release validator separately proves that every reference passes, each faulty code starter fails for a declared behavioral reason, and each written-answer oracle agrees with actual execution.

The first six setup exercises are hand-authored. Keep their independent acceptance checks and CLI onboarding behavior intact. A Design task's mechanical score does not establish architecture quality; its rationale requires the separate rubric.
