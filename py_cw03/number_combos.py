def pairs_in_combo(combo):
    pairs = set()
    for ix, item in enumerate(combo):
        next = combo[ix + 1] if ix < len(combo) - 1 else None
        if next:
            pair = (item, next)
            pairs.add(pair)
    return pairs


def replace_pair(combo, pair):
    # first locate the position of the pair
    for ix in range(len(combo) - 1, 0, -1):
        next = combo[ix]
        previous = combo[ix - 1]
        ## print(f'{next=} {previous=} {pair=}')
        if pair == (previous, next):
            combo[ix - 1: ix + 1] = [ next + previous ]
            combo.sort()
            return tuple(combo)


def add_next_gen(all_combos):
    new_combos = set()
    for combo in all_combos:
        pairs = pairs_in_combo(combo)
        for pair in pairs:
            new_combo = replace_pair(list(combo), pair)
            new_combos.add(new_combo)
    all_combos.update(new_combos)


def combos(n):

    if n == 1:
        return [[1]]
    all_combos = set()
    all_ones = [1] * n
    all_ones = tuple(all_ones)
    all_combos.add(all_ones)

    count = len(all_combos)

    while True:
        add_next_gen(all_combos)
        new_count = len(all_combos)
        if new_count == count:
            break
        else:
            count = new_count
    mylist = [list (t) for t in all_combos]
    mylist.sort()
    return mylist


