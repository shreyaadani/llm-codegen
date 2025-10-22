from conftest import load_func

count_palindromic_substrings = load_func(2, "count_palindromic_substrings")

def test_simple():
    assert count_palindromic_substrings("aaa") == 6   # "a","a","a","aa","aa","aaa"

def test_mixed():
    assert count_palindromic_substrings("abc") == 3   # each single letter

def test_empty():
    assert count_palindromic_substrings("") == 0
