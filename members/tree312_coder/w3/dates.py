
"""Week 3-1: Parse human-readable due dates."""

import re
from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(text: str, today: date) -> date:
    """Convert a date expression into a date object."""
    value = text.strip().lower()

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return date.fromisoformat(value)

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    weekday = value[:3]
    if weekday in WEEKDAYS and value in {
        weekday,
        ("monday", "tuesday", "wednesday",
         "thursday", "friday", "saturday", "sunday")[
            WEEKDAYS[weekday]
        ],
    }:
        target = WEEKDAYS[weekday]
        difference = (target - today.weekday()) % 7

        if difference == 0:
            difference = 7

        return today + timedelta(days=difference)

    raise ValueError(f"Unknown date expression: {text}")
