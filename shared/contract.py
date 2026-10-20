
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a task in the shared study planner."""

    title: str
    importance: int
    effort_h: float
    deadline: date


@dataclass
class Block:
    """Represent allocated study time for a task."""

    task: Task
    hours: float
