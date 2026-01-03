key_map: dict = {
    '0': '08',
    '1': '124',
    '2': '1235',
    '3': '236',
    '4': '1457',
    '5': '24568',
    '6': '3569',
    '7': '478',
    '8': '05789',
    '9': '689',
}

def get_pins(observed):
    positions = [None] * len(observed)
    out_array = []
    place_chars_at_level(0, observed, positions, out_array)
    return out_array

def place_chars_at_level(level, observed, positions, out_array):
    char_at_position = observed[level]
    for char in key_map[char_at_position]:
        positions[level] = char
        if level <= len(observed) - 2:
            place_chars_at_level(level + 1, observed, positions, out_array)
        else:
            trial_pin = "".join(positions)
            out_array.append(trial_pin)