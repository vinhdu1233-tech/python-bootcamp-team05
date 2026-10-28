
"""Error-handling tests for Member 3, Week 3."""

import subprocess
import sys


def run_cli(*args):
    """Run the shared Study Planner CLI."""
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            *map(str, args),
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def test_missing_file(tmp_path):
    path = tmp_path / "missing.csv"

    result = run_cli(path, "--hours", "2")

    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr


def test_empty_file(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text("", encoding="utf-8")

    result = run_cli(path, "--hours", "2")

    assert result.returncode == 1
    assert "CSV file is empty" in result.stderr
    assert "Traceback" not in result.stderr


def test_infeasible_plan(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Python,5,4,2026-10-30\n"
        "Math,4,3,2026-10-31\n",
        encoding="utf-8",
    )

    result = run_cli(
        path,
        "--hours", "2",
        "--today", "2026-10-28",
        "--require-complete",
    )

    assert result.returncode == 1
    assert "Not enough study time" in result.stderr
    assert "Traceback" not in result.stderr


def test_partial_allocation_still_works(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Python,5,4,2026-10-30\n",
        encoding="utf-8",
    )

    result = run_cli(
        path,
        "--hours", "2",
        "--today", "2026-10-28",
    )

    assert result.returncode == 0
    assert "Python: 2 hours" in result.stdout
    assert result.stderr == ""
