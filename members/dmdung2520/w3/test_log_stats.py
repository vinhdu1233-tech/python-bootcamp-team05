"""Tests for natural-language due date parsing."""

from datetime import date

import pytest

from members.dmdung2520.w3.log_stats import parse_due


def test_parse_iso_date():
    today = date(2026, 10, 28)

    assert parse_due("2026-10-30", today) == date(2026, 10, 30)


def test_parse_tomorrow():
    today = date(2026, 10, 28)

    assert parse_due("tomorrow", today) == date(2026, 10, 29)


def test_parse_days_from_today():
    today = date(2026, 10, 28)

    assert parse_due("in 3 days", today) == date(2026, 10, 31)


def test_parse_one_day_from_today():
    today = date(2026, 10, 28)

    assert parse_due("in 1 day", today) == date(2026, 10, 29)


def test_parse_zero_days_from_today():
    today = date(2026, 10, 28)

    assert parse_due("in 0 days", today) == today


def test_parse_next_weekday():
    today = date(2026, 10, 28)

    assert parse_due("Fri", today) == date(2026, 10, 30)


def test_parse_full_weekday_name():
    today = date(2026, 10, 28)

    assert parse_due("Monday", today) == date(2026, 11, 2)


def test_parse_weekday_case_insensitive():
    today = date(2026, 10, 28)

    assert parse_due("FRIDAY", today) == date(2026, 10, 30)


def test_same_weekday_means_next_week():
    today = date(2026, 10, 30)

    assert parse_due("Fri", today) == date(2026, 11, 6)


def test_parse_date_with_surrounding_whitespace():
    today = date(2026, 10, 28)

    assert parse_due("  tomorrow  ", today) == date(2026, 10, 29)


def test_empty_date_raises_value_error():
    today = date(2026, 10, 28)

    with pytest.raises(ValueError, match="Due date cannot be empty"):
        parse_due("", today)


def test_whitespace_date_raises_value_error():
    today = date(2026, 10, 28)

    with pytest.raises(ValueError, match="Due date cannot be empty"):
        parse_due("   ", today)


def test_invalid_date_raises_value_error():
    today = date(2026, 10, 28)

    with pytest.raises(ValueError, match="Invalid due date"):
        parse_due("not a date", today)


def test_invalid_iso_date_raises_value_error():
    today = date(2026, 10, 28)

    with pytest.raises(ValueError, match="Invalid due date"):
        parse_due("2026-02-30", today)
