from datetime import date

import pytest

from members.TuanTu2205.w2.models import Task


def test_days_left():
    task = Task("DS exam", 5, 6.0, date(2026, 10, 30))

    assert task.days_left(date(2026, 10, 22)) == 8


def test_overdue_task():
    task = Task("Homework", 4, 2.0, date(2026, 10, 20))

    assert task.days_left(date(2026, 10, 22)) == 0


def test_invalid_importance():
    with pytest.raises(ValueError):
        Task("Homework", 6, 2.0, date(2026, 10, 30))