
def is_palindrome(text: str) -> bool:
    """Check whether text reads the same forwards and backwards.

    Unlike the original C++ sorting task, this function checks a string
    and returns a boolean instead of sorting a list.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("madam"))  # True
    print(is_palindrome("hello"))  # False
    print(is_palindrome("A man, a plan, a canal: Panama!"))  # True
    print(is_palindrome(""))  # True
