import numpy as np
import pytest


def minimum_loss(numbers: list[int]) -> int:
    """Find the minimum positive difference prices[i] - prices[j] with j > i

    Args:
        prices (list[int]): list of integers

    Returns:
        int: the minimum positive difference
    """
    res = 10**10

    numbers = sorted(list(enumerate(numbers)), key=lambda x: x[1])

    for sell, buy in zip(numbers[:-1], numbers[1:]):
        if sell[0] > buy[0] and buy[1] - sell[1] < res:
            res = buy[1] - sell[1]

    return res


def minimum_loss_naive(numbers: list[int]) -> int:
    """Naive implementation of minimu loss

    Args:
        numbers (list[int]): list of integers

    Returns:
        int: the minimum positive difference
    """
    res = 10**10
    for i, buy in enumerate(numbers):
        for sell in numbers[i:]:
            v = buy - sell
            if v > 0 and v < res:
                res = v

    return res


@pytest.mark.parametrize("n_tests, max_price, size", [(100, 100, 20)])
def test_minimum_loss(n_tests: int, max_price: int, size: int):
    """Test minimum loss against naive implementatioj

    Args:
        n_tests (int): the number of random test cases
        max_price (int): the maximum price
        size (int): the length of the price time series
    """
    rng = np.random.default_rng(0)

    prices_range = list(range(1, max_price))
    for i in range(n_tests):
        print(f"test {i}")
        rng.shuffle(prices_range)
        prices = list(prices_range[:size])
        res = minimum_loss(prices)
        expected = minimum_loss_naive(prices)

        assert res == expected, f"ERROR {i}"


# Run test from cmd:
# python -m pytest ./Minimum_Loss/minimum_loss.py
