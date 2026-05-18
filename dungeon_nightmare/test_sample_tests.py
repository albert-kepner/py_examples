from solution import analyze_dungeon

import pprint

dungeon1 = {
    "start": "A",
    "goal": "G",
    "doors": ["D1", "D2"],
    "rooms": {
        "A": {"keys": 0, "exits": [{"to": "B", "door": None}]},
        "B": {"keys": 1, "exits": [{"to": "A", "door": None}, {"to": "C", "door": "D1"}]},
        "C": {"keys": 1, "exits": [{"to": "B", "door": "D1"}, {"to": "G", "door": "D2"}]},
        "G": {"keys": 0, "exits": [{"to": "C", "door": "D2"}]}
    }
}

dungeon2 = {
    "start": "A",
    "goal": "G",
    "doors": ["D1", "D2"],
    "rooms": {
        "A": {"keys": 0, "exits": [{"to": "B", "door": None}]},
        "B": {"keys": 1, "exits": [{"to": "A", "door": None}, {"to": "C", "door": "D1"}, {"to": "D", "door": "D2"}]},
        "C": {"keys": 0, "exits": [{"to": "B", "door": "D1"}, {"to": "G", "door": None}]},
        "D": {"keys": 0, "exits": [{"to": "B", "door": "D2"}]},
        "G": {"keys": 0, "exits": []}
    }
}

dungeon3 = {
    "start": "A",
    "goal": "G",
    "doors": ["D1", "D2"],
    "rooms": {
        "A": {"keys": 0, "exits": [{"to": "B", "door": None}]},
        "B": {"keys": 1, "exits": [{"to": "A", "door": None}, {"to": "C", "door": "D1"}]},
        "C": {"keys": 0, "exits": [{"to": "B", "door": "D1"}, {"to": "G", "door": "D2"}]},
        "G": {"keys": 0, "exits": [{"to": "C", "door": "D2"}]}
    }
}

dungeon4 = {
    "start": "A",
    "goal": "G",
    "doors": ["D1", "D2", "D3", "D4"],
    "rooms": {
        "A": {"keys": 0, "exits": [{"to": "B", "door": None}]},
        "B": {"keys": 2, "exits": [{"to": "A", "door": None}, {"to": "C", "door": "D1"}]},
        "C": {"keys": 0, "exits": [{"to": "B", "door": "D1"}, {"to": "F", "door": "D2"}, {"to": "D", "door": None}]},
        "F": {"keys": 0, "exits": [{"to": "C", "door": "D2"}]},
        "D": {"keys": 0, "exits": [{"to": "E", "door": "D3"}, {"to": "G", "door": "D4"}, {"to": "C", "door": None}]},
        "E": {"keys": 0, "exits": [{"to": "D", "door": "D3"}]},
        "G": {"keys": 0, "exits": []}
    }
}

