import pytest
import numpy as np


def substrings(str_num: str):
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


def substrings_naive(str_num: str):
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
    assert substrings(str_num) == expected


# Run test from cmd:
# python -m pytest ./Sam_And_Substring/sam_and_substring.py
