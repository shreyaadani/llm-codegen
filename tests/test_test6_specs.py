import pytest
from conftest import load_func

longest_word = load_func(6, "longest_word")


def test_longest_word_empty_string_spec():
    assert longest_word("") == ""


def test_longest_word_no_alphanumeric_spec():
    assert longest_word("!!! ??? ,,,") == ""


def test_longest_word_single_word_spec():
    assert longest_word("Hello") == "Hello"


def test_longest_word_punctuation_ignored_spec():
    result = longest_word("hello,world! wow.")
    assert result in {"hello", "world"}


def test_longest_word_tie_lengths_spec():
    result = longest_word("alpha beta gamma")
    assert result in {"alpha", "gamma"}


def test_longest_word_digits_only_spec():
    assert longest_word("123 45 6789") == "6789"


def test_longest_word_mixed_alphanumeric_spec():
    assert longest_word("id1234 x99 abc") == "id1234"


def test_longest_word_irregular_spacing_spec():
    assert longest_word("   many   spaces   here   ") == "spaces"

def test_longest_word_case_preserved_spec():
    assert longest_word("a ABCDE bb") == "ABCDE"


def test_longest_word_mixed_separators_spec():
    result = longest_word("one,two;three:four")
    assert result in {"three", "four"}
