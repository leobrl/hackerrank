import pytest
import numpy as np


def stock_max(prices: list[int]):
    ret = 0

    left, right = [], prices
    while len(right) > 0:
        m = max(right)
        m_idx = right.index(m)
        left, right = right[:m_idx+1], right[m_idx+1:]
        ret += -sum(left[:-1]) + left[-1] * (len(left) - 1)

    return ret


def stock_max_naive(prices: list[int]):

    def _recursive_call(prices, v=0, s=0):
        if not prices:
            return v

        current, *prices = prices
        return max(
            _recursive_call(prices, v = v-current, s = s + 1),
            _recursive_call(prices, v=v, s=s),
            _recursive_call(prices, v=v+s*current, s = 0)
        )

    ret = _recursive_call(prices)
    return ret



@pytest.mark.parametrize(
    "prices, expected_ret",
    [
        ([1, 2], 1),
        ([2, 1], 0),
        ([5, 3, 2], 0),
        ([1, 2, 100], 197),
        ([1, 3, 1, 2], 3),
        ([0, 0, 0], 0)
    ]
)
def test_stock_max(prices, expected_ret):
    assert stock_max(prices=prices) == expected_ret


def test_against_naive():
    rng = np.random.default_rng(1)

    for i in range(50):
        prices = list(rng.integers(low=1, high=100, size=10))

        assert stock_max(prices) == stock_max_naive(prices), f"Error: {i}"


if __name__ == "__main__":
    test_against_naive()


# Run test from cmd:
# python -m pytest ./Stock_Max/stock_max.py
