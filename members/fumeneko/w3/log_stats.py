"""Summarise request counts and latency statistics by route."""

from collections import Counter
from collections.abc import Iterable
from math import ceil, isfinite


def analyse(pairs: Iterable[tuple[str, float]]) -> dict[str, object]:
    """Return request counts, per-route p95 latency, and the slowest route.

    The p95 uses the nearest-rank method: sort latencies and select the
    value at rank ceil(0.95 * n). Empty input returns empty dictionaries
    and None for the slowest route.

    Args:
        pairs: An iterable of (route, latency_ms) pairs.

    Returns:
        A dictionary with counts, p95, and slowest keys.

    Raises:
        ValueError: If a route is empty or a latency is negative/non-finite.
    """
    latencies: dict[str, list[float]] = {}
    counts: Counter[str] = Counter()

    for route, latency_ms in pairs:
        if not isinstance(route, str) or not route.strip():
            raise ValueError("route must be a non-empty string")
        if not isfinite(latency_ms) or latency_ms < 0:
            raise ValueError("latency_ms must be finite and non-negative")

        counts[route] += 1
        latencies.setdefault(route, []).append(float(latency_ms))

    p95: dict[str, float] = {}
    for route, values in latencies.items():
        ordered = sorted(values)
        rank = ceil(0.95 * len(ordered))
        p95[route] = ordered[rank - 1]

    slowest = max(p95, key=p95.get) if p95 else None

    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
