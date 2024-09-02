import pytest


big_number = 10**9 + 7


def lego_blocks(n: int, m: int) -> int:
    """Calculates the number of vways we can build a wall of height n and width m
    with an infinite number of lego block (1x1), (1x2), (1x3) and (1x4) so that
    there is no vertical cut through the wall

    Args:
        n (int): height
        m (int): width

    Returns:
        int: the number of valid wall formations modulus 10**9 + 7
    """

    N = m + 1
    f = [0] * N
    g = [0] * N
    h = [0] * N

    f[0], g[0], h[0] = 1, 1, 1
    for i in range(1, N):
        for k in [1, 2, 3, 4]:
            if (i - k) >= 0:
                f[i] += f[i - k] % big_number

    for i in range(1, N):
        g[i] = pow(f[i], n, big_number)
        h[i] = g[i]

    for i in range(1, N):
        for j in range(1, i):
            h[i] -= h[j] * g[i - j]

        h[i] = h[i] % big_number

    return h[-1]


@pytest.mark.parametrize(
    "height, width, expected",
    [
        (2, 2, 3),
        (3, 2, 7),
        (2, 3, 9),
        (4, 4, 3375),
        (4, 5, 35714),
        (4, 6, 447902),
        (4, 7, 5562914),
        (5, 4, 29791),
        (6, 4, 250047),
        (7, 4, 2048383),
    ],
)
def test_lego_blocks(height: int, width: int, expected: int):
    """_summary_

    Args:
        height (int): height of the wall
        width (int): width of the wall
        expected (int): the correct output
    """
    actual = lego_blocks(height, width)
    assert actual == expected


# Run test from cmd:
# python -m pytest ./Lego_Blocks/lego_blocks.py
