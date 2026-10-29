"""Tests for the study planner command-line interface."""

import sys

from members.lnmthi.w3 import cli


def write_tasks(path):
    """Create a CSV file containing sample tasks."""
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Past Task,3,2,2026-10-27\n"
        "Today Task,4,1.5,2026-10-28\n"
        "Future Task,5,3,2026-10-30\n"
        "Long Task,2,8,2026-10-28\n",
        encoding="utf-8",
    )
    return path


def test_cli_filters_by_date_and_hours(tmp_path, monkeypatch, capsys):
    """Only tasks meeting both filters should be printed."""
    task_file = write_tasks(tmp_path / "tasks.csv")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "cli",
            "--file",
            str(task_file),
            "--today",
            "2026-10-28",
            "--hours",
            "5",
        ],
    )

    result = cli.main()
    output = capsys.readouterr().out

    assert result == 0
    assert "Past Task" in output
    assert "Today Task" in output
    assert "Future Task" not in output
    assert "Long Task" not in output


def test_cli_missing_file_returns_one(monkeypatch, capsys, tmp_path):
    """A missing CSV file should return exit code 1."""
    missing_file = tmp_path / "missing.csv"
    monkeypatch.setattr(
        sys, "argv", ["cli", "--file", str(missing_file)]
    )

    result = cli.main()
    captured = capsys.readouterr()

    assert result == 1
    assert "Error:" in captured.err


def test_cli_no_matching_tasks(tmp_path, monkeypatch, capsys):
    """Print a message when no tasks match the filters."""
    task_file = write_tasks(tmp_path / "tasks.csv")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "cli",
            "--file",
            str(task_file),
            "--today",
            "2026-10-20",
        ],
    )

    result = cli.main()
    output = capsys.readouterr().out

    assert result == 0
    assert "No tasks match" in output


def test_cli_negative_hours_is_rejected(monkeypatch):
    """Negative hour limits should be rejected by argparse."""
    monkeypatch.setattr(
        sys, "argv", ["cli", "--hours", "-1"]
    )

    try:
        cli.main()
    except SystemExit as error:
        assert error.code == 2
    else:
        raise AssertionError("Expected argparse to reject negative hours")
