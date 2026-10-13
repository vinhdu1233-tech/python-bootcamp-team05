import string

def word_count(text: str) -> dict:
    if not text or not text.strip():
        return {}
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    # Sắp xếp theo số lần xuất hiện giảm dần, nếu bằng nhau thì theo thứ tự bảng chữ cái
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]