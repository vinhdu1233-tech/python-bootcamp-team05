"""Tests for date parsing."""

from datetime import date

import pytest

from members.dmdung2520.w3.dates import parse_due


def test_parse_iso_date():
    today = date(2026, 10, 28)
    assert parse_due("2026-10-30", today) == date(2026, 10, 30)


def test_parse_tomorrow():
    today = date(2026, 10, 28)
    assert parse_due("tomorrow", today) == date(2026, 10, 29)


def test_parse_days_from_today():
    today = date(2026, 10, 28)
    assert parse_due("in 3 days", today) == date(2026, 10, 31)


def test_parse_next_weekday():
    today = date(2026, 10, 28)
    assert parse_due("Fri", today) == date(2026, 10, 30)


def test_same_weekday_means_next_week():
    today = date(2026, 10, 30)
    assert parse_due("Fri", today) == date(2026, 11, 6)


def test_invalid_date_raises_value_error():
    with pytest.raises(ValueError):
        parse_due("not a date", date(2026, 10, 28))
