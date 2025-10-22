def count_primes_upto(n):
    if n < 2:
        return 0
    
    # Sieve of Eratosthenes
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    # Count the number of True values
    count = 0
    for prime_check in is_prime:
        if prime_check:
            count += 1
            
    return count