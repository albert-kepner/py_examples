from finite_life3 import next_gen, get_generation

# def test_print3():
#     input1 = [[1, 0], [1, 1]]
#     output = next_gen(input1)
#     print('\n')
#     print(input1)
#     print('\n')
#     print(output)
#
#
# def test_diag_3():
#     input1 = [[1, 0], [0, 1]]
#     output = next_gen(input1)
#     print('\n')
#     print(input1)
#     print('\n')
#     print(output)
#
#
# def test_blinker3_0():
#     input1 = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],]
#     output = get_generation(input1,0)
#     print('\n')
#     print(input1)
#     print('\n')
#     print(output)
#
#
# def test_blinker3_1():
#     input1 = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],]
#     output = get_generation(input1,1)
#     print('\n')
#     print(input1)
#     print('\n')
#     print(output)
#
#
# def test_blinker3_2():
#     input1 = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],]
#     output = get_generation(input1,2)
#     print('\n')
#     print(input1)
#     print('\n')
#     print(output)

def test_blinker3_10():
    input1 = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],]
    for n in range(21):
        output = get_generation(input1,n)
        print('\n')
        print(output)

