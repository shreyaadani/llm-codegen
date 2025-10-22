from conftest import load_func
digital_root = load_func(3, "digital_root")

def test_basic():
    assert digital_root(9875) == 2  # 9+8+7+5=29 -> 2+9=11 -> 1+1=2

def test_single_digit():
    assert digital_root(9) == 9

def test_zero():
    assert digital_root(0) == 0
