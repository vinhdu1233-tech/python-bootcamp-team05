
def summary(grades: list[float]) -> dict[str, float | int]:
    """Return the minimum, maximum, mean and median of grades."""
    if not grades:
        raise ValueError("grades must not be empty")

    ordered = sorted(grades)
    count = len(ordered)

    middle = count // 2
    if count % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2

    return {
        "min": min(ordered),
        "max": max(ordered),
        "mean": round(sum(ordered) / count, 2),
        "median": median,
    }
