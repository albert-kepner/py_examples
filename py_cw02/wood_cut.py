BACKOFF = 0.8

def wood_cut(woods, n):
    total = sum(woods)
    upper_bound = total//n
    lower_bound = 0
    if is_valid(woods, 1, n):
        lower_bound = 1
    converged = False
    while not converged:
        try_length = int(BACKOFF * (upper_bound - lower_bound) + lower_bound)
        if try_length == upper_bound:
            try_length -= 1
        if upper_bound - lower_bound <= 1:
            if is_valid(woods, lower_bound + 1, n):
                lower_bound += 1
            print(f'BEST Length: {lower_bound}')
            return lower_bound
        valid = is_valid(woods, try_length, n)
        ## print(f'{try_length=} {valid=}')
        if valid:
            lower_bound = try_length
        else:
            upper_bound = try_length
        if upper_bound - lower_bound <= 1:
            if is_valid(woods, lower_bound + 1, n):
                lower_bound += 1
            if is_valid(woods, lower_bound + 1, n):
                lower_bound += 1
            print(f'BEST Length: {lower_bound}')
            return lower_bound



def is_valid(woods, try_length, n):
    if try_length == 0:
        return True
    count = 0
    for wood in woods:
        count = count + wood//try_length
    return count >= n
