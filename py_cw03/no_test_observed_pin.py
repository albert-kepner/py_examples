from observed_pin import get_pins


def test_sample_tests():
    test_cases = [
        ('8', ['5', '7', '8', '9', '0']),
        ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', [
            "339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
            "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
            "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"
        ])
    ]

    for pin, expected in test_cases:
        print(f'Testing {pin}')
        out_array = get_pins(pin)
        out_array.sort()
        expected.sort()
        print('Expected:', expected)
        print('Got:', out_array)
        assert out_array == expected