from conftest import load_func

are_anagrams = load_func(4, "are_anagrams")

def test_true():
    assert are_anagrams("listen", "silent")

def test_false():
    assert not are_anagrams("apple", "pale")

def test_case_insensitive():
    # Verifies ignoring spaces and case differences
    assert are_anagrams("Below", "Elbow")
