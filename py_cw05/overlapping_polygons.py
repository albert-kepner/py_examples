from fractions import Fraction

Point = tuple[Fraction, Fraction]
CoordList = list[Point]

def merge_polygons(poly1: CoordList, poly2: CoordList) -> CoordList:
    return []

## Given two line segments, each represented by a tuple of two points,
## determine whether the line segments cross and return True iff they cross.
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

def segment_intersection(p1: Point, p2: Point, p3: Point, p4: Point) -> Point | None:
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
    if rx == 0 and ry == 0:
        return p1 if point_on_segment(p1, p3, p4) else None
    if sx == 0 and sy == 0:
        return p3 if point_on_segment(p3, p1, p2) else None

    # q - p
    qpx, qpy = x3 - x1, y3 - y1

    rxs = cross(rx, ry, sx, sy)
    qpxr = cross(qpx, qpy, rx, ry)

    # Parallel lines?
    if rxs == 0:
        # Collinear?
        if qpxr == 0:
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
