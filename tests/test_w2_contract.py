
from datetime import date

from shared.contract import Block, Task


def test_create_task():
    task = Task(
        title="Python Homework",
        importance=5,
        effort_h=3.0,
        deadline=date(2026, 10, 22),
    )

    assert task.title == "Python Homework"
    assert task.importance == 5
    assert task.effort_h == 3.0
    assert task.deadline == date(2026, 10, 22)


def test_create_block():
    task = Task("Python Homework", 5, 3.0, date(2026, 10, 22))
    block = Block(task=task, hours=2.0)

    assert block.task == task
    assert block.hours == 2.0
