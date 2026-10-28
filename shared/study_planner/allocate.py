import math

from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Allocate study hours greedily in the given task order.

    Each task receives up to its required effort hours before the next task is considered. Tasks receiving zero hours are omitted. The total allocation never exceeds the budget."""

    if not math.isfinite(hours):
        raise ValueError("Available hours must be finite.")

    if hours < 0:
        raise ValueError("Available hours cannot be negative.")

    for task in tasks:
        if not math.isfinite(task.effort_h):
            raise ValueError("Task effort hours must be finite.")

        if task.effort_h < 0:
            raise ValueError("Task effort hours cannot be negative.")

    remaining = hours
    blocks = []

    for task in tasks:
        if remaining <= 0:
            break

        allocated_hours = min(task.effort_h, remaining)

        if allocated_hours > 0:
            blocks.append(
                Block(task=task, hours=allocated_hours)
            )
            remaining -= allocated_hours

    return blocks
