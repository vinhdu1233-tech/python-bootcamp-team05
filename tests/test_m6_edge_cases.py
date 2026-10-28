
from datetime import date, timedelta

import pytest

from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def make_task(
    title: str,
    importance: int = 3,
    effort_h: float = 2.0,
    deadline: date = date(2026, 11, 1),
) -> Task:
    return Task(title, importance, effort_h, deadline)


def test_parse_csv_rejects_non_finite_effort(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Task A,5,nan,2026-11-01\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_csv(csv_file)


@pytest.mark.parametrize("effort", ["inf", "-inf"])
def test_parse_csv_rejects_infinite_effort(tmp_path, effort):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        f"Task A,5,{effort},2026-11-01\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_csv(csv_file)


def test_parse_csv_missing_file_raises_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        parse_csv(tmp_path / "missing.csv")


def test_prioritise_empty_list():
    assert prioritise([], date(2026, 10, 28)) == []


def test_prioritise_preserves_order_for_equal_scores():
    today = date(2026, 10, 28)
    first = make_task("First", 4, 1.0, today + timedelta(days=2))
    second = make_task("Second", 2, 1.0, today + timedelta(days=1))

    result = prioritise([first, second], today)

    assert result == [first, second]


def test_prioritise_does_not_modify_input():
    today = date(2026, 10, 28)
    tasks = [
        make_task("Later", 1, 1.0, today + timedelta(days=5)),
        make_task("Sooner", 5, 1.0, today + timedelta(days=1)),
    ]
    original = tasks.copy()

    prioritise(tasks, today)

    assert tasks == original


def test_allocate_zero_budget_returns_empty_list():
    tasks = [make_task("Task A", effort_h=2.0)]

    assert allocate(tasks, 0.0) == []


def test_allocate_skips_zero_effort_tasks():
    zero_task = make_task("Zero", effort_h=0.0)
    normal_task = make_task("Normal", effort_h=2.0)

    result = allocate([zero_task, normal_task], 3.0)

    assert [(block.task.title, block.hours) for block in result] == [
        ("Normal", 2.0)
    ]


@pytest.mark.parametrize("hours", [float("nan"), float("inf")])
def test_allocate_rejects_non_finite_budget(hours):
    with pytest.raises(ValueError):
        allocate([make_task("Task A")], hours)


def test_allocate_rejects_non_finite_effort():
    task = make_task("Task A", effort_h=float("nan"))

    with pytest.raises(ValueError):
        allocate([task], 3.0)


def test_render_empty_list():
    assert render([]) == ""


def test_render_preserves_decimal_hours():
    task = make_task("Review Python", effort_h=1.5)
    blocks = allocate([task], 1.5)

    assert render(blocks) == "Review Python: 1.5 hours"
