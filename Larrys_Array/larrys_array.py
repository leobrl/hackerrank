import pytest


def larrys_array_inversion_trick(v: list[int]) -> str:
    """Solves larry's array by counting the number of inversions.
    How this works:
    1.  a sorted array as a zero number of inversions.
    2.  a rotation of a 3 element array is equivalent to two swaps. Thus any number of rotations
        will results in an even number of inversions

    Args:
        v (list[int]): list of integers between 1 and len(v) (included) in random order.

    Returns:
        str: "YES" if the list can be sorted by cycling terns of numbers, "NO" otherwise.
    """

    inversions = 0
    for i in range(1, len(v)):
        for j in range(0, i):
            if v[j] > v[i]:
                inversions += 1

    return "YES" if inversions % 2 == 0 else "NO"


def larrys_array(v: list[int]) -> str:
    """Decides if the input list can be sorted by cycling any 3 consecutive numbers any number of time.

    Args:
        v (list[int]): list of integers between 1 and len(v) (included) in random order.

    Returns:
        str: "YES" if the list can be sorted by cycling terns of numbers, "NO" otherwise.
    """
    i = 0
    while i < len(v):
        if v[i] == i + 1:
            i += 1
        else:
            j = i + 1
            while j < len(v) and v[j] != i + 1:
                j += 1

            while v[i] != i + 1:
                if j - i == 1:
                    idx1, idx2, idx3 = j - 1, j, j + 1
                else:
                    idx1, idx2, idx3 = j - 2, j - 1, j

                if idx3 >= len(v):
                    break

                v[idx1], v[idx2], v[idx3] = v[idx2], v[idx3], v[idx1]
                j -= 1
            i += 1

    for i, e in enumerate(v, start=1):
        if e != i:
            return "NO"

    return "YES"


@pytest.mark.parametrize(
    "v, expected",
    [
        ([1, 6, 5, 2, 4, 3], "YES"),
        ([3, 2, 1], "NO"),
        ([3, 1, 2], "YES"),
        ([1, 3, 4, 2], "YES"),
        (list(reversed(range(1, 1_000))), "NO"),
    ],
)
def test_larrys_array(v: list[int], expected: str):
    """Test larrys_array function

    Args:
        v (list[int]):  list of integers between 1 and len(v) (included) in random order.
        expected (str): expected result
    """
    res = larrys_array(v)
    assert res == expected


@pytest.mark.parametrize(
    "v, expected",
    [
        ([1, 6, 5, 2, 4, 3], "YES"),
        ([3, 2, 1], "NO"),
        ([3, 1, 2], "YES"),
        ([1, 3, 4, 2], "YES"),
        (list(reversed(range(1, 1_000))), "NO"),
    ],
)
def test_larrys_array_inversion_trick(v: list[int], expected: str):
    """Test larrys_array function

    Args:
        v (list[int]):  list of integers between 1 and len(v) (included) in random order.
        expected (str): expected result
    """
    res = larrys_array_inversion_trick(v)
    assert res == expected


# Run test from cmd:
# python -m pytest ./Larrys_Array/larrys_array.py
