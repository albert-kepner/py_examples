class C:
    def __init__(self, char, position):
        self.char = char
        self.weight = 0
        self.position = position

    char: str
    weight: int
    position: int

    def __str__(self):
        return f'char = {self.char}; weight = {self.weight} position = {self.position}'

    def __repr__(self):
        return f'char = {self.char}; weight = {self.weight} position = {self.position}'


def recover_secret(triplets) -> str:
    all_chars: set = { x for trips in triplets for x in trips}
    dict1: dict = { c: C(c, ix) for ix, c in enumerate(all_chars) }
    list1 = list( dict1.values() )
    list1.sort(key=lambda x: (x.weight, x.char))
    for ix,x in enumerate(list1):
        x.position=ix

    change: bool = True
    while change:
        change = False
        for trip in triplets:
            c0 = dict1[trip[0]]
            c1 = dict1[trip[1]]
            c2 = dict1[trip[2]]
            change |= check(c0,c1)
            change |= check(c1,c2)
            change |= check(c0,c2)
        list1.sort(key=lambda x: (x.weight, x.char))
        for ix, x in enumerate(list1):
            x.position = ix

    chars = [c.char for c in list1]
    secret = ''.join(chars)
    return secret
    # triplets is a list of triplets from the secret string. Return the string.

def check(c1: C, c2: C) -> bool:
    """
    If c1 is after c2 in sorted position,
    decrease the weight of c1 and increase the weight of c2
    :param c1:
    :param c2:
    :return True if the weight needed to change, else false:
    """
    change = False
    if c1.position > c2.position:
        c1.weight -= 1
        c2.weight += 1
        change = True
    return change
