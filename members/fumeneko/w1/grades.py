def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Scores list cannot be empty.")
    
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": round(float(median), 2)
    }
