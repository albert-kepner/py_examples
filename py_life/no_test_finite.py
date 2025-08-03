from finite_life import next_gen, count_neighbors

def test_print():
    input = [[1, 0], [1, 1]]
    output = next_gen(input)
    print('\n')
    print(input)
    print('\n')
    print(output)


def test_diag_01():
    input = [[1, 0], [0, 1]]
    output = next_gen(input)
    print('\n')
    print(input)
    print('\n')
    print(output)


def test_blinker():
    input = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],]
    output = next_gen(input)
    print('\n')
    print(input)
    print('\n')
    print(output)

