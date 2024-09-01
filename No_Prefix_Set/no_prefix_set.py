import pytest
import time
import numpy as np


ORD_A = ord("a")
N_LETTERS = 10


class Node:
    """Trie node"""

    def __init__(self, value):
        self.value = value
        self.nexts = [None] * N_LETTERS
        self.end_of_word = False


def no_prefix_impl(ws: list[str]) -> str:
    """Finds if any of the word in the given set is a prefix of another word in the same set.
    If none of the strings is a prefix it returns "GOOD SET", otherwise "BAD SET"

    Args:
        ws (list[str]): list of strings

    Returns:
        str: either "GOOD SET" or "BAD SET"
    """

    roots: list[Node | None] = [None] * N_LETTERS
    for w in ws:
        nexts = roots

        existing_word = True
        for v in (ord(x) - ORD_A for x in w):
            if nexts[v] is None:
                existing_word = False
                nexts[v] = Node(v)
            node = nexts[v]
            if node.end_of_word:
                return f"BAD SET\n{w}"

            nexts = node.nexts

        if existing_word:
            return f"BAD SET\n{w}"

        node.end_of_word = True

    return "GOOD SET"


def no_prefix(ws: list[str]):
    """Finds if any of the word in the given set is a prefix of another word in the same set.
    If none of the strings is a prefix it prints "GOOD SET", otherwise "BAD SET"

    Args:
        ws (list[str]): list of strings
    """
    print(no_prefix_impl(ws))


def no_prefix_naive(ws: list[str]) -> str:
    """Naive implementation of the prefix problem for testing the trie algorithm.
    Finds if any of the word in the given set is a prefix of another word in the same set.
    If none of the strings is a prefix it prints "GOOD SET", otherwise "BAD SET"

    Args:
        ws (list[str]): list of strings

    Returns:
        str: either "GOOD SET" or "BAD SET"
    """
    for i, w1 in enumerate(ws):
        for w2 in ws[i + 1 :]:
            if w1.startswith(w2) or w2.startswith(w1):
                return "BAD SET"

    return "GOOD SET"


@pytest.mark.parametrize(
    "n_tests, n_words, min_word_length, max_word_length",
    [
        (1000, 20, 5, 10),
        (100, 1000, 5, 10),
    ],
)
def test_no_prefix(
    n_tests: int, n_words: int, min_word_length: int, max_word_length: int
):
    """Test no_prefix_impl against a naive implementation. Note that the word that triggers a BAD SET
    can differ in the two implementations

    Args:
        n_tests (int): _description_
        n_words (int): _description_
        min_word_length (int): _description_
        max_word_length (int): _description_
    """

    rng = np.random.default_rng(0)
    letters = [chr(i) for i in range(ORD_A, ORD_A + N_LETTERS)]

    case_tested = set()
    for t in range(n_tests):
        words = [
            "".join(
                rng.choice(
                    letters,
                    size=rng.integers(low=min_word_length, high=max_word_length),
                    replace=True,
                )
            )
            for _ in range(n_words)
        ]

        expected = no_prefix_naive(words)
        actual = no_prefix_impl(words)

        case_tested.add(expected)

        idx_n = actual.find("\n")
        assert (
            expected == actual[: idx_n if idx_n > 0 else len(actual)]
        ), f"ERROR: test {t} fails"

    assert sorted(list(case_tested)) == ["BAD SET", "GOOD SET"]


def test_performance_no_prefix():
    """Test that largest input execute in reasonable time"""
    rng = np.random.default_rng(0)
    letters = [chr(i) for i in range(ORD_A, ORD_A + N_LETTERS)]

    words = [
        "".join(
            rng.choice(
                letters,
                size=rng.integers(low=30, high=60),
                replace=True,
            )
        )
        for _ in range(100_000)
    ]

    s = time.time()
    _ = no_prefix_impl(words)
    e = time.time()
    assert e - s < 10


# Run test from cmd:
# python -m pytest ./No_Prefix_Set/no_prefix_set.py
