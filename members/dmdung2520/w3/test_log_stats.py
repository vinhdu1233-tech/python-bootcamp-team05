
"""Tests for route log statistics."""

import pytest

from members.dmdung2520.w3.log_stats import analyse


def test_analyse_counts_requests_per_route():
    result = analyse(
        [
            ("/home", 10),
            ("/api", 20),
            ("/home", 30),
            ("/api", 40),
        ]
    )

    assert result["counts"] == {"/home": 2, "/api": 2}


def test_analyse_calculates_p95_per_route():
    result = analyse(
        [
            ("/home", 10),
            ("/home", 20),
            ("/home", 30),
            ("/home", 40),
            ("/home", 50),
            ("/home", 60),
            ("/home", 70),
            ("/home", 80),
            ("/home", 90),
            ("/home", 100),
        ]
    )

    assert result["p95"]["/home"] == 100.0


def test_analyse_finds_slowest_route():
    result = analyse(
        [
            ("/fast", 10),
            ("/fast", 20),
            ("/slow", 100),
            ("/slow", 200),
        ]
    )

    assert result["slowest"] == "/slow"


def test_analyse_empty_input():
    result = analyse([])

    assert result == {
        "counts": {},
        "p95": {},
        "slowest": None,
    }


def test_analyse_single_request():
    result = analyse([("/home", 12.5)])

    assert result["counts"] == {"/home": 1}
    assert result["p95"] == {"/home": 12.5}
    assert result["slowest"] == "/home"


def test_analyse_rejects_empty_route():
    with pytest.raises(ValueError, match="route"):
        analyse([("", 10)])


@pytest.mark.parametrize("latency", [-1, float("inf"), float("-inf"), float("nan")])
def test_analyse_rejects_invalid_latency(latency):
    with pytest.raises(ValueError, match="finite and non-negative"):
        analyse([("/home", latency)])


@pytest.mark.parametrize("latency", ["10", None, True])
def test_analyse_rejects_non_numeric_latency(latency):
    with pytest.raises(TypeError, match="real number"):
        analyse([("/home", latency)])


def test_analyse_uses_first_route_when_p95_ties():
    result = analyse(
        [
            ("/first", 50),
            ("/second", 50),
        ]
    )

    assert result["slowest"] == "/first"
