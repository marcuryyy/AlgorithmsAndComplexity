M, N = map(int, input().split())

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return is_prime


def find_min_k(N, M):
    max_limit = 2 * 10 ** 7
    is_prime = sieve_of_eratosthenes(max_limit)

    prime_count = [0] * (max_limit + 1)
    for i in range(1, max_limit + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    for K in range(2, max_limit + 1):
        if K + N - 1 > max_limit:
            break
        count_primes = prime_count[K + N - 1] - prime_count[K - 1]
        if count_primes == M:
            return K

    return -1


result = find_min_k(N, M)
print(result)
