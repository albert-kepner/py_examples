from battle1 import validate_battlefield, valid_group


def test1():
    b = [[1,1,1,0], [0,0,0,0], [0,0,1,1]]
    print (b)
    x = validate_battlefield(b)

def test2():
    bad1 = [(1,1),(3,1)]

    bad2 = [(1,1),(2,2)]

    bad3 = [(1,1),(4,1)]

    print(f'{bad1=} {valid_group(bad1)=}')
    print(f'{bad2=} {valid_group(bad2)=}')
    print(f'{bad3=} {valid_group(bad3)=}')

    good1 = [(77,77)]

    good2 = [(1,1),(2,1)]

    good3 = [(1,1),(2,1),(3,1),(4,1)]

    print(f'{good1=} {valid_group(good1)=}')
    print(f'{good2=} {valid_group(good2)=}')
    print(f'{good3=} {valid_group(good3)=}')

def test_battlefield():
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ok = validate_battlefield(battleField)
    assert ok