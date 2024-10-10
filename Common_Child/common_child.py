import pytest
import numpy as np
from functools import lru_cache


def common_child_naive(s1: str, s2: str):

    res = 0

    @lru_cache
    def recursive_call(_s1: str, _s2: str, counter):
        nonlocal res

        if not _s1 or not _s2:
            res = max(res, counter)
            return

        if _s1[0] in _s2:
            idx = _s2.index(_s1[0])
            recursive_call(_s1[1:], _s2[idx + 1 :], counter + 1)

        recursive_call(_s1[1:], _s2, counter)

        if _s2[0] in _s1:
            idx = _s1.index(_s2[0])
            recursive_call(_s2[1:], _s1[idx + 1 :], counter + 1)

        recursive_call(_s1, _s2[1:], counter)

    recursive_call(s1, s2, 0)

    return res


def common_child(s1: str, s2: str) -> int:
    s1 = list(s1)
    s2 = list(s2)
    n = len(s1)

    matrix = [[0] * (n + 1) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

    return matrix[n - 1][n - 1]


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("abcd", "abdc", 3),
        ("harry", "sally", 2),
        ("aa", "bb", 0),
        ("shinchan", "noharaaa", 3),
        ("noharaaa", "shinchan", 3),
        ("abcdef", "fbdamn", 2),
        ("fbdamn", "abcdef", 2),
        ("jrnuj", "nrvuj", 3),
        ("wqnhibbaev", "qxnpzsqooy", 2),
    ],
)
def test_common_child(s1, s2, expected):
    actual = common_child(s1, s2)
    assert actual == expected


def test_common_child_against_naive():
    rng = np.random.default_rng(0)

    for i in range(100):

        s1 = "".join(map(chr, rng.integers(low=97, high=123, size=10)))
        s2 = "".join(map(chr, rng.integers(low=97, high=123, size=10)))
        expected = common_child_naive(s1, s2)
        res = common_child(s1, s2)

        assert expected == res, f"ERROR {i} {s1} {s2}"


# Run test from cmd:
# python -m pytest ./Common_Child/common_child.py
