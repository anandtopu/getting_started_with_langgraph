"""Reject prohibited teaching patterns outside the explicit migration document."""

import json
import re
from pathlib import Path

from common.data import ROOT
from common.files import source_files


def prohibited_patterns(root: Path = ROOT) -> list[str]:
    document = (root / "docs/MIGRATING_FROM_OLDER_VERSIONS.md").read_text("utf-8")
    registry = re.search(
        r"<!-- legacy-scan-registry -->\s*\x60{3}json\s*(.*?)\x60{3}", document, re.DOTALL
    )
    if registry is None:
        raise ValueError("The migration document is missing its scanner registry.")
    return json.loads(registry.group(1))


def scan(root: Path = ROOT) -> list[str]:
    patterns = prohibited_patterns(root)
    errors = []
    for path in source_files(root):
        relative = path.relative_to(root).as_posix()
        if relative == "docs/MIGRATING_FROM_OLDER_VERSIONS.md" or relative.startswith(
            "docs/verification/"
        ):
            continue
        if path.suffix not in {".py", ".md", ".ipynb", ".ts", ".yaml", ".yml", ".toml"}:
            continue
        for line_number, line in enumerate(path.read_text("utf-8-sig").splitlines(), 1):
            for pattern in patterns:
                if re.search(r"(?<!\w)" + re.escape(pattern) + r"(?!\w)", line):
                    errors.append(
                        f"{relative}:{line_number}: prohibited teaching pattern from migration registry"
                    )
    return errors


def main() -> int:
    errors = scan()
    for error in errors:
        print(error)
    print(f"Legacy API scan: {len(errors)} problems.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
