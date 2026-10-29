"""Black-box tests for the team Week 3 CLI (independent of member W3 CLI)."""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MODULE = "shared.study_planner"
HEADER = "title,importance,effort_h,deadline\n"


def invoke_cli(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", MODULE, *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_runs_complete_pipeline_and_prioritises(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(
        HEADER
        + "DS exam,5,6,2026-10-30\n"
        + "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )
    result = invoke_cli(str(csv_path), "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0, result.stderr
    assert result.stdout == "Assignment: 1.5 hours\nDS exam: 0.5 hours\n"
    assert result.stderr == ""


def test_cli_uses_bundled_sample_without_path():
    result = invoke_cli("--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0, result.stderr
    assert result.stdout == "Review Python: 2 hours\n"
    assert result.stderr == ""


@pytest.mark.parametrize("hours", ["0", "0.0"])
def test_cli_zero_hours_has_no_blocks(tmp_path, hours):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(HEADER + "Task A,5,2,2026-10-30\n", encoding="utf-8")
    result = invoke_cli(str(csv_path), "--hours", hours, "--today", "2026-10-26")
    assert result.returncode == 0
    assert result.stdout == ""
    assert result.stderr == ""


def test_cli_empty_csv_has_no_blocks(tmp_path):
    csv_path = tmp_path / "tasks.csv"
    csv_path.write_text(HEADER, encoding="utf-8")
    result = invoke_cli(str(csv_path), "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0
    assert result.stdout == ""


def test_cli_missing_csv_exits_one(tmp_path):
    result = invoke_cli(str(tmp_path / "missing.csv"), "--hours", "2")
    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "missing.csv" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_invalid_csv_exits_one(tmp_path):
    csv_path = tmp_path / "bad.csv"
    csv_path.write_text(HEADER + "Task A,6,2,2026-10-30\n", encoding="utf-8")
    result = invoke_cli(str(csv_path), "--hours", "2")
    assert result.returncode == 1
    assert "line 2" in result.stderr
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize("hours", ["-1", "nan", "inf", "abc"])
def test_cli_rejects_invalid_hours(hours):
    result = invoke_cli("--hours", hours)
    assert result.returncode == 2
    assert "hours" in result.stderr.lower()


@pytest.mark.parametrize("day", ["2026-02-30", "not-a-date"])
def test_cli_rejects_invalid_today(day):
    result = invoke_cli("--today", day)
    assert result.returncode == 2
    assert "YYYY-MM-DD" in result.stderr


def test_cli_help():
    result = invoke_cli("--help")
    assert result.returncode == 0
    assert "--hours" in result.stdout
    assert "--today" in result.stdout
    assert "CSV" in result.stdout
