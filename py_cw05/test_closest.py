from closest import closest_pair

points1 = \
(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
points2 = \
[(2, 2), (2, 8), (5, 5), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9)]


def verify(points, expected):
  actual = closest_pair(points)
  if not actual or len(actual) != 2 or not all(pt and isinstance(pt, tuple) and len(pt) == 2 for pt in actual):
    raise  TypeError(f"Output should be a tuple or list of tuples: ((a,b), (x,y)), but got {actual}")
  else:
    exp, act = (sorted(stuff) for stuff in (expected, actual))
    assert exp == act

def test_1():
  expected = ((6, 3), (7, 4))
  verify(points1, expected)
  expected = ((5, 5), (5, 5))
  verify(points2, expected)
