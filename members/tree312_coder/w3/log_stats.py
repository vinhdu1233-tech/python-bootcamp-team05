
"""Week 3-2: Analyse chat request latency."""

import math
from collections import Counter, defaultdict


def analyse(
    pairs: list[tuple[str, float]],
) -> dict:
    """Calculate route counts, p95 latency and slowest route."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        if not math.isfinite(latency) or latency < 0:
            raise ValueError("Latency must be finite and non-negative")

        counts[route] += 1
        latencies[route].append(latency)

    p95: dict[str, float] = {}

    for route, values in latencies.items():
        sorted_values = sorted(values)

        rank = math.ceil(0.95 * len(sorted_values))
        p95[route] = sorted_values[rank - 1]

    if p95:
        slowest = min(
        p95,
        key=lambda route: (-p95[route], route),
    )
    else:
        slowest = None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
