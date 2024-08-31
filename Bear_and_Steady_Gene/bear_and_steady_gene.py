from itertools import chain
from collections import Counter, deque

import numpy as np
import pytest


def find_min_substring(string: list[str], sub_string: list[str]) -> tuple[int, int]:
    """Finds the shortest ofsubstring of string that contains all letters in sub_string,
    in no particular order

    Args:
        string (list[str]): the string, as a list
        sub_string (list[str]): the letters that must be part of the substring

    Returns:
       tuple[int, int]:: start and end of the substring so that substring = string[start:end]
    """
    if not sub_string:
        return 0, 0

    to_find = Counter(sub_string)
    founded = {k: 0 for k in string}

    # initial substring
    def initialize_histogram():
        end, n = 0, 0

        while end < len(string):
            e = string[end]
            if to_find[e] > 0:
                founded[e] += 1
                if founded[e] <= to_find[e]:
                    n += 1

            if n == len(sub_string):
                break

            end += 1
        return end

    def find_min_length():
        nonlocal end, start

        min_len = end - start + 1
        while start < len(string):
            s = string[start]
            if (to_find[s] == 0) or (founded[s] > to_find[s]):
                start += 1
                if to_find[s] > 0:
                    founded[s] -= 1
            else:
                end += 1
                if end >= len(string):
                    break
                e = string[end]
                founded[e] += 1 if to_find[e] > 0 else 0

            length = (end - start) + 1
            if length < min_len:
                min_len = length

        return start, end + 1

    start = 0
    end = initialize_histogram()

    start, end = find_min_length()

    return start, end


def steady_gene_min_sub_string(gene: str) -> tuple[int, int]:
    """solve the steady gene problem

    Args:
        gene (str): a string of length n, where n is divisible by 4.
        It only contains the letters A, C, G T.

    Returns:
        tuple[int, int]: the start and the end (non inclusive) of the shortest string
    """
    gene = list(gene)
    bases = Counter(gene)

    m = len(gene) // 4
    bases_to_remove = [(v, bases[v] - m) for v in set(gene) if bases[v] - m > 0]

    target = list(chain(*[[b] * n for b, n in bases_to_remove]))

    start, end = find_min_substring(gene, target)

    return start, end


def steady_gene(gene: str) -> int:
    """Find the length of the smallest substring to replace in gene
    so that all bases occurs exactly the same number of times.

    Args:
        gene (str): a string of length n, where n is divisible by 4.
        It only contains the letters A, C, G T.

    Returns:
        int: the length of the shortest string
    """
    start, end = steady_gene_min_sub_string(gene)

    return end - start


@pytest.mark.parametrize(
    "n_tests, gene_len",
    [
        (100, 4),       # cornercases
        (5, 500_000), # stress test
        (1000, 100)     # general
    ]
)
def test_steady_gene_impl_with_random_input(n_tests: int, gene_len: int):
    """Parameterized test of steady_gene_min_sub_string

    Args:
        n_tests (int): the number of random strings to generate
        gene_len (int): the length of the random string
    """
    rng = np.random.default_rng(0)
    bases = ["A", "T", "G", "C"]
    for _ in range(n_tests):
        gene = "".join(rng.choice(bases, size=gene_len, replace=True))
        start, end = steady_gene_min_sub_string(gene)

        gene = list(gene)
        bases_count = Counter(gene)
        expected_m = len(gene) // 4
        bases_to_add = deque(
            chain(
                *[
                    [v] * (expected_m - bases_count[v])
                    for v in bases
                    if bases_count[v] - expected_m < 0
                ]
            )
        )
        bases_to_remove = list(
            chain(
                *[
                    [v] * (bases_count[v] - expected_m)
                    for v in set(gene)
                    if bases_count[v] - expected_m > 0
                ]
            )
        )
        for i, e in enumerate(gene[start : end + 1], start=start):
            if e in bases_to_remove:
                bases_to_remove.remove(e)
                gene[i] = bases_to_add.pop()

        counter = Counter(gene)
        for x in set(gene):
            assert counter[x] == expected_m

# Run test from cmd:
# python -m pytest ./Bear_and_Steady_Gene/bear_and_steady_gene.py
