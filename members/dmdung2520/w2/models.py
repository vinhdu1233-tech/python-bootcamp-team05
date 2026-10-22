from dataclasses import dataclass
from datetime import date
from math import isfinite


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("title must not be empty")
        if not isinstance(self.importance, int) or not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
        if not isinstance(self.effort_h, (int, float)) or not isfinite(self.effort_h) or self.effort_h < 0:
            raise ValueError("effort_h must be a finite non-negative number")
        if not isinstance(self.deadline, date):
            raise ValueError("deadline must be a date")

    def days_left(self, today: date) -> int:
        return max(0, (self.deadline - today).days)
