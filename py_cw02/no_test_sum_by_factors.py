from sum_by_factors import prime_sieve, sum_for_list

def no_test_sieve():
    primes = prime_sieve(100)
    print(primes)

def test_sum_for_list():
    result = sum_for_list([12, 15])
    print('')
    print(result)
    a = [15, 21, 24, 30, 45]
    result = sum_for_list(a)
    print('')
    print(result)
