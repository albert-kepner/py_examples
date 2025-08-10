def sum_for_list(lst: list[int]):
    dict1: dict[int, int] = dict()
    for i in lst:
        factors = prime_factors_of(i)
        for f in factors:
            s = dict1.get(f, 0)
            dict1[f] = i + s
    result1 = [(k,v) for k,v in dict1.items()]
    result1.sort()
    result2 = [[k,v] for k,v in result1]
    return result2

PRIMES = []

def prime_generator():
    global PRIMES
    PRIMES.append(2)
    yield 2
    for i in range(3, 1000000, 2):
        for p in PRIMES:
            if i % p == 0:
                break
            if p * p > i:
                PRIMES.append(i)
                yield i
                break

GEN = prime_generator()

def prime_gen():
    global GEN
    global PRIMES
    index = 0
    while True:
        if index >= len(PRIMES):
            next(GEN)
        prime_at_index = PRIMES[index]
        yield prime_at_index
        index += 1

def prime_factors_of(i: int) -> list[int]:
    remaining = i
    gen = prime_gen()
    p = next(gen)
    factors = []
    while p <= abs(remaining):
        if remaining % p == 0:
            factors.append(p)
            while remaining % p == 0:
                remaining = remaining / p
        p = next(gen)
    return factors





