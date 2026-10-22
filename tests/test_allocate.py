
from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def make_task(title: str, effort_h: float) -> Task:
    return Task(title=title, importance=3, effort_h=effort_h, deadline=date(2026, 10, 30),)


def test_allocate_when_hours_are_sufficient():
    tasks = [make_task("Task A", 2.0), make_task("Task B", 3.0),]

    blocks = allocate(tasks, 6.0)

    assert [block.hours for block in blocks] == [2.0, 3.0]
    assert sum(block.hours for block in blocks) <= 6.0


def test_allocate_when_hours_are_insufficient():
    tasks = [make_task("Task A", 2.0), make_task("Task B", 3.0),]

    blocks = allocate(tasks, 4.0)

    assert [block.hours for block in blocks] == [2.0, 2.0]
    assert [block.task.title for block in blocks] == ["Task A", "Task B",]
    assert sum(block.hours for block in blocks) <= 4.0


def test_allocate_zero_hours():
    tasks = [make_task("Task A", 2.0)]

    assert allocate(tasks, 0.0) == []


def test_allocate_fractional_hours():
    tasks = [make_task("Task A", 1.25), make_task("Task B", 2.0),]

    blocks = allocate(tasks, 2.5)

    assert [block.hours for block in blocks] == pytest.approx([1.25, 1.25])
    assert sum(block.hours for block in blocks) <= 2.5


def test_allocate_empty_task_list():
    assert allocate([], 5.0) == []


def test_allocate_never_exceeds_budget():
    tasks = [make_task("Task A", 4.0), make_task("Task B", 4.0), make_task("Task C", 4.0),]

    budget = 5.5
    blocks = allocate(tasks, budget)

    assert sum(block.hours for block in blocks) <= budget


def test_allocate_returns_block_objects():
    task = make_task("Task A", 2.0)

    blocks = allocate([task], 1.0)

    assert len(blocks) == 1
    assert isinstance(blocks[0], Block)
    assert blocks[0].task is task
    assert blocks[0].hours == 1.0


def test_allocate_rejects_negative_budget():
    with pytest.raises(ValueError):
        allocate([make_task("Task A", 2.0)], -1.0)
