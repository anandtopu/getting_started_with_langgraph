"""Custom workspace locations must still resolve the course's Node dependencies."""

import shutil

import pytest

from common.loading import load_module
from common.optional import missing_for
from gym.catalog import Catalog


@pytest.mark.skipif(missing_for("B1") is not None, reason="Install Node 24 and npm dependencies")
def test_external_workspace_runs_the_selected_typescript_file(tmp_path):
    task = Catalog().get("B1-01")
    candidate = tmp_path / "selected.py"
    shutil.copyfile(task.folder / "solution.py", candidate)
    shutil.copyfile(task.folder / "solution.ts", candidate.with_suffix(".ts"))
    result = load_module(candidate).run(
        {"claim_id": "EXTERNAL", "description": "  Roof damage  ", "amount_cents": 50000}
    )
    assert result["claim_id"] == "EXTERNAL"
    assert result["description"] == "Roof damage" and result["route"] == "fast_track"
