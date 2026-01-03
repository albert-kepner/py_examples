from nonogram_encoder import encode

test_tuple_sizes = (
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
)

my_nonogram = (
    (0, 0, 0, 1, 0, 0, 0, 1, 1, 0),
    (0, 0, 1, 1, 1, 0, 1, 1, 1, 1),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 0),
    (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 1, 1, 0, 0),
    (1, 0, 1, 0, 0, 0, 1, 1, 0, 0),
    (1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
    (1, 1, 1, 0, 0, 1, 1, 1, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)


def test1():
    print(f'{len(test_tuple_sizes)=}')
    print(f'{len(test_tuple_sizes[0])=}')

def test2():
    print(encode(my_nonogram))
