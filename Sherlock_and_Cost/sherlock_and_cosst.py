import pytest
import numpy as np


def cost(arr: list[int]) -> int:

    def get_cost(_arr):

        k = 0
        while k < len(_arr):
            if _arr[k] != 1:
                break
            k += 1

        _arr = _arr[max(0, k - 1) :]

        res = [[0, 0, 0] for _ in range(len(_arr))]
        for i, e1 in enumerate(_arr[1:], start=0):
            e0 = _arr[i]
            v0 = abs(e0 - 1)
            v1 = abs(1 - e1)

            res[i + 1][0] = res[i][1] + v0
            res[i + 1][1] = max(res[i][0] + v1, res[i][2] + v1)
            res[i + 1][2] = res[i][0]

        return res

    res = get_cost(arr)

    return max(res[-1])


def cost_naive(arr):

    list_arrays = []
    res = 0
    max_array = []

    def _get_cost(_arr, i, other):
        nonlocal res, list_arrays, max_array
        if len(other) == len(_arr):
            list_arrays.append(other)
            _res = 0
            for i, e in enumerate(other[1:]):
                _res += abs(other[i] - e)
            if _res == res and res > 0:
                max_array.append(other)
            elif _res > res:
                res = _res
                max_array = [other]
            return

        for k in range(1, _arr[i] + 1):
            _get_cost(_arr, i + 1, other + [k])

    _get_cost(arr, 0, [])

    return res


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 2),
        ([10, 1, 10, 1, 10], 36),
        ([8, 6, 5, 3, 3], 17),
        ([6, 9, 5, 6, 9], 26),
        ([8, 2, 1, 8, 1], 21),
        ([1, 1, 1, 2, 8], 7),
        ([5, 1, 3, 5, 4], 12),
        ([3, 9, 3, 3, 7], 22),
        ([1, 6, 6, 9, 3], 26),
        ([1, 1, 5, 5, 5, 7], 16),
    ],
)
def test_cost(arr: list[int], expected: int):
    assert cost(arr) == expected


def test_cost_against_naive():
    rng = np.random.default_rng(0)

    for i in range(100):
        v = rng.integers(low=1, high=10, size=6)
        res_1 = cost(v)
        res_2 = cost_naive(v)
        assert res_1 == res_2, f"ERROR {i}: {v}"


# Run test from cmd:
# python -m pytest ./Sherlock_and_Cost/sherlock_and_cosst.py
