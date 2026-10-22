
import json
from datetime import date

import pytest

from members.vinhdu1233_tech.w2.errors import (
    InfeasiblePlan,
    check_feasible,
)
from members.vinhdu1233_tech.w2.io_utils import load_tasks, save_json
from members.vinhdu1233_tech.w2.models import Task


def sample_task():
    return Task("DS exam", 5, 6.0, date(2026, 10, 30))


def test_load_csv(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n",
        encoding="utf-8",
    )

    tasks = load_tasks(path)

    assert len(tasks) == 1
    assert tasks[0] == sample_task()


def test_invalid_csv_row(tmp_path):
    path = tmp_path / "invalid.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,9,6,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        load_tasks(path)


def test_save_json(tmp_path):
    path = tmp_path / "tasks.json"
    save_json([sample_task()], path)

    data = json.loads(path.read_text(encoding="utf-8"))

    assert data[0]["title"] == "DS exam"
    assert data[0]["deadline"] == "2026-10-30"


def test_feasible_plan():
    check_feasible([sample_task()], available_h=8.0)


def test_infeasible_plan():
    with pytest.raises(InfeasiblePlan) as error:
        check_feasible([sample_task()], available_h=3.0)

    assert error.value.needed_h == 6.0
    assert error.value.available_h == 3.0
    assert "Not enough time" in str(error.value)
