"""Load a learner-selected script without importing a reference solution."""

import importlib.util
import sys
import uuid
from pathlib import Path
from types import ModuleType


def load_module(path: Path) -> ModuleType:
    name = "larkspur_attempt_" + uuid.uuid4().hex
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load the selected Python attempt.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module
