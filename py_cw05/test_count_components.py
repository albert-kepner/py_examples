from count_components import components





def no_test_01():
    grid_01 = """+--+--+--+
    |  |  |  |
    +--+--+--+
    |  |  |  |
    +--+--+--+
    """
    print(components(grid_01))

def no_test_02():
    grid_02 = """+--+--+--+
    |  |     |
    +  +--+--+
    |  |  |  |
    +--+--+--+
    """
    print(components(grid_02))

def test_03():
    grid_03 = """+--+--+--+
|  |     |
+  +  +--+
|        |
+--+--+--+
"""
    c = components(grid_03)
    print(f'{c=}')
    assert c == [(6, 1)]