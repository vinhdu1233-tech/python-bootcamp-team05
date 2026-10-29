from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a study task with importance, effort and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate the importance score after initialization."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return the remaining days, using zero for overdue tasks."""
        return max((self.deadline - today).days, 0)
