import pytest


class Constants:
    BIG_NUMBER = 10**9 + 7


def short_palindrome(s: str) -> int:
    """Calculates the number of 4-letter palindromes that can be constructed from
    a string s by taking any 4 letters in the same order as they appear in s.

    Args:
        s (str): the input string

    Returns:
        int: the number of palindromes modulus 10^9 + 7
    """

    s = list(s)
    set_s = set(s)
    n = len(set_s)
    m = dict(zip(set_s, range(n)))

    counter = [0] * n  # this keep tracks of the letters seen so far
    matrix = [
        [0] * n for _ in range(n)
    ]  # for each letter X this counts the number of times a letter appears before X
    almost_palindrome = [
        0
    ] * n  # this count the triplets of for xyy by incrementing by 1 the value at index x for each triplet.

    result = 0
    for e in s:
        idx = m[e]
        result += almost_palindrome[idx] % Constants.BIG_NUMBER

        for i, v in enumerate(matrix[idx]):
            almost_palindrome[i] += v # this works because if v > 0 it is at least the second time we have seen element e

        for i, v in enumerate(counter):
            matrix[idx][i] += v  # equivalent to adding 1 for every letter in s before e.

        counter[idx] += 1 # this is just to speed matrix update.

    return result % Constants.BIG_NUMBER


@pytest.mark.parametrize(
    "s, expected",
    [
        ("cbbaaaaaac", 31),
        ("caacabaabb", 8),
        ("cbbaaaaaacbcbbccbbbcaccabcbacc", 2727),
        ("caacabaabbbaaaacbbabcbbcccbccb", 2397),
        ("cccbcabccbbabbccacbbcbaacbbbcb", 3170),
        ("acaacbaabcbcaaccaacbbacbcccaca", 3101),
    ]
)
def test_short_palindrome(s, expected):
    actual = short_palindrome(s)
    assert actual == expected

# Run test from cmd:
# python -m pytest ./Short_Palindrome/short_palindrome.py
