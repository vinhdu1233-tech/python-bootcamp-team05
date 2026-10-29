def word_count(text: str) -> dict[str, int]:
    """Count the frequency of each word in a given text."""
    text = text.lower()

    for mark in ".,!?;:":
        text = text.replace(mark, " ")

    words = text.split()
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, sorted by count and name."""
    if k < 0:
        return []

    counts = word_count(text)

    ordered = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0]),
    )

    return ordered[:k]
