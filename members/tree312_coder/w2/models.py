
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("Importance must be between 1 and 5.")

        if self.effort_h < 0:
            raise ValueError("Effort hours cannot be negative.")

    def days_left(self, today: date) -> int:
        return max(0, (self.deadline - today).days)
