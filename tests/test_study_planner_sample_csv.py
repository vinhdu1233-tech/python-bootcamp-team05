from datetime import date
from pathlib import Path

from shared.study_planner.parse import parse_csv


def test_sample_csv_loads_expected_tasks():
    sample_csv = (
        Path(__file__).resolve().parents[1]
        / "samples"
        / "tasks.csv"
    )

    tasks = parse_csv(sample_csv)

    assert len(tasks) == 2
    assert [
        (task.title, task.importance, task.effort_h, task.deadline)
        for task in tasks
    ] == [
        ("Assignment", 5, 1.5, date(2026, 10, 30)),
        ("DS exam", 5, 0.5, date(2026, 10, 28)),
    ]
