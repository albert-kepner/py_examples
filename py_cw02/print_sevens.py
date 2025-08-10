def as_binary(n: int):
    if n < 0:
        raise ValueError(f'{n} must be non-negative int')
    remainder = n
    text = ''
    digit =  remainder % 2
    text += str(digit)
    while remainder > 0:
        remainder //= 2
        digit = remainder % 2
        text += str(digit)
    return text[::-1]


for i in range(240):
    s = 7 * i
    print(f'7 * {i} = {s} or binary {as_binary(s)}')



