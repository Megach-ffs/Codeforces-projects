def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def generate_prime_permutation(n):
    # Simple strategy: place larger numbers strategically
    perm = list(range(1, n+1))
    
    # Attempt to maximize prime cumulative sums
    def check_cumulative_primes(p):
        cumulative = 0
        prime_count = 0
        for num in p:
            cumulative += num
            if is_prime(int(cumulative + 0.5)):  # Ceiling rounding
                prime_count += 1
        return prime_count >= (n // 3 - 1)
    
    # Try different permutations
    from itertools import permutations
    
    for p in permutations(range(1, n+1)):
        if check_cumulative_primes(p):
            return list(p)
    
    return None  # No valid permutation found

def solve_test_cases(test_cases):
    results = []
    for n in test_cases:
        result = generate_prime_permutation(n)
        results.append(result)
    return results

# Example usage
test_cases = [100]
solutions = solve_test_cases(test_cases)
print(solutions)
