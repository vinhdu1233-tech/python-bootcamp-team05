"""Tests for due-date parsing."""

from datetime import date, timedelta

from members.lnmthi.w3.dates import parse_due


def test_parse_iso_date() -> None:
    assert parse_due("2026-10-30") == date(2026, 10, 30)


def test_parse_today() -> None:
    assert parse_due("today") == date.today()


def test_parse_tomorrow() -> None:
    assert parse_due("tomorrow") == date.today() + timedelta(days=1)


def test_parse_relative_days() -> None:
    assert parse_due("in 3 days") == date.today() + timedelta(days=3)
    assert parse_due("in 1 day") == date.today() + timedelta(days=1)


def test_parse_weekday_is_next_occurrence() -> None:
    days_ahead = (4 - date.today().weekday()) % 7 or 7
    assert parse_due("Fri") == date.today() + timedelta(days=days_ahead)


def test_invalid_expression_raises_value_error() -> None:
    for text in ("", "not a date", "32/13/2026", "in many days"):
        try:
            parse_due(text)
        except ValueError:
            continue
        raise AssertionError(f"Expected ValueError for {text!r}")