dungeon5 = {
    'start': 'A',
    'goal': 'L',
    'doors': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11'],
    'rooms': {
        'A': {'keys': 1, 'exits': [{'to': 'E', 'door': None}, {'to': 'F', 'door': 'D1'}, {'to': 'B', 'door': 'D2'}]},
        'B': {'keys': 0, 'exits': [{'to': 'F', 'door': None}, {'to': 'G', 'door': None}, {'to': 'A', 'door': 'D2'},
                                   {'to': 'I', 'door': 'D3'}, {'to': 'K', 'door': 'D6'}, {'to': 'L', 'door': 'D7'}]},
        'C': {'keys': 0, 'exits': [{'to': 'G', 'door': None}, {'to': 'D', 'door': None}, {'to': 'K', 'door': 'D9'}]},
        'D': {'keys': 0, 'exits': [{'to': 'G', 'door': None}, {'to': 'C', 'door': None}, {'to': 'J', 'door': 'D11'}]},
        'E': {'keys': 0, 'exits': [{'to': 'G', 'door': None}, {'to': 'A', 'door': None}, {'to': 'F', 'door': None}]},
        'F': {'keys': 2, 'exits': [{'to': 'E', 'door': None}, {'to': 'B', 'door': None}, {'to': 'J', 'door': None},
                                   {'to': 'A', 'door': 'D1'}, {'to': 'K', 'door': 'D8'}]},
        'G': {'keys': 0, 'exits': [{'to': 'E', 'door': None}, {'to': 'D', 'door': None}, {'to': 'C', 'door': None},
                                   {'to': 'B', 'door': None}, {'to': 'I', 'door': 'D5'}]},
        'H': {'keys': 0, 'exits': [{'to': 'J', 'door': None}, {'to': 'I', 'door': 'D4'}]},
        'I': {'keys': 0, 'exits': [{'to': 'L', 'door': None}, {'to': 'B', 'door': 'D3'}, {'to': 'H', 'door': 'D4'},
                                   {'to': 'G', 'door': 'D5'}, {'to': 'J', 'door': 'D10'}]},
        'J': {'keys': 0, 'exits': [{'to': 'H', 'door': None}, {'to': 'F', 'door': None}, {'to': 'I', 'door': 'D10'},
                                   {'to': 'D', 'door': 'D11'}]},
        'K': {'keys': 0, 'exits': [{'to': 'B', 'door': 'D6'}, {'to': 'F', 'door': 'D8'}, {'to': 'C', 'door': 'D9'}]},
        'L': {'keys': 0, 'exits': [{'to': 'I', 'door': None}, {'to': 'B', 'door': 'D7'}]}
    }
}
dungeon6 = {
    'start': 'A',
    'goal': 'L',
    'doors': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11'],
    'rooms': {
        'A': {'keys': 1, 'exits': [{'to': 'E', 'door': None}, {'to': 'F', 'door': 'D1'}, {'to': 'B', 'door': 'D2'}]},
        'B': {'keys': 0, 'exits': [{'to': 'F', 'door': None}, {'to': 'G', 'door': None}, {'to': 'A', 'door': 'D2'},
                                   {'to': 'I', 'door': 'D3'}, {'to': 'K', 'door': 'D6'}, {'to': 'L', 'door': 'D7'}]},
        'C': {'keys': 0, 'exits': [{'to': 'G', 'door': None}, {'to': 'D', 'door': None}, {'to': 'K', 'door': 'D9'}]},
        'D': {'keys': 0, 'exits': [{'to': 'G', 'door': None}, {'to': 'C', 'door': None}, {'to': 'J', 'door': 'D11'}]},
        'E': {'keys': 0, 'exits': [{'to': 'G', 'door': None}, {'to': 'A', 'door': None}, {'to': 'F', 'door': None}]},
        'F': {'keys': 2, 'exits': [{'to': 'E', 'door': None}, {'to': 'B', 'door': None}, {'to': 'J', 'door': None},
                                   {'to': 'A', 'door': 'D1'}, {'to': 'K', 'door': 'D8'}]},
        'G': {'keys': 0, 'exits': [{'to': 'E', 'door': None}, {'to': 'D', 'door': None}, {'to': 'C', 'door': None},
                                   {'to': 'B', 'door': None}, {'to': 'I', 'door': 'D5'}]},
        'H': {'keys': 0, 'exits': [{'to': 'J', 'door': None}, {'to': 'I', 'door': 'D4'}]},
        'I': {'keys': 0, 'exits': [{'to': 'L', 'door': None}, {'to': 'B', 'door': 'D3'}, {'to': 'H', 'door': 'D4'},
                                   {'to': 'G', 'door': 'D5'}, {'to': 'J', 'door': 'D10'}]},
        'J': {'keys': 0, 'exits': [{'to': 'H', 'door': None}, {'to': 'F', 'door': None}, {'to': 'I', 'door': 'D10'},
                                   {'to': 'D', 'door': 'D11'}]},
        'K': {'keys': 0, 'exits': [{'to': 'B', 'door': 'D6'}, {'to': 'F', 'door': 'D8'}, {'to': 'C', 'door': 'D9'}]},
        'L': {'keys': 0, 'exits': [{'to': 'I', 'door': None}, {'to': 'B', 'door': 'D7'}]}
    }
}
def mytest_assert_equals(actual, expected, dungeon):
    print(dungeon)
    assert actual == expected


def test_example_tests():
    print("Dungeon 1")
    def test_dung1():
        mytest_assert_equals(analyze_dungeon(dungeon1), (True, True), f"Input: {pprint.pformat(dungeon1, width=200)}\n")

    print("Dungeon 2")
    def test_dung2():
        mytest_assert_equals(analyze_dungeon(dungeon2), (True, False), f"Input: {pprint.pformat(dungeon2, width=200)}\n")

    print("Dungeon 3")
    def test_dung3():
        mytest_assert_equals(analyze_dungeon(dungeon3), (False, False), f"Input: {pprint.pformat(dungeon3, width=200)}\n")

    print("Dungeon 4")
    def test_dung4():
        mytest_assert_equals(analyze_dungeon(dungeon4), (True, False), f"Input: {pprint.pformat(dungeon4, width=200)}\n")

    print("Dungeon 5")
    def test_dung5():
        mytest_assert_equals(analyze_dungeon(dungeon5), (True, False), f"Input: {pprint.pformat(dungeon5, width=200)}\n")

    print("Dungeon 6")
    def test_dung6():
        mytest_assert_equals(analyze_dungeon(dungeon6), (True, False), f"Input: {pprint.pformat(dungeon6, width=200)}\n")
    test_dung1()
    test_dung2()
    test_dung3()
    test_dung4()
    test_dung5()
    test_dung6()

    