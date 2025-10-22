from conftest import load_func
f = load_func(4, "are_anagrams")

a, b = "Debit Card", "Bad Credit"
print("Loaded from:", f.__code__.co_filename)
print("Function output:", f(a, b))

print("Processed s1:", ''.join(c.lower() for c in a if c.isalnum()))
print("Processed s2:", ''.join(c.lower() for c in b if c.isalnum()))
print("Sorted s1:", sorted(''.join(c.lower() for c in a if c.isalnum())))
print("Sorted s2:", sorted(''.join(c.lower() for c in b if c.isalnum())))
