import pytest


__results__ = {
    0: 1,
    1: 1,
    2: 1,
    3: 1
}

__n_primes__ = {}

def count_primes(n: int):
    """Counts the number of primes less or equal n using Eratostane's sieve

    Args:
        n (int): integer

    Returns:
        _type_: number of primes less than n
    """
    if n <= 1:
        return 0

    if n in __n_primes__:
        return __n_primes__[n]

    is_prime = [1] * (n + 1)
    is_prime[0] = is_prime[1] = 0

    p = 2
    while p * p <= n:
        if is_prime[p] > 0:
            for multiple in range(p * p, n+1, p):
                is_prime[multiple] = 0
        p += 1

    __n_primes__[n] = sum(is_prime)
    return __n_primes__[n]


def count_arrangements(n: int):
    """Count possible arrangements of infinite blocks (4x1) or (1x4) in a (4xN) rectangle

    Args:
        n (int): the width of the rectangle
    """
    def recursive_call(m):
        res = 0

        if m in __results__:
            res += __results__[m]
        else:
            # add a brick vertically
            res += recursive_call(m-1)

            # add brick horizonatally
            if m >= 4:
                res += recursive_call(m - 4)

            __results__[m] = res
        return res

    res = recursive_call(n)
    return res

def red_john(n: int):
    return count_primes(count_arrangements(n))

@pytest.mark.parametrize(
    "n, expected",
    [(5, 2), (7, 3), (10, 6), (14, 15)]
)
def test_red_john(n: int, expected: int):
    assert red_john(n) == expected