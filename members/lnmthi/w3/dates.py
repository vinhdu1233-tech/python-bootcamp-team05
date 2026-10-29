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

def parse_due(text: str) -> date:
    """Parse a date, relative day, or weekday into a date."""
    value = text.strip().lower()
    today = date.today()

    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    if value == "today":
        return today

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if match:
        return today + timedelta(days=int(match.group(1)))

    if value in WEEKDAYS:
        days_ahead = (WEEKDAYS[value] - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)
    raise ValueError(f"Unknown date expression: {text!r}")
