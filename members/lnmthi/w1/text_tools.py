def word_count(text: str) -> dict[str, int]:
    text = text.lower()

    for punctuation in ".,!?:;":
        text = text.replace(punctuation, "")

    words = text.split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    result = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return result[:max(0, k)]


if __name__ == "__main__":
    text = "Git is fun. Git is fast!"
    print(word_count(text))
    print(top_k(text, 2))
