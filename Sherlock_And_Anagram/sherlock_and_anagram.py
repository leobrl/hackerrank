import pytest
from collections import defaultdict

def sherlock_and_anagram(s: str):

    s = list(s)
    anagrams = 0
    for length in range(1, len(s)):
        counter = defaultdict(int)
        for start in range(len(s) - length + 1):
            key = "".join(sorted(s[start:start + length]))

            anagrams += counter[key]

            counter[key] += 1

    return anagrams


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abba", 4),
        ("kkkk", 10),
        ("ifailuhkqq", 3),
        ("cdcd", 5)
    ]
)
def test_sherlock_and_anagram(s, expected):
    actual = sherlock_and_anagram(s)
    assert actual == expected

# Run test from cmd:
# python -m pytest ./Sherlock_And_Anagram/sherlock_and_anagram.py
