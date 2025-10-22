from conftest import load_func
count_primes_upto = load_func(10, "count_primes_upto")

def test_small():
    assert count_primes_upto(10) == 4  # 2,3,5,7

def test_zero_one():
    assert count_primes_upto(1) == 0

def test_large():
    assert count_primes_upto(20) == 8  # 2,3,5,7,11,13,17,19
