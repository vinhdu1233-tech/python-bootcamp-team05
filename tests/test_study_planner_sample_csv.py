from datetime import date
from pathlib import Path

from shared.study_planner.parse import parse_csv


def test_sample_csv_loads_expected_tasks():
    sample_csv = (
        Path(__file__).resolve().parents[1]
        / "shared"
        / "study_planner"
        / "sample_tasks.csv"
    )

    tasks = parse_csv(sample_csv)

    assert len(tasks) == 4
    assert [
        (task.title, task.importance, task.effort_h, task.deadline)
        for task in tasks
    ] == [
        ("Review Python", 5, 2.0, date(2026, 10, 22)),
        ("Complete assignment", 4, 3.5, date(2026, 10, 24)),
        ("Prepare for exam", 5, 5.0, date(2026, 10, 28)),
        ("Practice algorithms", 3, 1.5, date(2026, 10, 30)),
    ]
