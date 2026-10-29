"""Custom exceptions and feasibility checks for study plans."""

from collections.abc import Sequence

from .models import Task


class InfeasiblePlan(Exception):
    """Signal that a study plan needs more time than is available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the required and available study hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Plan is infeasible: needed {needed_h}h, "
            f"but only {available_h}h available."
        )


def check_feasible(tasks: Sequence[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if task effort exceeds available study hours."""
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)
