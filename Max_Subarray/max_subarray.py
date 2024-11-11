import pytest
import numpy as np
from itertools import combinations

def max_subsequence(arr):
    positive_sum = sum(x for x in arr if x > 0)
    if positive_sum == 0:
        return max(arr)
    else:
        return positive_sum


def max_subarray(arr):
    n = len(arr)
    i = 0

    max_s = min(arr)
    s = 0
    while i < n:
        s = s + arr[i]

        if s > max_s:
            max_s = s

        if s < 0:
            s = 0

        i += 1

    return max_s


def max_subarray_subsequence(arr):
    return max_subarray(arr), max_subsequence(arr)


def max_subarray_naive(arr):

    m = min(arr)
    for l in range(1, len(arr)+1):
        for s in range(len(arr)-l+1):
            v = sum(arr[s: s + l])
            if v > m:
                m = v

    return m


def max_subsequence_naive(arr):
    m = min(arr)
    for l in range(1, len(arr)+1):
        for c in combinations(arr, l):
            v = sum(c)
            if v > m:
                m = v

    return m


def test_max_subarray():
    n = 10
    rng = np.random.default_rng(0)

    for t in range(1000):
        arr = rng.integers(low=-100, high=100, size=n)
        assert max_subarray_naive(arr) == max_subarray(arr), f"Error: {t}"


def test_max_subsequence():
    n = 10
    rng = np.random.default_rng(0)

    for t in range(1000):
        arr = rng.integers(low=-100, high=100, size=n)
        assert max_subsequence_naive(arr) == max_subsequence(arr), f"Error: {t}"


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, -1, 2, 3, 4, -5], (10, 11)),
        ([-2, -3, -1, -4, -6], (-1, -1)),
        ([1,2,3,4], (10, 10))
    ]
)
def test_max_subarray_subsequence(arr, expected):
    assert max_subarray_subsequence(arr) == expected


if __name__ == "__main__":
    # #-2 -3 -1 -4 -6
    # values = [2, -1, 2, 3, 4, -5]
    # # values = [-2, -3, -1, -4, -6]
    # a, b = max_subarray_subsequence(values)
    # print(a, b)

    test_max_subsequence()


# Run test from cmd:
# python -m pytest ./Max_Subarray/max_subarray.py
