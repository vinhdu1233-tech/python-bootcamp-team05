"""Week 3-2: per-route chat request counts and latency statistics."""

from collections import Counter, defaultdict
from math import ceil, isfinite
from typing import Iterable


def analyse(
    pairs: Iterable[tuple[str, float]],
) -> dict[str, dict[str, int] | dict[str, float] | str | None]:
    """Return counts, nearest-rank p95 latency by route, and slowest route.

    The nearest-rank 95th percentile is the item at rank ceil(0.95 * n)
    in the sorted values (one-based). Equal worst p95 values choose the
    alphabetically first route. Empty input has no slowest route.

    Raises:
        ValueError: If a latency is negative or not finite.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        if not isfinite(latency_ms) or latency_ms < 0:
            raise ValueError("Latency must be a finite, nonnegative number")
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}
    for route, values in latencies.items():
        ordered = sorted(values)
        index = ceil(0.95 * len(ordered)) - 1
        p95[route] = ordered[index]

    slowest = max(sorted(p95), key=p95.__getitem__) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
