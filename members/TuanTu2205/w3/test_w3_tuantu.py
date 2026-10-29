import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from members.TuanTu2205.w3.dates import parse_due
from members.TuanTu2205.w3.log_stats import analyse

ROOT = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("2026-10-30", date(2026, 10, 30)),
        ("tomorrow", date(2026, 10, 27)),
        ("in 3 days", date(2026, 10, 29)),
        ("Fri", date(2026, 10, 30)),
        ("MON", date(2026, 11, 2)),
    ],
)
def test_parse_due(text: str, expected: date) -> None:
    assert parse_due(text, date(2026, 10, 26)) == expected


def test_next_weekday_not_today() -> None:
    assert parse_due("Fri", date(2026, 10, 30)) == date(
        2026, 11, 6
    )


@pytest.mark.parametrize("text", ["", "yesterday", "2026-02-30"])
def test_parse_due_invalid(text: str) -> None:
    with pytest.raises(ValueError):
        parse_due(text, date(2026, 10, 26))


def test_analyse_counts_and_p95() -> None:
    result = analyse(
        [
            ("fee", 100),
            ("fee", 300),
            ("rule", 900),
            ("rule", 1100),
            ("fee", 200),
        ]
    )
    assert result["counts"] == {"fee": 3, "rule": 2}
    assert result["p95"] == {"fee": 300.0, "rule": 1100.0}
    assert result["slowest"] == "rule"


def test_analyse_empty() -> None:
    assert analyse([]) == {
        "counts": {},
        "p95": {},
        "slowest": None,
    }


def test_analyse_nearest_rank() -> None:
    result = analyse([("api", value) for value in range(1, 21)])
    assert result["p95"]["api"] == 19.0


@pytest.mark.parametrize("latency", [-1, float("nan"), float("inf")])
def test_analyse_invalid_latency(latency: float) -> None:
    with pytest.raises(ValueError):
        analyse([("api", latency)])


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the real CLI in a separate process."""
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "members.TuanTu2205.w3.cli",
            *args,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )


def test_cli_success() -> None:
    csv_path = ROOT / "members/TuanTu2205/w2/sample_tasks.csv"
    result = run_cli(
        str(csv_path),
        "--hours", "2",
        "--today", "2026-10-26",
    )

    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert result.stdout.splitlines() == [
        "Tonight (2.0 h):",
        "  1. Python homework ...... 2 h",
    ]



def test_cli_missing_file(tmp_path: Path) -> None:
    result = run_cli(
        str(tmp_path / "missing.csv"),
        "--hours", "2",
    )

    assert result.returncode == 1
    assert "Error loading tasks:" in result.stderr
    assert "Traceback" not in result.stderr
