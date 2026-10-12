
def word_count(text: str) -> dict[str, int]:
    """Count the occurrences of each word in a text."""

    text = text.lower()

    for punctuation in ".,!?;:":
        text = text.replace(punctuation, " ")

    words = text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, sorted alphabetically for ties."""

    counts = word_count(text)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:max(k, 0)]
