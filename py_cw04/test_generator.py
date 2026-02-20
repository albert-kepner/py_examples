def test_gen():
    for i,j in pairs():
        print(f'{i},{j}')



def pairs():
    for i in range(4):
        for j in range(4):
            yield i, j