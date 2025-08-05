from recover_secret import recover_secret

def test01():
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]
    result = recover_secret(triplets)
    print(result)
    assert result == 'whatisup'


def test02():
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's']
    ]
    result = recover_secret(triplets)
    print(result)
    assert result == 'whatisup'
