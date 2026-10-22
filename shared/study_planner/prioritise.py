from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Sort tasks by importance divided by remaining days.

    Today and overdue deadlines count as one day.
    Equal scores preserve the original input order.
    The input list is not modified.
    """
    return sorted(
        tasks,
        key=lambda task: (
            task.importance
            / max(1, (task.deadline - today).days)
        ),
        reverse=True,
    )