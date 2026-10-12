
def summary(scores: list[float]) -> dict:
    """Calculate the minimum, maximum, mean, and median of scores."""

    if not scores:
        raise ValueError("Scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(scores)

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        middle1 = sorted_scores[n // 2 - 1]
        middle2 = sorted_scores[n // 2]
        median = (middle1 + middle2) / 2

    median = round(median, 2)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median
    }
