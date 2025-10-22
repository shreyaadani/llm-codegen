def count_palindromic_substrings(s):
    n = len(s)
    if n == 0:
        return 0
    count = 0
    for center in range(n):
        l = r = center
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        l, r = center, center + 1
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count