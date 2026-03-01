from count_components import components

grid_01 = \
"""+--+--+--+
|  |  |  |
+--+--+--+
|  |  |  |
+--+--+--+
"""

grid_02 = \
"""+--+--+--+
|  |     |
+  +--+--+
|  |  |  |
+--+--+--+
"""

def test_01():
    print(components(grid_01))

def test_02():
    print(components(grid_02))
