from fractions import Fraction
from math import atan2, degrees
from typing import Any

Point = tuple[Fraction, Fraction]
Segment = tuple[Point, Point]
CoordList = list[Point]

f = Fraction
s = Segment


def pt(x: int, y: int) -> Point:
    return f(x), f(y)


def merge_polygons(poly1: CoordList, poly2: CoordList) -> CoordList:
    if is_clockwise(poly1):
        poly1.reverse()
    if is_clockwise(poly2):
        poly2.reverse()

    return []


def is_clockwise(poly1: CoordList) -> bool:
    """Returns True iff the poly1 closed ploygon has coordinates sequenced in a clock-wise rotation, False otherwise."""
    # The polygon should be closed, which implies the first and last Point should be the same.
    assert poly1[0] == poly1[-1]
    pt_minus1 = None
    pt_minus2 = None
    total_rotation = 0
    for ix, pt0 in enumerate(poly1):
        if pt_minus2:
            angle = signed_angle_ab_to_bc(pt_minus2, pt_minus1, pt0)
            total_rotation += angle
        pt_minus2 = pt_minus1
        pt_minus1 = pt0

    return total_rotation < 0


def find_intersections(poly1: CoordList, poly2: CoordList) -> list[tuple[Segment, Point]]:
    intersections = []
    assert poly1[0] == poly1[-1]
    assert poly2[0] == poly2[-1]
    pt1_prev = None
    # poly1b = poly1.copy()
    # poly1b.append(poly1[1])
    ## print('')
    ## print(f'{poly1b=}')
    # poly2b = poly2.copy()
    # poly2b.append(poly2[1])
    ## print(f'{poly2b=}')
    ## print('')
    for pt1 in poly1:

        if pt1_prev:
            a = (pt1_prev, pt1)
            pt2_prev = None
            for pt2 in poly2:
                if pt2_prev:
                    b = (pt2_prev, pt2)
                    if segments_might_cross(a, b):
                        cross_point = segment_intersection(a, b)
                        if cross_point:
                            intersections.append((a, cross_point))
                            ## print_intersections(intersections, f'{pt1=} {pt2=}')
                            intersections.append((b, cross_point))
                            ## print_intersections(intersections, f'{pt1=} {pt2=}')
                            ## print('')
                pt2_prev = pt2

        pt1_prev = pt1
    return intersections


def insert_crossing_points(poly1: CoordList, poly2: CoordList, cross_pts: list[tuple[Segment, Point]]):
    print('')
    for ix, int1 in enumerate(cross_pts):
        seg, pt1 = int1
        pt_after = seg[0]
        print(f'{ix=}: seg: {pseg(seg)} pt1: {pf(pt1)}')
        if ix % 2 == 0:
            ## insert into poly1
            i = poly1.index(pt_after)
            print(f'{i=} poly1 before: {print_poly(poly1)}')
            poly1.insert(i+1, pt1)
            print(f'{i=} poly1 after: {print_poly(poly1)}')
        else:
            ## insert into poly2
            i = poly2.index(pt_after)
            poly2.insert(i+1, pt1)


def print_intersections(intersections: list[tuple[Segment, Point]], label: str = None) -> None:
    if label:
        print(label)
    for ix, int1 in enumerate(intersections):
        print(f'{ix}: {int1_to_str(int1)}')


def pf(p1: Point) -> tuple[float, float]:
    return float(p1[0]), float(p1[1])

def pseg(seg: Segment) -> tuple[Any, Any]:
    return pf(seg[0]), pf(seg[1])

def print_poly(poly1: CoordList) -> str:
    return " ".join([str(pf(x)) for x in poly1])


def int1_to_str(int1: tuple[Segment, Point]) -> str:
    seg1, p1 = int1
    pa, pb = seg1
    return f'seg: {(pf(pa), pf(pb))} => {pf(p1)}'


## Given two line segments, each represented by a tuple of two points,
## determine whether the line segments might, possibly cross and return True iff their boundary boxes overlap.
def segments_might_cross(a: tuple[Point, Point], b: tuple[Point, Point]) -> bool:
    a_x1, a_y1 = a[0]
    b_x1, b_y1 = b[0]
    a_x2, a_y2 = a[1]
    b_x2, b_y2 = b[1]
    a_xmin = min(a_x1, a_x2)
    a_ymin = min(a_y1, a_y2)
    a_xmax = max(a_x1, a_x2)
    a_ymax = max(a_y1, a_y2)
    b_xmin = min(b_x1, b_x2)
    b_ymin = min(b_y1, b_y2)
    b_xmax = max(b_x1, b_x2)
    b_ymax = max(b_y1, b_y2)
    xmin = max(a_xmin, b_xmin)
    ymin = max(a_ymin, b_ymin)
    xmax = min(a_xmax, b_xmax)
    ymax = min(a_ymax, b_ymax)
    if xmin <= xmax and ymin <= ymax:
        return True
    else:
        return False


