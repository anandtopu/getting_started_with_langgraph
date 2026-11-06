# Contributing

Use Python 3.12 and start with `uv sync`. Changes should make the course easier to run, predict, or debug. Keep every claim, customer, policy, and service fictional.

## A useful contribution

Describe the learner's problem, the changed behavior, and how you verified it. For a bug, provide the exact command, package versions, and a small synthetic input. Do not include keys, real customer information, or your populated environment file.

Tasks use stable IDs from [the catalog](docs/GYM_TASK_CATALOG.md). Publish a task only when its spec, runnable starter or answer template, tests, three hints, complete solution, and explanation are ready. Update `gym/manifest.json` to make it available. Predict/Trace use JSON answers; Design adds a rubric and a self-review document. Tests must import the selected candidate, not the reference solution.

## Before submitting

```text
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv run python scripts/validate_gym.py
uv run python scripts/run_all_examples.py
uv run python scripts/check_coverage.py
uv run python scripts/check_links.py
uv run python scripts/check_legacy_apis.py
```

Use `--release` on gym/coverage validators only when checking the finished course. Until then, a release failure is expected and must not be hidden. Optional provider, Docker, and hosted-service tests are separate from the offline suite.

To install local hooks:

```text
uv sync --group maintain
uv run --group maintain pre-commit install
uv run --group maintain pre-commit run --all-files
```

## Teaching standards

Introduce jargon before using it. Ask learners to predict a result before revealing it. Examples have type hints, a main function, a script guard, expected output, and an explanation of their cost and safety. Keep a focused example around 120 lines; shared code belongs in common/.

Use the shared model factory. Tier 1 never imports provider integrations. Graded work uses scripted fakes and no network. Concurrency tests check causal order and superstep groups, not arbitrary sibling completion order.

Generate diagrams from compiled graphs where possible. Clear notebook outputs. Document any API substitution and its official source in [verification notes](docs/VERIFICATION_NOTES.md). New features must have six meaningful tasks, not six duplicate tests.

## Data changes

Regenerate fixtures with `uv run python scripts/build_data.py`. Review the data manifest, golden cases, and sample PDF rendering. Fixed seeds and dates make content reproducible. SQLite file headers can vary with the writer version across Python builds; compare logical records as well as file integrity.

## Conduct and licensing

Follow [the code of conduct](CODE_OF_CONDUCT.md). Contributions are made under the repository's [MIT license](LICENSE).
