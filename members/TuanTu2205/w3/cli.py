import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.TuanTu2205.w2.io_utils import load_tasks
from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def valid_hours(text: str) -> float:
    try:
        hours = float(text)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "hours must be numeric"
        ) from error

    if not math.isfinite(hours) or hours < 0:
        raise argparse.ArgumentTypeError(
            "hours must be finite and non-negative"
        )

    return hours


def main(argv: list[str] | None = None) -> int:
    """Build and print a study plan from a CSV file."""
    parser = argparse.ArgumentParser(
        description="Week 3 individual Study Planner"
    )
    parser.add_argument("csv_file", type=Path)
    parser.add_argument(
        "--hours", type=valid_hours, required=True
    )
    parser.add_argument(
        "--today",
        help="Reference date in YYYY-MM-DD format",
    )
    args = parser.parse_args(argv)

    try:
        today = (
            date.fromisoformat(args.today)
            if args.today else date.today()
        )
    except ValueError:
        print(
            "Error: --today must be a valid YYYY-MM-DD date",
            file=sys.stderr,
        )
        return 1

    try:
        personal_tasks = load_tasks(args.csv_file)
    except (OSError, ValueError) as error:
        print(f"Error loading tasks: {error}", file=sys.stderr)
        return 1

    tasks = [
        Task(
            title=task.title,
            importance=task.importance,
            effort_h=task.effort_h,
            deadline=task.deadline,
        )
        for task in personal_tasks
    ]

    ordered = prioritise(tasks, today)
    blocks = allocate(ordered, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    if not blocks:
        print("  No study blocks allocated.")

    for index, block in enumerate(blocks, start=1):
        print(
            f"  {index}. {block.task.title} ...... "
            f"{block.hours:g} h"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
