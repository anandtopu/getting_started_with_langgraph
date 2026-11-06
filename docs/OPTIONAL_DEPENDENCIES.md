# Install only the lessons you need

`uv sync` installs the core offline course and test tools. It needs network access for an uncached first download. After installation, the gym and tests block external connections and use deterministic fake models.

| Lessons | Installation |
| --- | --- |
| 00–15, 17, 20; capstones 01, 02, 05 | `uv sync` |
| 16 and capstone 03 | `uv sync --extra mcp` |
| 18, 22 and capstone 04 | `uv sync --extra apps` |
| 19 trajectory evaluation | `uv sync --extra eval` |
| 21 app security and encryption | `uv sync --extra apps --extra security` |
| B1 TypeScript | Install Node.js 24, then `npm ci` |
| B2 deep agents | `uv sync --extra bonus` |
| B3 and B4 | `uv sync` |
| Notebooks | Add `--extra notebooks` |
| Postgres | Add `--extra persistence` |
| Local Agent Server | Add `--extra deploy` |

Extras are cumulative in one command. For example, `uv sync --extra mcp --extra apps --extra notebooks` installs all three. Afterward, use `uv run --no-sync python ...` and `uv run --no-sync gym ...` to retain that exact environment. A later plain `uv sync` may remove optional packages.

For the complete maintainer validation environment:

```text
uv sync --locked --all-extras --group maintain
npm ci
uv run --no-sync pytest
uv run --no-sync python scripts/validate_gym.py --release --jobs 4
uv run --no-sync python scripts/check_notebooks.py
npm run typecheck
```

Base tests explicitly skip optional integrations and report why. The release validator refuses to count missing optional dependencies as a pass. No provider keys are needed even in the complete environment. Optional live-model experiments require a separate explicit `--live` command and can incur charges.

The TypeScript SQLite package has a native dependency. The lockfile records its approved install script; if your npm version asks, approve only the pinned `better-sqlite3` package after inspecting its package metadata. A C++ build toolchain is needed only if a compatible prebuilt binary is unavailable.
