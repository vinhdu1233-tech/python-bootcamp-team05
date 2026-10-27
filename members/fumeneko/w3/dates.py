"""Parse human-readable due dates into datetime.date values."""

import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0, "monday": 0,
    "tue": 1, "tues": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thur": 3, "thurs": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, tomorrow, in N days, or a weekday name.

    Weekday names refer to the next occurrence strictly after today.
    Matching is case-insensitive and ignores surrounding whitespace.

    Args:
        text: Human-readable due date.
        today: Reference date used for relative dates.

    Returns:
        The parsed due date.

    Raises:
        ValueError: If text is not one of the supported date formats.
    """
    value = text.strip().casefold()

    if value == "tomorrow":
        return today + timedelta(days=1)

    relative_match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if relative_match:
        return today + timedelta(days=int(relative_match.group(1)))

    if value in _WEEKDAYS:
        days_ahead = (_WEEKDAYS[value] - today.weekday()) % 7
        return today + timedelta(days=days_ahead or 7)

    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(
            f"Unsupported due date: {text!r}. Use YYYY-MM-DD, 'tomorrow', "
            "'in N days', or a weekday name such as 'Fri'."
        ) from error
