import sys

from members.dmdung2520.w3 import cli


def test_cli_missing_file(monkeypatch, capsys, tmp_path):
    missing_file = tmp_path / "missing.csv"

    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", str(missing_file)],
    )

    cli.main()

    captured = capsys.readouterr()
    assert "file not found" in captured.err.lower()


def test_cli_accepts_today_argument(monkeypatch, tmp_path):
    tasks_file = tmp_path / "tasks.csv"
    tasks_file.write_text(
        "title,importance,effort_h,deadline\n" "Learn Python,4,2,2026-11-05\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "cli.py",
            str(tasks_file),
            "--hours",
            "2",
            "--today",
            "2026-10-29",
        ],
    )

    cli.main()


def test_cli_invalid_today(monkeypatch, capsys, tmp_path):
    tasks_file = tmp_path / "tasks.csv"
    tasks_file.write_text(
        "title,importance,effort_h,deadline\n" "Learn Python,4,2,2026-11-05\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "cli.py",
            str(tasks_file),
            "--today",
            "invalid-date",
        ],
    )

    cli.main()

    captured = capsys.readouterr()
    assert "invalid --today value" in captured.err.lower()
