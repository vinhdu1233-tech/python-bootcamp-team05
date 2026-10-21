import json
from datetime import date

import pytest

from members.TuanTu2205.w2.io_utils import load_tasks, save_json
from members.TuanTu2205.w2.models import Task


def test_load_tasks(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )

    tasks = load_tasks(csv_file)

    assert len(tasks) == 2
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[0].deadline == date(2026, 10, 30)
    assert tasks[1].effort_h == 1.5


def test_save_json(tmp_path):
    tasks = [
        Task("DS exam", 5, 6.0, date(2026, 10, 30))
    ]
    output = tmp_path / "tasks.json"

    save_json(tasks, output)

    data = json.loads(output.read_text(encoding="utf-8"))

    assert data[0]["title"] == "DS exam"
    assert data[0]["deadline"] == "2026-10-30"


def test_invalid_importance(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n"
        "Homework,9,2,2026-10-27\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 3"):
        load_tasks(csv_file)


def test_missing_column(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,deadline\n"
        "DS exam,5,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 1"):
        load_tasks(csv_file)


def test_empty_title(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        ",5,6,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        load_tasks(csv_file)