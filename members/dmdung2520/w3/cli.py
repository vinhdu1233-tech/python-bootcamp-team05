
"""Command-line interface for the Week 3 study planner."""

import argparse
import math
import sys
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from members.dmdung2520.w2.io_utils import load_tasks
from shared.contract import Task as SharedTask
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def _non_negative_hours(value: str) -> float:
    """Parse a finite, non-negative number of study hours."""
    try:
        hours = float(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "hours must be a number"
        ) from error

    if not math.isfinite(hours) or hours < 0:
        raise argparse.ArgumentTypeError(
            "hours must be finite and non-negative"
        )

    return hours


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the study planner CLI."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a task CSV file."
    )
    parser.add_argument(
        "csv_file",
        type=Path,
        help="Path to the task CSV file",
    )
    parser.add_argument(
        "--hours",
        type=_non_negative_hours,
        default=2.0,
        help="Available study time in hours (default: 2)",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="Reference date (defaults to today)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the study planner and return its exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        loaded_tasks = load_tasks(args.csv_file)
    except FileNotFoundError:
        print(
            f"Error: CSV file not found: {args.csv_file}",
            file=sys.stderr,
        )
        return 1
    except (OSError, ValueError) as error:
        print(
            f"Error: could not load tasks: {error}",
            file=sys.stderr,
        )
        return 1

    tasks = [
        SharedTask(
            title=task.title,
            importance=task.importance,
            effort_h=task.effort_h,
            deadline=task.deadline,
        )
        for task in loaded_tasks
    ]

    ordered_tasks = prioritise(tasks, args.today)
    blocks = allocate(ordered_tasks, args.hours)
    output = render(blocks)

    print(output if output else "No study blocks allocated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
