import json
from datetime import date

import pytest

from members.fumeneko.w2.errors import InfeasiblePlan, check_feasible
from members.fumeneko.w2.io_utils import load_tasks, save_json
from members.fumeneko.w2.models import Task


def test_load_tasks_valid_csv(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Study Python,5,2.5,2026-10-30\n",
        encoding="utf-8",
    )

    tasks = load_tasks(path)

    assert tasks == [Task("Study Python", 5, 2.5, date(2026, 10, 30))]


@pytest.mark.parametrize(
    "csv_content",
    [
        "name,importance,effort_h,deadline\nTask,3,1,2026-10-30\n",
        "title,importance,effort_h,deadline\n,3,1,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask,8,1,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask,3,-1,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask,3,abc,2026-10-30\n",
        "title,importance,effort_h,deadline\nTask,3,1,not-a-date\n",
        "title,importance,effort_h,deadline\nTask,3,1\n",
        "title,importance,effort_h,deadline\nTask,3,1,2026-10-30,extra\n",
    ],
)
def test_load_tasks_invalid_csv(tmp_path, csv_content):
    path = tmp_path / "invalid.csv"
    path.write_text(csv_content, encoding="utf-8")

    with pytest.raises(ValueError, match="line"):
        load_tasks(path)


def test_save_json(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [Task("Study Python", 5, 2.5, date(2026, 10, 30))]

    save_json(tasks, path)

    assert json.loads(path.read_text(encoding="utf-8")) == [
        {
            "title": "Study Python",
            "importance": 5,
            "effort_h": 2.5,
            "deadline": "2026-10-30",
        }
    ]


def test_check_feasible():
    tasks = [Task("Task A", 4, 2.0, date(2026, 10, 30))]
    check_feasible(tasks, available_h=2.0)


def test_check_feasible_raises_for_insufficient_hours():
    tasks = [
        Task("Task A", 5, 2.0, date(2026, 10, 30)),
        Task("Task B", 4, 3.0, date(2026, 10, 31)),
    ]

    with pytest.raises(InfeasiblePlan) as error:
        check_feasible(tasks, available_h=4.0)

    assert error.value.needed_h == 5.0
    assert error.value.available_h == 4.0
