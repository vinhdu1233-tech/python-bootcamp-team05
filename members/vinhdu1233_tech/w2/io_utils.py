
import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from a CSV file."""
    tasks = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expected = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != expected:
            raise ValueError("Invalid CSV header at line 1")

        for row in reader:
            line_number = reader.line_num

            try:
                if None in row or any(
                    row.get(column) is None for column in expected
                ):
                    raise ValueError("Missing or extra CSV fields")

                title = row["title"].strip()

                if not title:
                    raise ValueError("Task title cannot be empty")

                task = Task(
                    title=title,
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )

                tasks.append(task)

            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid CSV row at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file."""
    data = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
