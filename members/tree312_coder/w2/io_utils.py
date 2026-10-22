
import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks = []

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required_fields = {"title", "importance", "effort_h", "deadline"}

        if reader.fieldnames is None or not required_fields.issubset(reader.fieldnames):
            raise ValueError("Invalid CSV header on line 1.")

        for row in reader:
            line = reader.line_num

            try:
                if None in row:
                    raise ValueError("Too many values.")

                if any(row[field] is None for field in required_fields):
                    raise ValueError("Missing values.")

                title = row["title"].strip()
                if not title:
                    raise ValueError("Title cannot be empty.")

                task = Task(
                    title=title,
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid data on line {line}: {error}"
                ) from error

    return tasks

def save_json(tasks: list[Task], path: str | Path) -> None:
    data = []

    for task in tasks:
        data.append({
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        })

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
