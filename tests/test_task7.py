from conftest import load_func
is_balanced_parentheses = load_func(7, "is_balanced_parentheses")

def test_true():
    assert is_balanced_parentheses("([]{})") is True

def test_false_missing():
    assert is_balanced_parentheses("((()]") is False

def test_empty():
    assert is_balanced_parentheses("") is True
