import pytest


def radio_trasmitters(x: list[int], k: int) -> int:
    """Given a 1-D map, find the minimum number of transmitter that should be
    placed in the map so that all points are reached by the radio signal

    Args:
        x (list[int]): the map
        k (int): the transmitter range

    Returns:
        int: the number of transmitters
    """
    x = sorted(set(x))
    n = len(x)
    l, c, r = 0, 0, 0

    res = 0
    while c < n:
        while c + 1 < n and x[c + 1] - x[l] <= k:
            c = c + 1

        res += 1
        r = c

        while r + 1 < n and x[r + 1] - x[c] <= k:
            r = r + 1

        l, c, r = r + 1, r + 1, r + 1

    return res


@pytest.mark.parametrize(
    "x, k, expected",
    [
        ([1, 2, 3, 4, 5], 1, 2),
        ([7, 2, 4, 6, 5, 9, 12, 11], 2, 3),
        ([5, 4, 3, 2, 1], 1, 2),
    ],
)
def test_radio_trasmitter(x: list[int], k: int, expected: int):
    """Test radio_transmitter function against given testcases

    Args:
        x (list[int]): the map
        k (int): the transmitters range
        expected (int): the expected result.
    """
    actual = radio_trasmitters(x, k)
    assert actual == expected


# Run test from cmd:
# python -m pytest ./Hackerland_Radio_Transmitter/hackerland_radio_transmitter.py
