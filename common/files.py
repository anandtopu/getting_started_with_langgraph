"""Walk course sources without traversing virtual environments or learner attempts."""

import os
from collections.abc import Iterator
from pathlib import Path

IGNORED = {
    ".git",
    ".venv",
    "workspace",
    "tmp",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    "dist",
    "build",
    ".hypothesis",
}


def source_files(root: Path) -> Iterator[Path]:
    for directory, names, files in os.walk(root):
        names[:] = sorted(
            name
            for name in names
            if name not in IGNORED and not (Path(directory) / name).is_symlink()
        )
        for name in sorted(files):
            path = Path(directory) / name
            if not path.is_symlink():
                yield path
