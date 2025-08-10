from sum_by_factors2 import prime_factors_of,  prime_gen

def no_test_primes_01():
    print('')
    for limit in range(5, 20, 5):
        p2 = prime_gen()
        for i in range(limit):
            print(next(p2))

def test_factors():
    for i in range(100):
        factors = prime_factors_of(i)
        print(f'{i=} {factors=}')
