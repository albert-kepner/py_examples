from equal_to_24 import equal_to_24


def test_1_1_1_13():
    val = equal_to_24(1, 1, 1, 13)
    assert not val.startswith('It')

## a=48,b=33,c=22,d=8
def test_48_33_22_8():
    val = equal_to_24(48, 33, 22, 8)
    print(val)
    assert not val.startswith('It')

def test_21_32_46_26():
    val = equal_to_24(21,32,46,26)
    print(val)
    assert not val.startswith('It')


def test_positive():
    tests = [
        print(f'{equal_to_24(1, 2, 3, 4)=}'),
        print(f'{equal_to_24(2, 3, 4, 5)=}'),
        print(f'{equal_to_24(3, 4, 5, 6)=}'),
        print(f'{equal_to_24(13, 13, 6, 12)=}'),
        print(f'{equal_to_24(2, 7, 7, 13)=}'),
        print(f'{equal_to_24(4, 3, 1, 6)=}'),
    ]

def test_bad():
    assert equal_to_24(1,1,1, 1) == "It's not possible!"
