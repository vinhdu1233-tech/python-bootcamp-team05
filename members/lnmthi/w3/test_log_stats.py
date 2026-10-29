"""Tests for chat log analysis."""

import pytest

from members.lnmthi.w3.log_stats import analyse


def test_counts_requests_per_route() -> None:
    result = analyse([
        ("/chat", 100),
        ("/chat", 200),
        ("/search", 50),
    ])
    assert result["counts"] == {"/chat": 2, "/search": 1}


def test_calculates_p95_latency() -> None:
    result = analyse([
        ("/chat", 100),
        ("/chat", 200),
        ("/chat", 300),
        ("/search", 50),
    ])
    assert result["p95"]["/chat"] == 300
    assert result["p95"]["/search"] == 50


def test_finds_slowest_route() -> None:
    result = analyse([
        ("/chat", 100),
        ("/search", 500),
        ("/search", 600),
    ])
    assert result["slowest"] == "/search"


def test_empty_input() -> None:
    assert analyse([]) == {
        "counts": {},
        "p95": {},
        "slowest": None,
    }


def test_negative_latency_raises_value_error() -> None:
    with pytest.raises(ValueError):
        analyse([("/chat", -1)])
