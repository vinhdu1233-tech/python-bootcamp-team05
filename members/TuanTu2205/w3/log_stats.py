from collections import Counter, defaultdict
from math import ceil, isfinite


def analyse(
    pairs: list[tuple[str, float]],
) -> dict[str, dict[str, int] | dict[str, float] | str | None]:
    counts: Counter[str] = Counter()
    groups: dict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        if not isinstance(route, str) or not route.strip():
            raise ValueError("Route must be a non-empty string")

        if (
            isinstance(latency_ms, bool)
            or not isinstance(latency_ms, (int, float))
            or not isfinite(latency_ms)
            or latency_ms < 0
        ):
            raise ValueError("Latency must be finite and non-negative")

        counts[route] += 1
        groups[route].append(latency_ms)

    p95: dict[str, float] = {}

    for route, values in groups.items():
        ordered = sorted(values)
        index = ceil(0.95 * len(ordered)) - 1
        p95[route] = float(ordered[index])

    slowest = (
        min(p95, key=lambda route: (-p95[route], route))
        if p95 else None
    )

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
