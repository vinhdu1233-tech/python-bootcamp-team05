"""Week 3-3: command-line study planner using existing Week 2 modules.

Example:
    python -m members.vinhdu1233_tech.w3.cli \\
        members/vinhdu1233_tech/w2/sample_tasks.csv \\
        --hours 2 --today 2026-10-26
"""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.vinhdu1233_tech.w2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def _nonnegative_hours(text: str) -> float:
    """Parse a finite, nonnegative number of available hours."""
    try:
        hours = float(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be numeric") from exc
    if not math.isfinite(hours) or hours < 0:
        raise argparse.ArgumentTypeError("hours must be finite and nonnegative")
    return hours


def main(argv: list[str] | None = None) -> int:
    """Read CSV tasks, prioritise and allocate hours, then print a plan."""
    parser = argparse.ArgumentParser(description="Week 3 individual study planner")
    parser.add_argument("csv_file", type=Path, help="CSV file containing study tasks")
    parser.add_argument("--hours", type=_nonnegative_hours, required=True)
    parser.add_argument(
        "--today",
        help="Use YYYY-MM-DD instead of the current date for reproducible plans",
    )
    args = parser.parse_args(argv)

    try:
        today = date.fromisoformat(args.today) if args.today else date.today()
    except ValueError:
        print("Error: --today must be a valid YYYY-MM-DD date", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(args.csv_file)  # Reuse Member 1's Week 2 CSV reader.
    except (OSError, ValueError) as exc:
        print(f"Error loading tasks: {exc}", file=sys.stderr)
        return 1

    ordered = prioritise(tasks, today)  # Reuse the team's Week 2 planner.
    blocks = allocate(ordered, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    if not blocks:
        print("  No study blocks allocated.")
    for number, block in enumerate(blocks, start=1):
        print(f"  {number}. {block.task.title} ...... {block.hours:g} h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
