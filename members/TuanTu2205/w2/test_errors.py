from datetime import date

import pytest

from members.TuanTu2205.w2.errors import (
    InfeasiblePlan,
    check_feasible,
)
from members.TuanTu2205.w2.models import Task


def sample_tasks():
    return [
        Task("DS exam", 5, 3.0, date(2026, 10, 30)),
        Task("Python homework", 4, 2.0, date(2026, 10, 27)),
    ]


def test_sufficient_hours():
    assert check_feasible(sample_tasks(), 6.0) is None


def test_insufficient_hours():
    with pytest.raises(InfeasiblePlan) as exc:
        check_feasible(sample_tasks(), 4.0)

    assert exc.value.needed_h == 5.0
    assert exc.value.available_h == 4.0


def test_exact_hours():
    assert check_feasible(sample_tasks(), 5.0) is None


def test_empty_tasks():
    assert check_feasible([], 0.0) is None


def test_error_message():
    error = InfeasiblePlan(5.0, 4.0)

    assert "5.0" in str(error)
    assert "4.0" in str(error)