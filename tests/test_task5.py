from conftest import load_func
intersection_sorted = load_func(5, "intersection_sorted")

def test_basic():
    assert intersection_sorted([1,2,3,4], [3,4,5,6]) == [3,4]

def test_duplicates():
    assert intersection_sorted([1,1,2,3], [1,2,2,3]) == [1,2,3]

def test_no_overlap():
    assert intersection_sorted([1,2], [3,4]) == []
