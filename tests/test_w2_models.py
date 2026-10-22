
from datetime import date

import pytest

from members.vinhdu1233_tech.w2.models import Task


def test_create_task():
    task = Task("Study Python", 5, 2.0, date(2026, 10, 25))

    assert task.title == "Study Python"
    assert task.importance == 5
    assert task.effort_h == 2.0


def test_days_left():
    task = Task("Study Python", 5, 2.0, date(2026, 10, 25))

    assert task.days_left(date(2026, 10, 20)) == 5


def test_overdue_task():
    task = Task("Study Python", 5, 2.0, date(2026, 10, 15))

    assert task.days_left(date(2026, 10, 20)) == 0


def test_invalid_importance():
    with pytest.raises(ValueError):
        Task("Study Python", 6, 2.0, date(2026, 10, 25))
