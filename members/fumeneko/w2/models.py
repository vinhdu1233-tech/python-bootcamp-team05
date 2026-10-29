"""Data models for the Week 2 study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a study task loaded from CSV."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate the task's importance after initialization."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return non-negative days remaining until the deadline."""
        delta = (self.deadline - today).days
        return max(0, delta)
