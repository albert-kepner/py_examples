def apply_tuple(n, tup):
    n_digits = list(str(n))
    i = tup[0]
    j = tup[1]
    digit_i = n_digits.pop(i)
    n_digits.insert(j, digit_i)
    new_str = ''.join(n_digits)
    new_n = int(new_str)
    return new_n


def smallest(n):
    n_str = str(n)
    n_digits = list(n_str)
    n_len = len(n_digits)
    tuples = [(i, j) for i in range(n_len) for j in range(n_len)]
    tuples = sorted(tuples, key=lambda x: x[0] + x[1])
    min_value = n
    min_tuple = tuples[0]
    for ix, tup in enumerate(tuples):
        n2 = apply_tuple(n, tup)
        if n2 < min_value:
            min_value = n2
            min_tuple = tup
    return [min_value, min_tuple[0], min_tuple[1]]
