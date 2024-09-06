import pytest


def almost_sorted(arr: list[int]) -> str:
    """Determine if an array can be sorted swapping to elements or reversing a subarray.
    It assumes that len(arr) >= 2

    Args:
        arr (list[int]): list of integers.

    Returns:
        str: a string message with the solution.
    """
    sorted_arr = sorted(arr)

    res = None
    t = None
    l, r = -1, -1
    for i, v in enumerate(zip(arr, sorted_arr)):
        e, s = v
        if e != s:
            if l > 0 and r > 0:
                res = "no"
                break

            if l < 0:
                l, t = i, s
            else:
                if e == t:
                    r = i

    if not res:
        if l >= 0 and r >= 0:
            arr[l], arr[r] = arr[r], arr[l]

            if arr[l + 1 : r + 1] == sorted_arr[l + 1 : r + 1]:
                res = f"yes\nswap {l+1} {r+1}"
            elif (
                arr[l + 1 : r] == list(reversed(sorted_arr[l + 1 : r]))
                and arr[l + 1 : r]
            ):
                res = f"yes\nreverse {l+1} {r+1}"
            else:
                res = "no"
        else:
            res = "yes"

    return res


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 2], "yes\nswap 1 2"),
        ([3, 1, 2], "no"),
        ([1, 5, 4, 3, 2, 6], "yes\nreverse 2 5"),
        ([1, 3, 2, 4, 6, 5], "no"),
    ],
)
def test_almost_sorted(arr, expected):
    res = almost_sorted(arr)
    assert res == expected


# Run test from cmd:
# python -m pytest ./Almost_Sorted/almost_sorted.py
