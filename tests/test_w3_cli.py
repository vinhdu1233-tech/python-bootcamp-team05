"""Tests for the Week 3 study planner command-line interface."""

from members.fumeneko.w3.cli import main


def test_cli_prints_a_study_plan(tmp_path, capsys):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Review Python,5,2.0,2026-10-30\n"
        "Practice tests,3,1.0,2026-11-04\n",
        encoding="utf-8",
    )

    exit_code = main(
        [str(csv_file), "--hours", "2", "--today", "2026-10-26"]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Review Python: 2 hours\n"
    assert captured.err == ""


def test_cli_missing_file_returns_one_and_prints_message(tmp_path, capsys):
    missing_file = tmp_path / "missing.csv"

    exit_code = main(
        [str(missing_file), "--hours", "2", "--today", "2026-10-26"]
    )

    captured = capsys.readouterr()
    assert exit_code == 1
    assert f"Error: CSV file not found: {missing_file}" in captured.err


def test_cli_empty_csv_tasks_prints_message(tmp_path, capsys):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n",
        encoding="utf-8",
    )

    exit_code = main(
        [str(csv_file), "--hours", "2", "--today", "2026-10-26"]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "No study blocks allocated.\n"


def test_cli_rejects_invalid_csv_with_exit_one(tmp_path, capsys):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text("bad,header\n", encoding="utf-8")

    exit_code = main([str(csv_file), "--hours", "2"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Error: could not load tasks:" in captured.err
