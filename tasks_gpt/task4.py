def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    # Sort both strings and check if they are equal
    return sorted(s1) == sorted(s2)