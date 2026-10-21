import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with Path(path).open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        required = {"title", "importance", "effort_h", "deadline"}

        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("Invalid CSV header at line 1")

        for row in reader:
            try:
                title = row["title"].strip()

                if not title:
                    raise ValueError("Title cannot be empty")

                task = Task(
                    title=title,
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )

            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid CSV row at line {reader.line_num}: {error}"
                ) from error

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = []

    for task in tasks:
        row = asdict(task)
        row["deadline"] = task.deadline.isoformat()
        data.append(row)

    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)