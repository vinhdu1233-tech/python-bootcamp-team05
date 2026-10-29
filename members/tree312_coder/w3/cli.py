
"""Week 3-3: Command-line study planner."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.tree312_coder.w2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def valid_hours(value: str) -> float:
    """Convert and validate available study hours."""
    try:
        hours = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Hours must be numeric"
        ) from exc

    if not math.isfinite(hours) or hours < 0:
        raise argparse.ArgumentTypeError(
            "Hours must be finite and non-negative"
        )

    return hours


def main(argv: list[str] | None = None) -> int:
    """Read tasks and print a prioritised study plan."""
    parser = argparse.ArgumentParser(
        description="Week 3 individual Study Planner"
    )

    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--hours", type=valid_hours, required=True)
    parser.add_argument("--today", type=str, default=None)

    args = parser.parse_args(argv)

    try:
        today = (
            date.fromisoformat(args.today)
            if args.today
            else date.today()
        )

        tasks = load_tasks(args.csv_file)
        ordered = prioritise(tasks, today)
        blocks = allocate(ordered, args.hours)

    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Tonight ({args.hours:.1f} h):")

    for index, block in enumerate(blocks, start=1):
        print(
            f"  {index}. {block.task.title} "
            f"...... {block.hours:g} h"
        )

    if not blocks:
        print("  No tasks allocated.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
