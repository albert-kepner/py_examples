from puzzle_solve import slide_puzzle

puzzle2a = [
    [3, 1],
    [2, 0],
]

puzzle2b = [
    [3, 2],
    [1, 0],
]

puzzle1 = [
    [4, 1, 3],
    [2, 8, 0],
    [7, 6, 5]
]
puzzle2 = [
    [10, 3, 6, 4],
    [1, 5, 8, 0],
    [2, 13, 7, 15],
    [14, 9, 12, 11]
]
puzzle3 = [
    [3, 7, 14, 15, 10],
    [1, 0, 5, 9, 4],
    [16, 2, 11, 12, 8],
    [17, 6, 13, 18, 20],
    [21, 22, 23, 19, 24]
]

puzzle_bad = [
    [0, 1, 8],
    [7, 5, 3],
    [4, 2, 6],
]


def test_slide():
    answer = slide_puzzle(puzzle1)
    print(f'Answer: {answer}')
    answer = slide_puzzle(puzzle2)
    print(f'Answer: {answer}')
    answer = slide_puzzle(puzzle3)
    print(f'Answer: {answer}')
    answer = slide_puzzle(puzzle2a)
    print(f'Answer: {answer}')
    answer = slide_puzzle(puzzle2b)
    print(f'Answer: {answer}')

def test_bad():
    answer = slide_puzzle(puzzle_bad)
    print(f'Answer: {answer}')