from fractions import Fraction

Point = tuple[Fraction, Fraction]


def segment_intersection(seg1: Segment, seg2: Segment) -> Point | None:
    p1, p2 = seg1
    p3, p4 = seg2
    return segment_intersection_pts(p1, p2, p3, p4)


def segment_intersection_pts(p1: Point, p2: Point, p3: Point, p4: Point) -> Point | None:
    """
    Exact intersection of segments p1->p2 and p3->p4 using Fraction arithmetic.

    Returns:
        Point (Fraction, Fraction) if the intersection is a single point (including endpoints),
        None if disjoint OR collinear-overlap (infinitely many intersection points).
    """

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    def cross(ax: Fraction, ay: Fraction, bx: Fraction, by: Fraction) -> Fraction:
        return ax * by - ay * bx

    def dot(ax: Fraction, ay: Fraction, bx: Fraction, by: Fraction) -> Fraction:
        return ax * bx + ay * by

    def point_on_segment(p: Point, a: Point, b: Point) -> bool:
        (px, py), (ax, ay), (bx, by) = p, a, b
        # Collinear?
        if cross(bx - ax, by - ay, px - ax, py - ay) != 0:
            return False
        # Within bounding box (exact)
        return (min(ax, bx) <= px <= max(ax, bx)) and (min(ay, by) <= py <= max(ay, by))

    # r = p2 - p1, s = p4 - p3
    rx, ry = x2 - x1, y2 - y1
    sx, sy = x4 - x3, y4 - y3

    # Handle degenerate segments (points)
    if rx == Fraction(0) and ry == Fraction(0):
        return p1 if point_on_segment(p1, p3, p4) else None
    if sx == Fraction(0) and sy == Fraction(0):
        return p3 if point_on_segment(p3, p1, p2) else None

    # q - p
    qpx, qpy = x3 - x1, y3 - y1

    rxs = cross(rx, ry, sx, sy)
    qpxr = cross(qpx, qpy, rx, ry)

    # Parallel lines?
    if rxs == Fraction(0):
        # Collinear?
        if qpxr == Fraction(0):
            # Project segment2 endpoints onto segment1 and check interval overlap
            rr = dot(rx, ry, rx, ry)  # > 0 because not degenerate here
            t0 = dot(x3 - x1, y3 - y1, rx, ry) / rr
            t1 = dot(x4 - x1, y4 - y1, rx, ry) / rr
            tmin, tmax = (t0, t1) if t0 <= t1 else (t1, t0)

            # Disjoint collinear
            if tmax < 0 or tmin > 1:
                return None

            # Collinear overlap => infinitely many intersection points
            return None
        else:
            return None  # parallel non-collinear

    # Non-parallel: solve p + t r = q + u s
    t = cross(qpx, qpy, sx, sy) / rxs
    u = cross(qpx, qpy, rx, ry) / rxs

    if Fraction(0) <= t <= Fraction(1) and Fraction(0) <= u <= Fraction(1):
        return (x1 + t * rx, y1 + t * ry)

    return None


def signed_angle_ab_to_bc(a: Point, b: Point, c: Point) -> float:
    angle = 180 + signed_angle_ab_to_ac(b, a, c)
    if angle > 180:
        angle = angle - 360
    return angle


def signed_angle_ab_to_ac(a: Point, b: Point, c: Point) -> float:
    """
    Signed angle in degrees from segment ab to segment ac.
    CCW is positive, CW is negative.
    Returned range: [-180, 180).

    Points are (Fraction, Fraction).
    """
    ax, ay = a
    bx, by = b
    cx, cy = c

    # Vectors from a
    v1x, v1y = bx - ax, by - ay  # ab
    v2x, v2y = cx - ax, cy - ay  # ac

    if (v1x == 0 and v1y == 0) or (v2x == 0 and v2y == 0):
        raise ValueError("Angle is undefined when a==b or a==c (zero-length segment).")

    # Exact rationals
    dot: Fraction = v1x * v2x + v1y * v2y
    cross: Fraction = v1x * v2y - v1y * v2x

    # atan2 needs floats; convert at the last moment
    ang = degrees(atan2(float(cross), float(dot)))  # (-180, 180]

    # Normalize boundary to keep [-180, 180)
    if ang == 180.0:
        ang = -180.0
    return ang
