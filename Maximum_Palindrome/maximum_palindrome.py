import pytest
import numpy as np


class Cache:
    """Cache class to speed up repeated calculations."""

    __BIG_NUMBER__ = 10**9 + 7
    __WORD__ = None
    __COMULATIVE_COUNTER__ = None
    __FACTORIAL__ = None
    __INVERSE_FACTORIAL__ = None


def cached_recursive_factorial(word: str):
    """Fill __FACTORIAL__ and __INVERSE_FACTORIAL__ in cache

    Args:
        word (str): the problem input word
    """
    n = len(word) // 2 + 1

    Cache.__FACTORIAL__ = [1] * (n + 1)
    Cache.__INVERSE_FACTORIAL__ = [1] * (n + 1)
    for k in range(1, n + 1):
        Cache.__FACTORIAL__[k] = (
            (k) * Cache.__FACTORIAL__[k - 1]
        ) % Cache.__BIG_NUMBER__
        Cache.__INVERSE_FACTORIAL__[k] = pow(
            Cache.__FACTORIAL__[k], -1, Cache.__BIG_NUMBER__
        )


def set_comulative_counter(word: str):
    """Set __WORD__ and __COMULATIVE_COUNTER__ in cache
    __COMULATIVE_COUNTER__ contains comulative number of times a letter has been seen
    in word[:i]

    Args:
        word (str): the problem input word
    """
    comulative_counter = {}
    for i, e in enumerate(word):
        if e not in comulative_counter:
            comulative_counter[e] = [0] * (len(word) + 1)

        for v in comulative_counter.values():
            v[i + 1] = v[i]
        comulative_counter[e][i + 1] += 1

    Cache.__WORD__ = word
    Cache.__COMULATIVE_COUNTER__ = comulative_counter


def initialize(word: str):
    """Set the cache given for the problem input word.

    Args:
        word (str): the problem input word
    """
    cached_recursive_factorial(word)
    set_comulative_counter(word)


def answer_query(left: int, right: int) -> int:
    """Calculates the number of palindromes of maximum lenght that can be constructed with
    all letters in __WORD__[left-1: right]

    Args:
        left (int): start of the string as index starting from 1
        right (int): end of the string as index starting from 1

    Returns:
        int: the number of palindomes modulus __BIG_NUMBER__
    """

    m = 0
    odds = set()
    counter_palindrome = {}

    for c in Cache.__COMULATIVE_COUNTER__:
        n = (
            Cache.__COMULATIVE_COUNTER__[c][right]
            - Cache.__COMULATIVE_COUNTER__[c][left - 1]
        )
        if n == 0:
            continue

        if n >= 2:
            k = (n if n % 2 == 0 else n - 1) // 2
            counter_palindrome[c] = k
            m += k

        if n % 2 > 0:
            odds.add(c)

    # calc permutations
    den = 1
    num = Cache.__FACTORIAL__[m]
    for k in counter_palindrome.values():
        den *= Cache.__INVERSE_FACTORIAL__[k]

    res = int(
        (((num * den) % Cache.__BIG_NUMBER__) * max((1, len(odds))))
        % Cache.__BIG_NUMBER__
    )

    return res


@pytest.mark.parametrize(
    "word, left, right, expected",
    [
        ("aaaa", 1, 4, 1),
        ("abcd", 1, 4, 4),
        ("abcabcxyz", 1, 9, 18),
        ("madamimadam", 4, 7, 2),
        ("kthftvbbqiodvlwtrftbokyexcpowhwqwesxbjpcmptxkllxem", 2, 30, 262080),
        ("vpmghbbaeuqwmpyspnnxguqajvnatsvecvanchmkkaadaqnqgp", 20, 45, 10080),
    ],
)
def test_answer_query(word, left, right, expected):
    initialize(word)
    actual = answer_query(left, right)
    assert actual == expected


# Run test from cmd:
# python -m pytest ./Maximum_Palindrome/maximum_palindrome.py
