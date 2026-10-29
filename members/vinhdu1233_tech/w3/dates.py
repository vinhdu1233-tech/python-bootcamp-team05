"""Week 3-1: parse human-friendly task due dates deterministically."""

import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, 'tomorrow', 'in N days', or the next weekday.

    A weekday always refers to a *future* occurrence: asking for 'Tue'
    on Tuesday returns the Tuesday of the following week.

    Raises:
        ValueError: If the expression is unknown or the ISO date is invalid.
    """
    value = text.strip().lower()

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return date.fromisoformat(value)
    if value == "tomorrow":
        return today + timedelta(days=1)

    relative = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if relative:
        return today + timedelta(days=int(relative.group(1)))

    if value in _WEEKDAYS:
        delta = (_WEEKDAYS[value] - today.weekday()) % 7
        return today + timedelta(days=delta or 7)

    raise ValueError(f"Unknown due date: {text!r}")
