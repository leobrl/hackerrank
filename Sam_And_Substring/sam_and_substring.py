import pytest
import numpy as np


def substrings(str_num: str) -> int:
    """Given a number as a string, determine the sum of all integer values of substrings of the string

    Args:
        str_num (str): an integer as a string

    Returns:
        int: the sum of integer substrings
    """

    BIG_NUMBER = 10**9 + 7
    n = len(str_num)

    powers = [1] * n
    for i in range(1, n):
        powers[i] = ((powers[i - 1] * 10) % BIG_NUMBER + 1) % BIG_NUMBER

    res = 0
    for i, m in enumerate(map(int, iter(str_num))):
        v = ((m * i + m) * powers[n - i - 1]) % BIG_NUMBER
        res = (res + int(v)) % BIG_NUMBER

    return int(res) % BIG_NUMBER


def substrings_naive(str_num: str) -> int:
    """Naive implementation of substrings

    Args:
        str_num (str): an integer as a string

    Returns:
        int: the sum of integer substrings
    """
    res = 0
    for i in range(0, len(str_num)):
        for j in range(i, len(str_num)):
            res += int(str_num[i : j + 1])

    return res


@pytest.mark.parametrize(
    "str_num, expected",
    [("16", 23), ("123", 164), ("404", 456), ("849", 1003), ("123456789", 167657325)],
)
def test_substrings(str_num, expected):
    """Test

    Args:
        str_num (_type_): the input number
        expected (_type_): the expected result
    """
    assert substrings(str_num) == expected


# Run test from cmd:
# python -m pytest ./Sam_And_Substring/sam_and_substring.py
