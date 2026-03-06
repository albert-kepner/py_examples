from overlapping_polygons import (merge_polygons,
                                  segment_intersection,
                                  segment_intersection_pts,
                                  segments_might_cross,
                                  Point,
                                  Segment,
                                  CoordList,
                                  signed_angle_ab_to_ac,
                                  )

from fractions import Fraction

f = Fraction
s = Segment

def test_01():
    p1 = (f(0,1), f(0,1))
    p2 = (f(10,1), f(10,1))
    p3 = (f(0,1), f(10,1))
    p4 = (f(10,1), f(0,1))
    sa = (p1, p2)
    sb = (p3, p4)
    does_intersect = segment_intersection(sa, sb)
    assert does_intersect == (Fraction(5, 1), Fraction(5, 1))
    print(f'does_intersect: {does_intersect}')
    might_cross = segments_might_cross(sa, sb)
    print(f'might_cross: {might_cross}')
    angle = signed_angle_ab_to_ac(p1, p2, p3)
    print(f'angle: {angle}')
    angle = signed_angle_ab_to_ac(p1, p3, p2)
    print(f'angle: {angle}')


def test_02():
    p1 = (f(2), f(2))
    p2 = (f(7), f(6))
    p3 = (f(2), f(4))
    p4 = (f(7), f(8))
    sa = (p1, p2)
    sb = (p3, p4)
    does_intersect = segment_intersection(sa, sb)
    assert does_intersect == None
    print(f'does_intersect: {does_intersect}')
    might_cross = segments_might_cross(sa, sb)
    print(f'might_cross: {might_cross}')


def test_03():
    p1 = (f(2), f(1))
    p2 = (f(4), f(3))
    p3 = (f(2), f(6))
    p4 = (f(4), f(4))
    sa = (p1, p2)
    sb = (p3, p4)
    does_intersect = segment_intersection(sa, sb)
    assert does_intersect == None
    print(f'does_intersect: {does_intersect}')
    might_cross = segments_might_cross(sa, sb)
    print(f'might_cross: {might_cross}')
