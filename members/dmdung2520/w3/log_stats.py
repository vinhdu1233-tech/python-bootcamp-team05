
"""Summarise request counts and latency statistics by route."""

from collections import Counter
from collections.abc import Iterable
from math import ceil, isfinite
from numbers import Real
from typing import TypedDict


class LogStats(TypedDict):
    """Describe the result returned by log analysis."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: Iterable[tuple[str, float]]) -> LogStats:
    """Return request counts, per-route p95 latency, and the slowest route.

    The p95 uses the nearest-rank method. For each route, latencies are
    sorted and the value at rank ceil(0.95 * n) is selected.

    If multiple routes have the same p95, the first route encountered
    is reported as the slowest. Empty input returns empty dictionaries
    and None for the slowest route.

    Args:
        pairs: An iterable of (route, latency_ms) pairs.

    Returns:
        A dictionary containing counts, p95, and slowest.

    Raises:
        TypeError: If a latency is not a real number.
        ValueError: If a route is empty or latency is negative or non-finite.
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency_ms in pairs:
        if not isinstance(route, str) or not route.strip():
            raise ValueError("route must be a non-empty string")

        if isinstance(latency_ms, bool) or not isinstance(latency_ms, Real):
            raise TypeError("latency_ms must be a real number")

        latency = float(latency_ms)

        if not isfinite(latency) or latency < 0:
            raise ValueError("latency_ms must be finite and non-negative")

        counts[route] += 1
        latencies.setdefault(route, []).append(latency)

    p95: dict[str, float] = {}

    for route, values in latencies.items():
        ordered = sorted(values)
        rank = ceil(0.95 * len(ordered))
        p95[route] = ordered[rank - 1]

    slowest = max(p95, key=p95.__getitem__) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
