from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

TODAY = date(2026, 10, 22)


def make_task(title, importance, deadline):
    return Task(title, importance, 2.0, deadline)


def test_higher_importance_first():
    low = make_task("Low", 2, date(2026, 10, 25))
    high = make_task("High", 5, date(2026, 10, 25))

    assert prioritise([low, high], TODAY) == [high, low]


def test_nearer_deadline_first():
    far = make_task("Far", 5, date(2026, 10, 30))
    near = make_task("Near", 3, date(2026, 10, 23))

    assert prioritise([far, near], TODAY) == [near, far]


def test_overdue_and_today():
    overdue = make_task("Overdue", 4, date(2026, 10, 20))
    due_today = make_task("Today", 3, TODAY)
    tomorrow = make_task("Tomorrow", 2, date(2026, 10, 23))

    result = prioritise([tomorrow, due_today, overdue], TODAY)

    assert result == [overdue, due_today, tomorrow]


def test_ties_keep_original_order():
    first = make_task("First", 4, date(2026, 10, 24))
    second = make_task("Second", 4, date(2026, 10, 24))

    assert prioritise([first, second], TODAY) == [first, second]


def test_empty_list():
    assert prioritise([], TODAY) == []


def test_input_not_modified():
    first = make_task("First", 1, date(2026, 10, 30))
    second = make_task("Second", 5, date(2026, 10, 23))
    tasks = [first, second]

    result = prioritise(tasks, TODAY)

    assert result == [second, first]
    assert tasks == [first, second]