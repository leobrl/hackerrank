import pytest


def highest_value_palindrome(s: str, n: int, k: int) -> str:
    """Find the largest palindrome that can be generated
    by changing at most k digits in the input number

    Args:
        s (str): the input number
        n (int): the number of digits in s
        k (int): the number of changes that are allowed

    Returns:
        str: the palindrome number or -1, if a palindrome cannot be generated
    """
    s = list(map(int, list(s)))
    modified = [0] * len(s)

    # first pass
    i, j = 0, n - 1
    while k > 0 and i < j:
        if i != j:
            if s[i] != s[j]:
                s[i] = s[j] = max(s[i], s[j])
                k -= 1
                modified[i] = 1

        i, j = i + 1, j - 1

    # second pass
    i, j = 0, n - 1
    while k > 0 and i <= j:
        if i == j:
            if s[i] != 9 and k >= 1:
                s[i] = 9
        else:
            m = modified[i] + modified[j]
            if s[i] != 9 and k >= (2 - m):
                s[i] = s[j] = 9
                k -= 2 - m

        i, j = i + 1, j - 1

    return "".join(map(str, s)) if s == s[::-1] else "-1"


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("100", 2, "909"),
        ("3943", 1, "3993"),
        ("092282", 3, "992299"),
        ("0011", 1, "-1"),
    ],
)
def test_highest_value_palindrome(s: str, k: int, expected: str):
    """_summary_

    Args:
        s (str): the input number
        k (int): the number of changes that are allowed
        expected (str): the expected result
    """
    actual = highest_value_palindrome(s, len(s), k)
    assert actual == expected


# Run test from cmd:
# python -m pytest ./Highest_Value_Palindrome/highest_value_palindrome.py
