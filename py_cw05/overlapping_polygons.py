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
    poly1.append(poly1[0])
    poly2.append(poly2[0])
    cycle = merge_polygons_V0(poly1, poly2)
    return cycle[0:-1]

def merge_polygons_V0(poly1: CoordList, poly2: CoordList) -> CoordList:
    intersect = find_intersections(poly1, poly2)
    graph = build_graph(poly1, poly2, intersect)
    cycles: list[CoordList] = find_cycles(graph)
    if len(cycles) == 1:
        return cycles[0]
    max_area = 0.0
    best_cycle = None
    for cycle in cycles:
        area  = area_of_bounding_box(cycle)
        if area > max_area:
            best_cycle = cycle
            max_area = area

    return best_cycle

def area_of_bounding_box(cycle1: CoordList) -> float:
    pt1 = cycle1[0]
    pt1_x, pt1_y = pt1
    min_x: Fraction = pt1_x
    min_y: Fraction = pt1_y
    max_x: Fraction = pt1_x
    max_y: Fraction = pt1_y
    for pt2 in cycle1:
        pt2_x, pt2_y = pt2
        min_x = min(min_x, pt2_x)
        min_y = min(min_y, pt2_y)
        max_x = max(max_x, pt2_x)
        max_y = max(max_y, pt2_y)
    area = float(Fraction(max_x - min_x) * Fraction(max_y - min_y))
    return area

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


def find_intersections(poly1: CoordList, poly2: CoordList) -> tuple[list[list[Point]],list[list[Point]]]:
    ## We have a convention that both polygons should be traversed in a counter-clockwise
    ## rotation.
    if is_clockwise(poly1):
        poly1.reverse()
    if is_clockwise(poly2):
        poly2.reverse()


    cross_pts1 = [[] for _ in range(len(poly1))]
    cross_pts2 = [[] for _ in range(len(poly2))]
    assert poly1[0] == poly1[-1]
    assert poly2[0] == poly2[-1]
    pt1_prev = None
    for i,pt1 in enumerate(poly1):

        if pt1_prev:
            a = (pt1_prev, pt1)
            pt2_prev = None
            for j,pt2 in enumerate(poly2):
                if pt2_prev:
                    b = (pt2_prev, pt2)
                    if segments_might_cross(a, b):
                        cross_point = segment_intersection(a, b)
                        if cross_point:
                            cross_pts1[i].append(cross_point)
                            cross_pts2[j].append(cross_point)
                pt2_prev = pt2

        pt1_prev = pt1
    return cross_pts1, cross_pts2

def print_intersections(poly1: CoordList, poly2: CoordList, cross_pts: tuple[list[list[Point]],list[list[Point]]]) -> None:
    cross1, cross2 = cross_pts
    print('\npoly1')
    for i, pt1 in enumerate(poly1):
        print(f'{i=}, {pf(pt1)}')
        if cross1[i]:
            print('        crossings: ', " ".join([str(pf(pt2)) for pt2 in cross1[i]]))
    print('\npoly2')
    for i,pt1 in enumerate(poly2):
        print(f'{i=}, {pf(pt1)}')
        if cross2[i]:
            print('        crossings: ', " ".join([str(pf(pt2)) for pt2 in cross2[i]]))


def build_graph(poly1: CoordList,
                poly2: CoordList,
                cross_pts: tuple[list[list[Point]],list[list[Point]]],
                ) -> dict[Point,list[Point]]:
    graph: dict[Point,list[Point]] = {}
    cross1, cross2 = cross_pts
    expand_graph(poly1, cross1, graph)
    expand_graph(poly2, cross2, graph)
    return graph


def add_crossings(prev_pt: Point,
                  pt1: Point,
                  crossings:
                  list[Point],
                  graph: dict[Point,list[Point]]) -> None:
    crossings.append(pt1)
    if pt1 > prev_pt:
        # linear points ascending order
        crossings.sort()
    else:
        # linear points descending order
        crossings.sort(reverse=True)
    node = graph.get(prev_pt, [])
    for pt2 in crossings:
        node.append(pt2)
        graph[prev_pt] = node
        node = graph.get(pt2, [])
        prev_pt = pt2


def expand_graph(poly1: CoordList, cross_pts: list[list[Point]], graph: dict[Point,list[Point]]) -> None:
    prev_pt = None
    for i, pt1 in enumerate(poly1):
        node = graph.get(prev_pt, [])
        if cross_pts[i]:
            add_crossings(prev_pt, pt1, cross_pts[i], graph)
        else:
            node.append(pt1)
            graph[prev_pt] = node
        prev_pt = pt1

def find_cycles(graph: dict[Point,list[Point]],) -> list[CoordList]:
    """Find cyles in the directed graph by always preferring to turn right.
    These cycles should correspond either to the common outer perimeter of combined polygons or else
    to the boundary of internal holes."""
    ## Keep a set of all the nodes in the graph that have not been explored.
    keys = list(graph.keys())
    keys = [key for key in keys if key ]
    unexplored: set[Point] = set(keys)
    cycles: list[CoordList] = []
    prev_pt, pt1 = find_starting_segment(graph, unexplored)
    ## print(f'find_starting_segment: prev_pt: {prev_pt} pt1: {pt1}')
    while prev_pt and pt1:
        ## We have an unexplored segment where prev_pt has only pt1 as the single successor
        unexplored.remove(pt1)
        unexplored.remove(prev_pt)
        current_cycle: CoordList = [prev_pt, pt1]
        found_in_cycle: set[Point] = set(current_cycle)
        while True:
            next_pt = prefer_right_turns(graph, prev_pt, pt1)
            if next_pt in unexplored:
                unexplored.remove(next_pt)
            current_cycle.append(next_pt)
            ## print(f'current_cycle: {current_cycle}')
            if next_pt and next_pt in found_in_cycle:
                ## We have completed a cycle with next_pt.
                index1 = current_cycle.index(next_pt)
                if index1 > 0:
                    current_cycle = current_cycle[index1:]
                cycles.append(current_cycle)
                break
            found_in_cycle.add(next_pt)
            prev_pt, pt1 = pt1, next_pt
        prev_pt, pt1 = find_starting_segment(graph, unexplored)

    return cycles

def prefer_right_turns(graph: dict[Point,list[Point]], prev_pt: Point, pt1: Point) -> Point:
    """When there is a choice of successor points, prefer rightmost turn.
    Because counterclockwise is defined as positive, the rightmost turn will be the smallest angle."""
    node = graph.get(pt1, [])
    if len(node) == 1:
        return node[0]
    min_angle = 360
    best_pt = None
    for pt2 in graph[pt1]:
        angle = signed_angle_ab_to_bc(prev_pt, pt1, pt2)
        if angle < min_angle:
            min_angle = angle
            best_pt = pt2
    return best_pt

def find_starting_segment(graph: dict[Point,list[Point]], unexplored: set[Point]) -> tuple[Point , Point]:
    for prev_pt in unexplored:
        node = graph.get(prev_pt, [])
        if len(node) == 1:
            pt1 = node[0]
            if pt1 in unexplored:
                return prev_pt, node[0]
    return None, None


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
