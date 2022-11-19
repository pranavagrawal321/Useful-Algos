import math


def sieve(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, math.isqrt(n)):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    return list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(is_prime))))
