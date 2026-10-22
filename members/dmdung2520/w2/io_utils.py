import csv
import json
from datetime import date

from members.dmdung2520.w2.models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        expected_headers = ["title", "importance", "effort_h", "deadline"]
        if reader.fieldnames != expected_headers:
            raise ValueError("Invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            try:
                title = row["title"]
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid row at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
