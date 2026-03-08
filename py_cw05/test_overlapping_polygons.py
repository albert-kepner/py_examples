from overlapping_polygons import *

from fractions import Fraction



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

def test_04():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    print('')
    for p3 in [pt(0,2), pt(0,10), pt(5,10), pt(10, 10), pt(20,10), pt(20, 1), pt(20, 0), pt(20, -10)]:
        # print(f'{type(p1)=} {type(p2)=} {type(p3)=}')
        # print(f'{p1}, {p2}, {p3}')
        angle = signed_angle_ab_to_bc(p1, p2, p3)
        print(f'angle: {angle}')

def test_05():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    print('')
    for p3 in [pt(0,2), pt(0,10), pt(5,10), pt(10, 10), pt(20,10), pt(20, 1), pt(20, 0)]:
        # print(f'{type(p1)=} {type(p2)=} {type(p3)=}')
        # print(f'{p1}, {p2}, {p3}')
        angle = signed_angle_ab_to_ac(p2, p1, p3)
        print(f'angle: {angle}')

def test_06():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    print('')
    for p3 in [pt(0,2), pt(0,10), pt(5,10), pt(10, 10), pt(20,10), pt(20, 1), pt(20, 0), pt(20, -10)]:
        p3 = (p3[0], -p3[1])
        angle = signed_angle_ab_to_bc(p1, p2, p3)
        print(f'angle: {angle}')

def test_07():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    p3 = pt(5, 10)
    p4 = pt(0,0)
    poly1: CoordList = [p1, p2, p3, p4]
    cw = is_clockwise(poly1)
    print(f'cw: {cw}')
    poly1.reverse()
    cw = is_clockwise(poly1)
    print(f'cw: {cw}')

def test_08():
    poly1 = [pt(0,5), pt(10,0), pt(10,10), pt(0,5)]
    poly2 = [pt(5,0),pt(5,10), pt(15, 5), pt(5, 0)]
    intersect = find_intersections(poly1, poly2)
    print_intersections(poly1, poly2, intersect)


def test_09():
    poly1 = [pt(0,5), pt(10,0), pt(10,10), pt(0,5)]
    poly2 = [pt(5,0),pt(5,10), pt(15, 5), pt(5, 0)]
    pass

