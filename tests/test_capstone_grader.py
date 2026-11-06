"""A learner candidate cannot turn skipped acceptance checks into a pass."""

import sys

from common.config import ROOT
from common.process import offline_environment, run_process


def test_skipping_capstone_acceptance_is_not_success(tmp_path):
    candidate = tmp_path / "candidate.py"
    candidate.write_text(
        "import pytest\ndef run(case):\n    pytest.skip('not implemented')\n", encoding="utf-8"
    )
    result = run_process(
        [sys.executable, "scripts/check_capstone.py", "01", "--candidate", str(candidate)],
        cwd=ROOT,
        env=offline_environment(),
    )
    assert result.returncode == 5
    assert "skipped tests do not count" in result.stdout
