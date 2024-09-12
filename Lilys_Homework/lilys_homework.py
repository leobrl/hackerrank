import pytest


def n_swaps_to_sort(arr: list[int], reverse: bool) -> int:
    """Calculates the number of swaps required to sort the input array
    in ascending or descending order. The input array is sorted in the process.

    Args:
        arr (list[int]): array of distinct numbers
        reverse (bool): if the array should be sorted ascending or descending

    Returns:
        int: the number of swaps required to sort the array
    """

    sorted_arr = sorted(arr, reverse=reverse)

    indices = {}
    for i, e in enumerate(arr):
        indices[e] = i

    res = 0
    i = 0
    while i < len(arr):
        w = arr[i]
        c = sorted_arr[i]

        if w != c:
            idx_c = indices[c]
            arr[i], arr[idx_c] = arr[idx_c], arr[i]
            indices[w] = idx_c
            res += 1
        i += 1

    return res


def lilys_homework(arr: list[int]) -> int:
    """Find the number of swaps required to minimize the sum of absolute difference of consecutive elements
    This can be done by checking the number of swaps required to sort the array in ascending or descending
    order and taking the minimum.

    Args:
        arr (list[int]): array of distinct numbers

    Returns:
        int: the number of swaps required to minimize the sum of absolute difference of consecutive elements
    """

    # Write your code here
    res_1 = n_swaps_to_sort(list(arr), reverse=False)
    res_2 = n_swaps_to_sort(list(arr), reverse=True)

    return min(res_1, res_2)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([7, 15, 12, 3], 2),
        ([2, 5, 3, 1], 2),
        ([25, 19, 15, 8, 9, 1, 2, 0, 5, 24], 7),
        ([17, 29, 1, 12, 20, 24, 28, 2, 28, 28], 4),
    ],
)
def test_lilys_homework(arr, expected):
    actual = lilys_homework(arr)
    assert actual == expected


# Run test from cmd:
# python -m pytest ./Lilys_Homework/lilys_homework.py
