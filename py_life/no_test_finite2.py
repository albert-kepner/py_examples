from finite_life2 import next_gen

def test_print():
    input1 = [[1, 0], [1, 1]]
    output = next_gen(input1)
    print('\n')
    print(input1)
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

