
"""Tests for the Week 3 study planner CLI."""

import pytest

from members.dmdung2520.w3.cli import main


def create_tasks_csv(tmp_path):
    """Create a valid sample task CSV file."""
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Review Python,5,2,2026-10-30\n"
        "Practice algorithms,3,1,2026-11-04\n",
        encoding="utf-8",
    )
    return csv_file


def test_cli_prints_a_study_plan(tmp_path, capsys):
    csv_file = create_tasks_csv(tmp_path)

    exit_code = main(
        [
            str(csv_file),
            "--hours",
            "2",
            "--today",
            "2026-10-26",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Review Python: 2 hours" in captured.out
    assert captured.err == ""


def test_cli_missing_file_returns_one(tmp_path, capsys):
    missing_file = tmp_path / "missing.csv"

    exit_code = main(
        [
            str(missing_file),
            "--hours",
            "2",
            "--today",
            "2026-10-26",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 1
    assert f"CSV file not found: {missing_file}" in captured.err


def test_cli_invalid_csv_returns_one(tmp_path, capsys):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text("wrong,header\n", encoding="utf-8")

    exit_code = main([str(csv_file)])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "could not load tasks" in captured.err


def test_cli_empty_csv_prints_message(tmp_path, capsys):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n",
        encoding="utf-8",
    )

    exit_code = main([str(csv_file)])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "No study blocks allocated."


def test_cli_accepts_default_hours(tmp_path, capsys):
    csv_file = create_tasks_csv(tmp_path)

    exit_code = main(
        [
            str(csv_file),
            "--today",
            "2026-10-26",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Review Python: 2 hours" in captured.out


@pytest.mark.parametrize("hours", ["-1", "nan", "inf", "-inf", "abc"])
def test_cli_rejects_invalid_hours(tmp_path, hours):
    csv_file = create_tasks_csv(tmp_path)

    with pytest.raises(SystemExit) as error:
        main([str(csv_file), "--hours", hours])

    assert error.value.code == 2


def test_cli_rejects_invalid_today(tmp_path):
    csv_file = create_tasks_csv(tmp_path)

    with pytest.raises(SystemExit) as error:
        main([str(csv_file), "--today", "invalid-date"])

    assert error.value.code == 2
