from integer_partitions import partitions

def test_1_to_25():
    for n in range(1, 77, 1):
    # for n in [1, 2]:
        p = partitions(int(n))
        msg = f'{n=} {p=}'
        print(msg)