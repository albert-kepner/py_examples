from right_wrong_guess import guess_number, check_right_facts, check_wrong_facts, check_right_all_true, check_wrong_all_false


def test1():
    right = [
        'The number is an even number',
        'The number is divisible by 4',
        'The number is more than 10'
    ]
    wrong = [
        'The number is more than 20',
        'The number is divisible by 3',
        'The number is ending with 0'
    ]
    number = guess_number(right, wrong)
    assert number == 16

def test2():
    right = [
        "The number is more than 492",
        "The number is less than 1374",
        "The number is divisible by 11",
        "The number is divisible by 13",
        "The number is starting with 1",
        "The number is divisible by 7"
    ]
    wrong = []
    number = guess_number(right, wrong)
    assert number == 1001