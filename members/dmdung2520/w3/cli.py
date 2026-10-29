"""Command-line interface for the Week 3 study planner."""

import argparse
import sys
from datetime import date
from pathlib import Path

from members.dmdung2520.w2.io_utils import load_tasks
from members.dmdung2520.w3.dates import parse_due


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Plan study tasks from a CSV file.")
    parser.add_argument("csv_file", help="Path to the task CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        default=date.today().isoformat(),
        help="Reference date in YYYY-MM-DD format",
    )
    return parser


def main() -> int:
    """Load tasks and display a study plan."""
    parser = build_parser()
    args = parser.parse_args()

    if args.hours < 0:
        parser.error("--hours must not be negative")

    try:
        today = parse_due(args.today, date.today())
    except ValueError as error:
        print(f"Invalid --today value: {error}", file=sys.stderr)
        return 1

    csv_path = Path(args.csv_file)

    if not csv_path.is_file():
        print(f"Error: file not found: {csv_path}", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(csv_path)
    except (ValueError, OSError) as error:
        print(f"Error reading tasks: {error}", file=sys.stderr)
        return 1

    tasks.sort(
        key=lambda task: (
            task.deadline,
            -task.importance,
            task.effort_h,
        )
    )

    print(f"Study plan for {today.isoformat()}")
    print(f"Available hours: {args.hours:g}")
    print("-" * 40)

    remaining_hours = args.hours

    for task in tasks:
        if remaining_hours <= 0:
            break

        allocated_hours = min(task.effort_h, remaining_hours)

        if allocated_hours <= 0:
            continue

        print(
            f"{task.title} | "
            f"importance={task.importance} | "
            f"deadline={task.deadline.isoformat()} | "
            f"study={allocated_hours:g} hours"
        )

        remaining_hours -= allocated_hours

    print("-" * 40)
    print(f"Remaining hours: {remaining_hours:g}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
