import csv
import json
import math
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from CSV, raising ValueError with the relevant line number."""
    tasks = []
    expected_fields = ["title", "importance", "effort_h", "deadline"]

    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != expected_fields:
            raise ValueError(
                f"Invalid CSV header at line 1: expected {expected_fields}"
            )

        for row in reader:
            line_num = reader.line_num
            try:
                if None in row or any(row.get(field) is None for field in expected_fields):
                    raise ValueError("missing or extra CSV fields")

                title = row["title"].strip()
                if not title:
                    raise ValueError("title cannot be empty")

                importance = int(row["importance"])
                if not 1 <= importance <= 5:
                    raise ValueError("importance must be between 1 and 5")

                effort_h = float(row["effort_h"])
                if not math.isfinite(effort_h) or effort_h < 0:
                    raise ValueError("effort_h must be a finite non-negative number")

                deadline = date.fromisoformat(row["deadline"].strip())

                tasks.append(
                    Task(
                        title=title,
                        importance=importance,
                        effort_h=effort_h,
                        deadline=deadline,
                    )
                )
            except (TypeError, ValueError, AttributeError) as error:
                raise ValueError(
                    f"Invalid row at line {line_num}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
