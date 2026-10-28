"""Command-line interface for filtering study planner tasks."""

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

from ..w2.io_utils import load_tasks


def main() -> int:
    """Load tasks from CSV and filter them by deadline and effort."""
    parser = argparse.ArgumentParser(description="Filter study planner tasks.")
    parser.add_argument(
        "--file",
        default=str(Path(__file__).parents[1] / "w2" / "task.csv"),
        help="Path to the task CSV file.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        help="Show tasks requiring no more than this many hours.",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="Reference date (defaults to today).",
    )
    args = parser.parse_args()

    if args.hours is not None and args.hours < 0:
        parser.error("--hours must not be negative")

    try:
        tasks = load_tasks(args.file)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    cutoff = args.today + timedelta(days=1)
    filtered = [
        task for task in tasks
        if task.deadline < cutoff
        and (args.hours is None or task.effort_h <= args.hours)
    ]

    if not filtered:
        print("No tasks match the given filters.")
        return 0

    for task in filtered:
        print(
            f"{task.title} | importance={task.importance} "
            f"| effort_h={task.effort_h:g} "
            f"| deadline={task.deadline.isoformat()}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


