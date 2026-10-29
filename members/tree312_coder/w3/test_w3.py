
"""Tests for tree312-coder's Week 3 exercises."""

from datetime import date

import pytest

from members.tree312_coder.w3.cli import main
from members.tree312_coder.w3.dates import parse_due
from members.tree312_coder.w3.log_stats import analyse


def test_iso_date():
    today = date(2026, 10, 26)
    assert parse_due("2026-10-30", today) == date(2026, 10, 30)


def test_tomorrow():
    today = date(2026, 10, 26)
    assert parse_due("tomorrow", today) == date(2026, 10, 27)


def test_in_three_days():
    today = date(2026, 10, 26)
    assert parse_due("in 3 days", today) == date(2026, 10, 29)


def test_next_friday():
    today = date(2026, 10, 26)
    assert parse_due("Fri", today) == date(2026, 10, 30)


def test_invalid_date():
    with pytest.raises(ValueError):
        parse_due("invalid", date(2026, 10, 26))


def test_log_analysis():
    pairs = [
        ("/login", 100),
        ("/login", 200),
        ("/home", 50),
    ]

    result = analyse(pairs)

    assert result["counts"]["/login"] == 2
    assert result["p95"]["/login"] == 200
    assert result["slowest"] == "/login"


def test_empty_log():
    result = analyse([])
    assert result["counts"] == {}
    assert result["slowest"] is None


def test_invalid_latency():
    with pytest.raises(ValueError):
        analyse([("/login", float("nan"))])


def test_cli_missing_file(capsys, tmp_path):
    missing = tmp_path / "missing.csv"

    code = main([str(missing), "--hours", "2"])

    assert code == 1
    assert "Error:" in capsys.readouterr().err


def test_cli_success(capsys, tmp_path):
    csv_file = tmp_path / "tasks.csv"

    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Assignment,5,1.5,2026-10-27\n"
        "Exam,4,3,2026-10-30\n",
        encoding="utf-8",
    )

    code = main([
        str(csv_file),
        "--hours", "2",
        "--today", "2026-10-26",
    ])

    output = capsys.readouterr().out

    assert code == 0
    assert "Assignment" in output
    assert "Exam" in output
    assert "0.5 h" in output
