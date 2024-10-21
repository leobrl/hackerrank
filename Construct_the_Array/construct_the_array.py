import pytest
import numpy as np


def count_array(n, k, x):

    BIG_NUMBER = 10**9 + 7

    res = k - 1 if x == 1 else k - 2

    v = 1 - k if x == 1 else 1

    for i in range(1, n - 2):
        res = (res * (k - 1)) % BIG_NUMBER
        res += -v if i % 2 == 0 else v
        res = res % BIG_NUMBER

    return res


def count_array_naive(n, k, x):

    count = 0

    def _add(arr):
        nonlocal count
        if len(arr) == n:
            if arr[-1] == x:
                count += 1
            return

        prev = arr[-1]
        for i in range(1, k + 1):
            if i != prev:
                _add(arr + [i])

    _add([1])
    return count


@pytest.mark.parametrize(
    "data, expected",
    [
        ((4, 3, 2), 3),
        ((5, 3, 2), 5),
        ((4, 4, 1), 6),
        ((3, 2, 1), 1),
        ((3, 4, 2), 2),
        ((8, 7, 4), 39991),
        [(10_000, 10_000, 1000), 259150193],
    ],
)
def test_count_array(data, expected):
    actual = count_array(*data)
    assert actual == expected


def _test_count_array_against_naive():
    rng = np.random.default_rng(1)

    m = 10
    for i in range(50):

        n = rng.integers(low=3, high=m)
        k = rng.integers(low=2, high=m)
        x = rng.integers(low=1, high=k)

        actual = count_array(n, k, x)
        expected = count_array_naive(n, k, x)

        assert actual == expected, f"ERROR at {i} for count_array({n}, {k}, {x})."


# Run test from cmd:
# python -m pytest ./Construct_the_Array/construct_the_array.py
