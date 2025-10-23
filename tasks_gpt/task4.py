def are_anagrams(s1, s2):
    s1 = ''.join(c.lower() for c in s1 if c.isalnum())
    s2 = ''.join(c.lower() for c in s2 if c.isalnum())
    return sorted(s1) == sorted(s2)
