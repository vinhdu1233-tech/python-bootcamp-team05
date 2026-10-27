"""Tests for Week 3 due-date parsing."""

from datetime import date

import pytest

from members.fumeneko.w3.dates import parse_due


@pytest.mark.parametrize(
    ("text", "today", "expected"),
    [
        ("2026-10-30", date(2026, 10, 26), date(2026, 10, 30)),
        ("tomorrow", date(2026, 10, 26), date(2026, 10, 27)),
        ("in 3 days", date(2026, 10, 26), date(2026, 10, 29)),
        ("in 1 day", date(2026, 10, 26), date(2026, 10, 27)),
        ("in 0 days", date(2026, 10, 26), date(2026, 10, 26)),
        ("Fri", date(2026, 10, 26), date(2026, 10, 30)),
        ("friday", date(2026, 10, 26), date(2026, 10, 30)),
        ("MON", date(2026, 10, 26), date(2026, 11, 2)),
        ("  tomorrow  ", date(2026, 10, 26), date(2026, 10, 27)),
    ],
)
def test_parse_due_supported_formats(text, today, expected):
    assert parse_due(text, today) == expected


def test_weekday_is_strictly_next_occurrence_when_today_matches():
    assert parse_due("Fri", date(2026, 10, 30)) == date(2026, 11, 6)


@pytest.mark.parametrize(
    "text",
    [
        "",
        "next Friday",
        "yesterday",
        "in -3 days",
        "in three days",
        "2026-02-30",
        "26-10-2026",
    ],
)
def test_parse_due_rejects_unsupported_or_invalid_text(text):
    with pytest.raises(ValueError, match="Unsupported due date"):
        parse_due(text, date(2026, 10, 26))
