"""Content gates must detect broken examples and documentation, not just exist."""

import re
from collections import namedtuple
from io import StringIO

from rich.console import Console

from common.config import ROOT
from common.pretty import print_checkpoint
from scripts.check_legacy_apis import prohibited_patterns, scan
from scripts.check_links import check_links


def test_repository_links_and_legacy_patterns():
    assert scan() == []
    count, errors = check_links()
    assert count > 100
    assert errors == []


def test_scanner_rejects_banned_code(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "MIGRATING_FROM_OLDER_VERSIONS.md").write_text(
        (ROOT / "docs/MIGRATING_FROM_OLDER_VERSIONS.md").read_text("utf-8"), encoding="utf-8"
    )
    (tmp_path / "example.py").write_text(prohibited_patterns()[0], encoding="utf-8")
    assert len(scan(tmp_path)) == 1


def test_link_checker_detects_missing_file_and_anchor(tmp_path):
    (tmp_path / "README.md").write_text(
        "# Overview\n[bad](missing.md)\n[bad anchor](#absent)\n[good](#overview)\n",
        encoding="utf-8",
    )
    count, errors = check_links(tmp_path)
    assert count == 3
    assert len(errors) == 2


def test_printing_redacts_nested_checkpoint_credentials():
    snapshot = namedtuple("Snapshot", ["values", "config"])
    output = StringIO()
    print_checkpoint(
        snapshot({"claim": "synthetic"}, {"nested": [{"OPENAI_API_KEY": "private-value"}]}),
        console=Console(file=output, force_terminal=False),
    )
    assert "private-value" not in output.getvalue()
    assert "[REDACTED]" in output.getvalue()
    assert "synthetic" in output.getvalue()


def test_migration_debugging_example_runs(capsys):
    document = (ROOT / "docs/MIGRATING_FROM_OLDER_VERSIONS.md").read_text("utf-8")
    examples = re.findall(r"\x60{3}python\n(.*?)\x60{3}", document, re.DOTALL)
    assert len(examples) == 1
    exec(compile(examples[0], "migration-example", "exec"), {"__name__": "__main__"})
    assert "validated" in capsys.readouterr().out
