from conftest import load_func
second_largest = load_func(9, "second_largest")

def test_basic():
    assert second_largest([1,2,3,4,5]) == 4

def test_with_duplicates():
    assert second_largest([5,5,5,4,3]) == 4

def test_two_elements():
    assert second_largest([10,20]) == 10
