"""End-to-end tests for the shared T-W3 Study Planner CLI.

These tests run the public Python module in a separate process rather than
mocking its parser, prioritiser, allocator, or renderer.
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CSV_HEADER = "title,importance,effort_h,deadline\n"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the public CLI exactly as a user would from the repository root."""
    return subprocess.run(
        [sys.executable, "-m", "shared.study_planner", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )


def write_csv(tmp_path: Path, *rows: str) -> Path:
    """Write a small valid CSV fixture and return its path."""
    path = tmp_path / "tasks.csv"
    path.write_text(CSV_HEADER + "".join(f"{row}\n" for row in rows), encoding="utf-8")
    return path


def test_e2e_prioritises_allocates_and_renders(tmp_path: Path) -> None:
    """The CLI must order by urgency, allocate partially, and render blocks."""
    csv_path = write_csv(
        tmp_path,
        "Later task,4,3,2026-10-30",
        "Urgent task,5,1.5,2026-10-27",
    )
    result = run_cli(str(csv_path), "--hours", "2", "--today", "2026-10-26")

    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout.splitlines() == [
        "Urgent task: 1.5 hours",
        "Later task: 0.5 hours",
    ]


def test_e2e_equal_priority_retains_csv_order(tmp_path: Path) -> None:
    """Two tasks with the same score retain the original CSV order."""
    csv_path = write_csv(
        tmp_path,
        "First,4,1,2026-10-28",
        "Second,2,1,2026-10-27",
    )
    result = run_cli(str(csv_path), "--hours", "3", "--today", "2026-10-26")

    assert result.returncode == 0
    assert result.stdout.splitlines() == [
        "First: 1 hours",
        "Second: 1 hours",
    ]


def test_e2e_zero_hours_produces_no_blocks(tmp_path: Path) -> None:
    """A zero budget succeeds without scheduling any positive-hour blocks."""
    csv_path = write_csv(tmp_path, "Read chapter,5,2,2026-10-27")
    result = run_cli(str(csv_path), "--hours", "0", "--today", "2026-10-26")

    assert result.returncode == 0
    assert result.stdout == ""
    assert result.stderr == ""


def test_e2e_uses_default_sample_csv() -> None:
    """The bundled example should work without an explicit CSV argument."""
    result = run_cli("--hours", "2", "--today", "2026-10-26")

    assert result.returncode == 0
    assert result.stdout == "Review Python: 2 hours\n"
    assert result.stderr == ""


@pytest.mark.parametrize(
    "row",
    [
        "Bad importance,7,2,2026-10-27",
        "Bad effort,5,-2,2026-10-27",
        "Bad deadline,5,2,not-a-date",
    ],
)
def test_e2e_invalid_csv_row_reports_error(tmp_path: Path, row: str) -> None:
    """Invalid input is reported on stderr without a Python traceback."""
    csv_path = write_csv(tmp_path, row)
    result = run_cli(str(csv_path), "--hours", "2", "--today", "2026-10-26")

    assert result.returncode == 1
    assert "line 2" in result.stderr
    assert "Traceback" not in result.stderr
    assert result.stdout == ""


def test_e2e_invalid_header_reports_error(tmp_path: Path) -> None:
    """Missing required CSV columns should fail cleanly."""
    csv_path = tmp_path / "wrong.csv"
    csv_path.write_text("title,importance\nTask,5\n", encoding="utf-8")
    result = run_cli(str(csv_path), "--hours", "2", "--today", "2026-10-26")

    assert result.returncode == 1
    assert "header" in result.stderr.lower()
    assert "Traceback" not in result.stderr


def test_e2e_missing_file_reports_error(tmp_path: Path) -> None:
    """A nonexistent CSV must not produce an unhandled traceback."""
    result = run_cli(str(tmp_path / "missing.csv"), "--hours", "2")

    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize("hours", ["-1", "abc", "nan", "inf"])
def test_e2e_invalid_budget_is_argument_error(tmp_path: Path, hours: str) -> None:
    """Malformed budgets are rejected by argparse with exit status 2."""
    csv_path = write_csv(tmp_path, "Task,5,2,2026-10-27")
    result = run_cli(str(csv_path), "--hours", hours, "--today", "2026-10-26")

    assert result.returncode == 2
    assert "hours" in result.stderr.lower()
    assert "Traceback" not in result.stderr


def test_e2e_invalid_today_is_argument_error(tmp_path: Path) -> None:
    """Malformed dates are rejected by argparse before any planning."""
    csv_path = write_csv(tmp_path, "Task,5,2,2026-10-27")
    result = run_cli(str(csv_path), "--hours", "2", "--today", "2026-02-30")

    assert result.returncode == 2
    assert "today" in result.stderr.lower()
    assert "Traceback" not in result.stderr


def test_e2e_help() -> None:
    """The public CLI documents both study hours and reference date."""
    result = run_cli("--help")

    assert result.returncode == 0
    assert "--hours" in result.stdout
    assert "--today" in result.stdout
    assert result.stderr == ""
