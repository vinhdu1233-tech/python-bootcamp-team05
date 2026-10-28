"""Command-line entry point for the shared Week 3 study planner.

Run from the repository root::

    python -m shared.study_planner --hours 2 --today 2026-10-26
    python -m shared.study_planner tasks.csv --hours 3 --today 2026-10-26

Use --help to see all options. This module coordinates existing shared logic;
it deliberately does not duplicate CSV parsing or scheduling algorithms.
"""

import argparse
import csv
import math
import sys
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from members.tree312_coder.w2.errors import InfeasiblePlan, check_feasible
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

DEFAULT_CSV = Path(__file__).with_name("sample_tasks.csv")


def _non_negative_hours(value: str) -> float:
    """Convert an hours argument, rejecting negative and non-finite values."""
    try:
        hours = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a number") from exc
    if not math.isfinite(hours) or hours < 0:
        raise argparse.ArgumentTypeError("hours must be finite and non-negative")
    return hours


def _iso_date(value: str) -> date:
    """Convert YYYY-MM-DD to a date and report mistakes as argument errors."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("today must be a valid YYYY-MM-DD date") from exc


def build_parser() -> argparse.ArgumentParser:
    """Describe the public Week 3 CLI options."""
    parser = argparse.ArgumentParser(
        description="Prioritise tasks from CSV and allocate your available study hours."
    )
    parser.add_argument(
        "csv_path",
        nargs="?",
        type=Path,
        default=DEFAULT_CSV,
        metavar="CSV",
        help="CSV with title,importance,effort_h,deadline (default: bundled sample)",
    )
    parser.add_argument(
        "--hours",
        type=_non_negative_hours,
        default=2.0,
        metavar="HOURS",
        help="Available study hours (non-negative, default: 2)",
    )
    parser.add_argument(
        "--today",
        type=_iso_date,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="Date to use for prioritisation (default: current date)",
    )
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Require enough hours to complete all tasks",
    )
    return parser



def run_plan(
    csv_path: Path,
    hours: float,
    today: date,
    require_complete: bool = False,
) -> str:
    """Build a study plan with optional feasibility checking."""

    # Check whether the CSV file is completely empty.
    if csv_path.stat().st_size == 0:
        raise ValueError("CSV file is empty")

    # Load tasks from CSV.
    tasks = parse_csv(csv_path)

    # Require enough time to finish all tasks when requested.
    if require_complete:
        check_feasible(tasks, hours)

    # Reuse existing scheduling functions.
    ordered = prioritise(tasks, today)
    blocks = allocate(ordered, hours)

    return render(blocks)


def main(argv: Sequence[str] | None = None) -> int:
    """Return 0 on success, 1 for data errors, 2 for CLI errors."""
    args = build_parser().parse_args(argv)

    try:
        output = run_plan(
            args.csv_path,
            args.hours,
            args.today,
            require_complete=args.require_complete,
        )

    except InfeasiblePlan as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if output:
        print(output)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
