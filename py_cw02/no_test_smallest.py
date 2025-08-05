from find_the_smallest import smallest

def test_smallest01():
    print('\n')

    n = 321
    result = smallest(n)
    print(f'{n=} {result=}')

    n = 123
    result = smallest(n)
    print(f'{n=} {result=}')

    n = 100
    result = smallest(n)
    print(f'{n=} {result=}')