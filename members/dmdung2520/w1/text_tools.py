
def word_count(text: str) -> dict[str, int]:
    words = text.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words, sorted by count then alphabetically."""
    if k < 0:
        raise ValueError("k must be non-negative")
    counts = word_count(text)
    ranked = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )
    return ranked[:k]


if __name__ == "__main__":
    text = "Git is fun. Git is fast!"
    print("Word counts:", word_count(text))
    print("Top 2:", top_k(text, 2))
