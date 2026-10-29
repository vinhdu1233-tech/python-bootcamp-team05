
from .models import Task


class InfeasiblePlan(Exception):
    """Raised when required study time exceeds available time."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Not enough time: need {self.needed_h} hours, "
            f"but only {self.available_h} hours available."
        )


def check_feasible(
    tasks: list[Task],
    available_h: float,
) -> None:
    """Raise InfeasiblePlan when tasks need too much time."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
