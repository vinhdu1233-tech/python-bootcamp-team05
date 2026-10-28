"""Analyze request counts and latency statistics by route."""

from collections import Counter, defaultdict
from collections.abc import Sequence
from math import ceil


def analyse(pairs: Sequence[tuple[str, float]]) -> dict:
    """Return request counts, p95 latency per route, and the slowest route."""
    counts = Counter(route for route, _ in pairs)
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        if latency_ms < 0:
            raise ValueError("Latency must not be negative.")
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}

    for route, values in latencies.items():
        values.sort()
        rank = ceil(0.95 * len(values))
        p95[route] = values[rank - 1]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
