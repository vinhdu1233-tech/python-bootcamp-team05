from datetime import date, timedelta

import pytest

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def test_pipeline_empty_csv(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")

    tasks = parse_csv(csv_file)
    prioritized = prioritise(tasks, date.today())
    blocks = allocate(prioritized, hours=5.0)

    assert tasks == []
    assert prioritized == []
    assert blocks == []
    assert render(blocks) == ""


@pytest.mark.parametrize(
    "csv_content",
    [
        "name,importance,effort_h,deadline\nTask A,5,2,2026-10-30\n",
        "title,importance,effort_h,deadline\n,5,2,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask A,8,2,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask A,5,-2,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask A,5,2,not-a-date\n",
        "title,importance,effort_h,deadline\nTask A,5,2\n",
        "title,importance,effort_h,deadline\nTask A,5,2,2026-10-30,extra\n",
    ],
)
def test_pipeline_rejects_invalid_csv(tmp_path, csv_content):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    with pytest.raises(ValueError, match="line"):
        parse_csv(csv_file)


def test_pipeline_overdue_and_zero_hours(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    overdue_deadline = date.today() - timedelta(days=2)
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        f"Old Task,5,2.0,{overdue_deadline.isoformat()}\n",
        encoding="utf-8",
    )

    tasks = parse_csv(csv_file)
    prioritized = prioritise(tasks, date.today())

    assert len(prioritized) == 1
    assert prioritized[0].title == "Old Task"
    assert allocate(prioritized, hours=0.0) == []

    blocks = allocate(prioritized, hours=5.0)
    assert len(blocks) == 1
    assert blocks[0].task.title == "Old Task"
    assert render(blocks) == "Old Task: 2 hours"


def test_pipeline_allocates_insufficient_hours_across_multiple_tasks(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Task A,5,2.0,2026-10-30\n"
        "Task B,4,3.0,2026-10-31\n",
        encoding="utf-8",
    )

    tasks = parse_csv(csv_file)
    prioritized = prioritise(tasks, date(2026, 10, 22))
    blocks = allocate(prioritized, hours=4.0)

    assert [(block.task.title, block.hours) for block in blocks] == [
        ("Task A", 2.0),
        ("Task B", 2.0),
    ]
    assert sum(block.hours for block in blocks) == 4.0
    assert render(blocks) == "Task A: 2 hours\nTask B: 2 hours"
