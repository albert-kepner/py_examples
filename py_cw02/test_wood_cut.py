from wood_cut import wood_cut

def test01():
    assert_equals(wood_cut([232, 124, 456], 7), 114)
    assert_equals(wood_cut([232, 124, 456], 20), 38)
    assert_equals(wood_cut([232, 124, 456], 1), 456)
    assert_equals(wood_cut([232, 124, 456], 2), 232)
    assert_equals(wood_cut([232, 124, 456], 3), 228)
    assert_equals(wood_cut([1, 1, 1], 4), 0)
    assert_equals(wood_cut([1, 1, 1], 3), 1)
    assert_equals(wood_cut([200000000, 2147483645, 2147483646, 2147483647], 4), 1073741823)
    assert_equals(wood_cut([2000000000, 2147483645, 2147483646, 2147483647], 4), 2000000000)

def assert_equals(n1, n2):
    assert n1 == n2