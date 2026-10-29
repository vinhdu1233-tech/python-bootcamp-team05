from .models import Task


class InfeasiblePlan(Exception):
    """Represent an error when required hours exceed available hours."""

    def __init__(
        self,
        needed_h: float,
        available_h: float,
    ) -> None:
        """Store required and available study hours."""
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        """Return a readable explanation of the infeasible plan."""
        return (
            f"Infeasible plan: need {self.needed_h} hours, "
            f"but only {self.available_h} hours available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when tasks require more available hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
