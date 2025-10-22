from conftest import load_func
longest_word = load_func(6, "longest_word")

def test_basic():
    assert longest_word("The quick brown fox") == "quick"

def test_tie_break():
    assert longest_word("one three five") in ["three", "five"]

def test_single_word():
    assert longest_word("hello") == "hello"


def test_punctuation():
    assert longest_word("a... bb, ccc!") == "ccc"


