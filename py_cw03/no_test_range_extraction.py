from range_extraction2 import solution

def ntest_single():
    integers = [1]
    assert solution(integers) == '1'

def test_two_nums():
    integers = [1, 2]
    assert solution(integers) == '1,2'
    integers = [-21, -20]
    assert solution(integers) == '-21,-20'

def test_one_range():
    integers = [1, 2, 3]
    assert solution(integers) == '1-3'

    integers = [1, 2, 3, 4]
    assert solution(integers) == '1-4'

def test_mixed_range():
    integers = [-1, 2, 3, 4, 15]
    assert solution(integers) == '-1,2-4,15'
    integers = [-3, -2, -1, 4, 5, 10, 11, 12]
    assert solution(integers) == '-3--1,4,5,10-12'
    integers = [-3, -2, -1, 4, 5, 10, 11, 12, 98, 99]
    assert solution(integers) == '-3--1,4,5,10-12,98,99'

def test_even():
    integers = [2,4,6,8,10]
    assert solution(integers) == '2,4,6,8,10'
