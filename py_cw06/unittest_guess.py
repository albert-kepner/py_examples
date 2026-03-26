import unittest
from guess_a_number import guess_number


class TestGuessNumber(unittest.TestCase):

    def test_basic_even_divisible_by_4(self):
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
        self.assertEqual(guess_number(right, wrong), 16)

    def test_large_number_multiple_constraints(self):
        right = [
            "The number is more than 492",
            "The number is less than 1374",
            "The number is divisible by 11",
            "The number is divisible by 13",
            "The number is starting with 1",
            "The number is divisible by 7"
        ]
        wrong = []
        self.assertEqual(guess_number(right, wrong), 1001)

    def test_contradictory_clues_returns_none(self):
        right = [
            'The number is an even number',
            'The number is divisible by 4',
            'The number is more than 10'
        ]
        wrong = [
            'The number is an even number',
            'The number is more than 20',
            'The number is divisible by 3',
            'The number is ending with 0'
        ]
        self.assertEqual(guess_number(right, wrong), None)

    def test_ambiguous_returns_none(self):
        right = [
            'The number is an even number',
            'The number is divisible by 4'
        ]
        wrong = [
            'The number is divisible by 3'
        ]
        self.assertEqual(guess_number(right, wrong), None)

    def test_starting_with_5(self):
        right = ["The number is more than 0", "The number is less than 729", "The number is divisible by 5", "The number is starting with 5", "The number is divisible by 11"]
        wrong = ["The number is divisible by 8", "The number is starting with 4", "The number is divisible by 14", "The number is ending with 5"]
        self.assertEqual(guess_number(right, wrong), 550)

    def test_starting_with_1(self):
        right = ["The number is less than 631", "The number is starting with 1"]
        wrong = ["The number is less than 198", "The number is divisible by 15", "The number is divisible by 6"]
        self.assertEqual(guess_number(right, wrong), 199)

    def test_ending_with_6(self):
        right = ["The number is more than 396", "The number is divisible by 11", "The number is an even number", "The number is ending with 6"]
        wrong = ["The number is more than 725", "The number is divisible by 15", "The number is starting with 1", "The number is starting with 5"]
        self.assertEqual(guess_number(right, wrong), 616)


# argv=[''] prevents unittest from reading notebook args; exit=False prevents kernel shutdown
unittest.main(argv=[''], exit=False)

# Run one specific test by name
suite = unittest.TestLoader().loadTestsFromName('test_basic_even_divisible_by_4', TestGuessNumber)
unittest.TextTestRunner(verbosity=2).run(suite)
