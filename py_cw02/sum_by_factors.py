def prime_sieve(max):
    primes = [2]
    for p in range(3, max + 1, 2):
        if test_prime(p, primes):
            primes.append(p)
    return primes


def test_prime(p, primes):
    for tp in primes:
        if p % tp == 0:
            return False
    return True


def sum_for_p(p, lst):
    total = 0
    for i in lst:
        if i % p == 0:
            total += i
    return total


def sum_for_list(lst: list[int]):
    amax = max(lst)
    amin = min(lst)
    max_ij = max(amax, -amin)

    primes = prime_sieve(max=max_ij)
    prime_set = set()
    for ij in lst:
        for p in primes:
            if ij % p == 0:
                prime_set.add(p)
    prime_list = list(prime_set)
    prime_list.sort()
    result = [[p, sum_for_p(p, lst)] for p in prime_list]
    return result
