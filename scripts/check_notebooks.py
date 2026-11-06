"""Execute every cleared course notebook in a real kernel, retaining outputs only in tmp."""

import argparse

from common.config import ROOT


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=99)
    parser.add_argument("--modules", nargs="+")
    args = parser.parse_args()
    import nbformat
    from nbclient import NotebookClient

    selected = sorted((ROOT / "modules").glob("**/notebook.ipynb"))
    checked = 0
    for path in selected:
        prefix = path.parent.name.split("_")[0]
        if args.modules and prefix not in args.modules:
            continue
        if prefix.isdigit() and int(prefix) > args.through:
            continue
        notebook = nbformat.read(path, as_version=4)
        assert all(
            not cell.get("outputs") and cell.get("execution_count") is None
            for cell in notebook.cells
            if cell.cell_type == "code"
        ), path
        # Block external calls inside the kernel; local kernel IPC remains available.
        notebook.cells.insert(
            0,
            nbformat.v4.new_code_cell(
                "import os, sys\nos.environ['LARKSPUR_OFFLINE'] = '1'\n"
                "from common.offline import block_network, install_socketpair_compatibility\n"
                "install_socketpair_compatibility()\nsys.addaudithook(block_network)"
            ),
        )
        NotebookClient(
            notebook,
            timeout=180,
            kernel_name="python3",
            resources={"metadata": {"path": str(ROOT)}},
        ).execute()
        output = ROOT / "tmp" / "notebooks" / path.relative_to(ROOT / "modules")
        output.parent.mkdir(parents=True, exist_ok=True)
        nbformat.write(notebook, output)
        checked += 1
        print(f"PASS {path.relative_to(ROOT)}", flush=True)
    print(f"Executed {checked} notebooks; committed outputs remain cleared.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
