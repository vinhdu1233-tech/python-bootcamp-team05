"""Focused tests for Member 1's Week 3 individual exercises."""

import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from members.vinhdu1233_tech.w3.dates import parse_due
from members.vinhdu1233_tech.w3.log_stats import analyse

ROOT = Path(__file__).resolve().parents[3]
TODAY = date(2026, 10, 6)  # Tuesday


def test_dates_from_instructor_examples() -> None:
    """Check all documented Week 3 date formats."""
    assert parse_due("2026-10-30", TODAY) == date(2026, 10, 30)
    assert parse_due("tomorrow", TODAY) == date(2026, 10, 7)
    assert parse_due("in 3 days", TODAY) == date(2026, 10, 9)
    assert parse_due("Fri", TODAY) == date(2026, 10, 9)
    assert parse_due("Tue", TODAY) == date(2026, 10, 13)


@pytest.mark.parametrize("invalid", ["someday", "2026-02-30", "in -2 days"])
def test_dates_reject_invalid_input(invalid: str) -> None:
    """Unknown, malformed and impossible dates are errors."""
    with pytest.raises(ValueError):
        parse_due(invalid, TODAY)


def test_dates_same_weekday_is_next_week() -> None:
    """A named weekday never resolves to today."""
    assert parse_due("tuesday", TODAY) == date(2026, 10, 13)
    assert parse_due("IN 1 DAY", TODAY) == date(2026, 10, 7)


def test_route_statistics_instructor_example() -> None:
    """Verify the counts and upper percentile from Chapter 18.7."""
    pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    result = analyse(pairs)
    assert result["counts"] == {"fee": 3, "rag": 2}
    assert result["p95"] == {"fee": 300, "rag": 1100}
    assert result["slowest"] == "rag"


def test_route_statistics_empty() -> None:
    """No traffic means no identifiable slowest route."""
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}


def test_route_statistics_tied_p95() -> None:
    """Alphabetical tie-breaking makes the result deterministic."""
    assert analyse([("z", 10), ("a", 10)])["slowest"] == "a"


@pytest.mark.parametrize("latency", [-1.0, float("nan"), float("inf")])
def test_route_statistics_reject_invalid_latency(latency: float) -> None:
    """Bad latency values should not silently corrupt the p95."""
    with pytest.raises(ValueError):
        analyse([("fee", latency)])


def _run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Execute the public command from the repository root."""
    return subprocess.run(
        [sys.executable, "-m", "members.vinhdu1233_tech.w3.cli", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_allocates_sample_from_week2() -> None:
    """The CLI reuses the already-committed individual Week 2 CSV."""
    sample = ROOT / "members/vinhdu1233_tech/w2/sample_tasks.csv"
    result = _run_cli(str(sample), "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0, result.stderr
    assert "Tonight (2.0 h):" in result.stdout
    assert "Assignment" in result.stdout
    assert "DS exam" in result.stdout


def test_cli_missing_file_is_exit_one() -> None:
    """The homework specifically requires exit status one for missing CSV."""
    result = _run_cli("missing.csv", "--hours", "2")
    assert result.returncode == 1
    assert "Error loading tasks:" in result.stderr


def test_cli_rejects_bad_date() -> None:
    """Invalid --today never causes an unhandled traceback."""
    sample = ROOT / "members/vinhdu1233_tech/w2/sample_tasks.csv"
    result = _run_cli(str(sample), "--hours", "2", "--today", "2026-02-30")
    assert result.returncode == 1
    assert "--today" in result.stderr


def test_cli_rejects_negative_hours() -> None:
    """argparse stops invalid time budgets before file access."""
    result = _run_cli("missing.csv", "--hours", "-1")
    assert result.returncode == 2
    assert "nonnegative" in result.stderr
