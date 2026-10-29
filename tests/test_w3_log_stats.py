"""Tests for Week 3 route latency statistics."""

import pytest

from members.fumeneko.w3.log_stats import analyse


def test_analyse_counts_routes_and_computes_p95():
    result = analyse(
        [
            ("/home", 10),
            ("/api", 20),
            ("/home", 30),
            ("/home", 40),
            ("/api", 100),
        ]
    )

    assert result == {
        "counts": {"/home": 3, "/api": 2},
        "p95": {"/home": 40.0, "/api": 100.0},
        "slowest": "/api",
    }


def test_analyse_uses_nearest_rank_for_p95():
    result = analyse([("/x", value) for value in range(1, 21)])

    assert result["p95"] == {"/x": 19.0}


def test_analyse_returns_empty_result_for_no_pairs():
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}


def test_analyse_accepts_zero_latency():
    assert analyse([("/health", 0)]) == {
        "counts": {"/health": 1},
        "p95": {"/health": 0.0},
        "slowest": "/health",
    }


def test_analyse_tied_p95_uses_first_route():
    result = analyse([("/first", 10), ("/second", 10)])

    assert result["p95"] == {"/first": 10.0, "/second": 10.0}
    assert result["slowest"] == "/first"


@pytest.mark.parametrize(
    "pairs",
    [
        [("", 10)],
        [("   ", 10)],
        [("/api", -1)],
        [("/api", float("inf"))],
        [("/api", float("nan"))],
    ],
)
def test_analyse_rejects_invalid_values(pairs):
    with pytest.raises(ValueError):
        analyse(pairs)


@pytest.mark.parametrize(
    "latency",
    ["fast", None, True],
)
def test_analyse_rejects_non_numeric_latency_types(latency):
    with pytest.raises(TypeError, match="latency_ms must be a real number"):
        analyse([("/api", latency)])
