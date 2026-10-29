
import csv
import math
from datetime import date
from pathlib import Path

from shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    """Load study tasks from a CSV file."""
    tasks = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expected = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != expected:
            raise ValueError("Invalid CSV header at line 1")

        for row in reader:
            try:
                if None in row or any(
                    row.get(field) is None for field in expected
                ):
                    raise ValueError("Missing or extra CSV fields")

                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])

                if not title:
                    raise ValueError("Title cannot be empty")

                if not 1 <= importance <= 5:
                    raise ValueError("Importance must be 1-5")

                if not math.isfinite(effort_h):
                    raise ValueError("Effort must be finite")

                if effort_h < 0:
                    raise ValueError("Effort cannot be negative")

                tasks.append(
                    Task(title, importance, effort_h, deadline)
                )

            except (TypeError, ValueError) as error:
                raise ValueError(
                    f"Invalid CSV data at line {reader.line_num}: {error}"
                ) from error

    return tasks
