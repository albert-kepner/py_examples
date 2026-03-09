from overlapping_polygons import *


def test_01():
    p1 = (f(0, 1), f(0, 1))
    p2 = (f(10, 1), f(10, 1))
    p3 = (f(0, 1), f(10, 1))
    p4 = (f(10, 1), f(0, 1))
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
    for p3 in [pt(0, 2), pt(0, 10), pt(5, 10), pt(10, 10), pt(20, 10), pt(20, 1), pt(20, 0), pt(20, -10)]:
        # print(f'{type(p1)=} {type(p2)=} {type(p3)=}')
        # print(f'{p1}, {p2}, {p3}')
        angle = signed_angle_ab_to_bc(p1, p2, p3)
        print(f'angle: {angle}')


def test_05():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    print('')
    for p3 in [pt(0, 2), pt(0, 10), pt(5, 10), pt(10, 10), pt(20, 10), pt(20, 1), pt(20, 0)]:
        # print(f'{type(p1)=} {type(p2)=} {type(p3)=}')
        # print(f'{p1}, {p2}, {p3}')
        angle = signed_angle_ab_to_ac(p2, p1, p3)
        print(f'angle: {angle}')


def test_06():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    print('')
    for p3 in [pt(0, 2), pt(0, 10), pt(5, 10), pt(10, 10), pt(20, 10), pt(20, 1), pt(20, 0), pt(20, -10)]:
        p3 = (p3[0], -p3[1])
        angle = signed_angle_ab_to_bc(p1, p2, p3)
        print(f'angle: {angle}')


def test_07():
    p1 = pt(0, 0)
    p2 = pt(10, 0)
    p3 = pt(5, 10)
    p4 = pt(0, 0)
    poly1: CoordList = [p1, p2, p3, p4]
    cw = is_clockwise(poly1)
    print(f'cw: {cw}')
    poly1.reverse()
    cw = is_clockwise(poly1)
    print(f'cw: {cw}')


def test_08():
    poly1 = [pt(0, 5), pt(10, 0), pt(10, 10), pt(0, 5)]
    poly2 = [pt(5, 0), pt(5, 10), pt(15, 5), pt(5, 0)]
    intersect = find_intersections(poly1, poly2)
    print_intersections(poly1, poly2, intersect)


def test_09():
    poly1 = [pt(0, 5), pt(10, 0), pt(10, 10), pt(0, 5)]
    poly2 = [pt(5, 0), pt(5, 10), pt(15, 5), pt(5, 0)]
    intersect = find_intersections(poly1, poly2)
    graph = build_graph(poly1, poly2, intersect)
    keys = list(graph.keys())
    keys = [key for key in keys if key]
    print(f'keys: {keys}')
    keys.sort()
    for key in keys:
        print(f'key: {pf(key)}')
        successors = graph[key]
        if successors:
            succ = ', '.join([str(pf(succ)) for succ in successors])
            print(f'        successors: {succ}')


def test_10():
    poly1 = [pt(0, 5), pt(10, 0), pt(10, 10), pt(0, 5)]
    poly2 = [pt(5, 0), pt(5, 10), pt(15, 5), pt(5, 0)]
    intersect = find_intersections(poly1, poly2)
    graph = build_graph(poly1, poly2, intersect)
    cycles = find_cycles(graph)
    print(f'{len(cycles)} cycles')
    for cycle in cycles:
        msg = ", ".join([str(pf(pt)) for pt in cycle])
        print(f'cycle: {msg}')


def test_11():
    poly1 = [pt(0, 5), pt(10, 0), pt(10, 10), pt(0, 5)]
    poly2 = [pt(5, 0), pt(5, 10), pt(15, 5), pt(5, 0)]
    cycle = merge_polygons_V0(poly1, poly2)
    msg = ", ".join([str(pf(pt)) for pt in cycle])
    print(f'cycle: {msg}')

example_test_cases = {
    'Simple Case': (
        [(0, 0), (0, 20), (20, 20), (20, 0)],
        [(5, 5), (15, 30), (30, 15)],
        [(0, 0), (0, 20), (11, 20), (15, 30), (30, 15), (20, 11), (20, 0)]
    ),
    'Simple Case - Reversed': (
        [(20, 0), (20, 20), (0, 20), (0, 0)],
        [(5, 5), (15, 30), (30, 15)],
        [(0, 0), (0, 20), (11, 20), (15, 30), (30, 15), (20, 11), (20, 0)]
    ),
    'Overlap Without Contained Points': (
        [(0, 0), (0, 4), (3, 4), (3, 0)],
        [(-1, 1), (-1, 3), (4, 3), (4, 1)],
        [(-1, 1), (-1, 3), (0, 3), (0, 4), (3, 4), (3, 3), (4, 3), (4, 1), (3, 1), (3, 0), (0, 0), (0, 1)]
    ),
    'Fully Contained': (
        [(0, 0), (0, 10), (10, 10), (10, 0)],
        [(2, 2), (5, 7), (8, 2)],
        [(0, 0), (0, 10), (10, 10), (10, 0)]
    ),
    'Holes': (
        [(0, 0), (0, 5), (2, 5), (2, 2), (5, 2), (5, 0)],
        [(1, 4), (4, 4), (4, 1)],
        [(0, 0), (0, 5), (2, 5), (2, 4), (4, 4), (4, 2), (5, 2), (5, 0)]
    ),
    'Different Start/Direction': (
        [(120, -50), (0, -50), (0, 50), (120, 50)],
        [(-80, 59), (31, 95), (100, 0), (31, -95), (-80, -59)],
        [(31, 95), (Fraction(1210, 19), 50), (120, 50), (120, -50), (Fraction(1210, 19), -50), (31, -95), (-80, -59), (-80, 59)]
    ),
    'Aligned Points': (
        [(2, 2), (0, 4), (2, 6), (4, 4)],
        [(0, 1), (2, 4), (4, 1)],
        [(0, 1), (Fraction(6, 5), Fraction(14, 5)), (0, 4), (2, 6), (4, 4), (Fraction(14, 5), Fraction(14, 5)), (4, 1)]
    ),
    'Window': (
        [(0, 6), (5, 11), (7, 11), (2, 6), (7, 1), (5, 1)],
        [(6, 12), (6, 0), (8, 0), (8, 12)],
        [(0, 6), (5, 11), (6, 11), (6, 12), (8, 12), (8, 0), (6, 0), (6, 1), (5, 1)]
    ),
    'Jagged': (
        [(1, 1), (1, 2), (2, 5), (3, 2), (4, 5), (5, 2), (6, 5), (7, 2), (8, 5), (9, 2), (9, 1)],
        [(2, Fraction(3, 2)), (2, 4), (8, 4), (8, Fraction(3, 2))],
        [(1, 1), (1, 2), (2, 5), (Fraction(7, 3), 4), (Fraction(11, 3), 4), (4, 5), (Fraction(13, 3), 4), (Fraction(17, 3), 4), (6, 5), (Fraction(19, 3), 4), (Fraction(23, 3), 4), (8, 5), (9, 2), (9, 1)]
    )
}

def make_case(name: str) -> tuple[Any, Any, Any]:
    return example_test_cases[name]


def test_12():
    poly1, poly2, answer = make_case('Simple Case')
    cycle = merge_polygons(poly1, poly2)
    print(answer)
    print(cycle)

## 'Fully Contained'
def test_13():
    poly1, poly2, answer = make_case('Fully Contained')
    poly1.append(poly1[0])
    poly2.append(poly2[0])
    intersect = find_intersections(poly1, poly2)
    print_intersections(poly1, poly2, cross_pts=intersect)
    graph = build_graph(poly1, poly2, intersect)
    cycles: list[CoordList] = find_cycles(graph)

    print(answer)
    print(cycles, flush=True)

    max_area = 0.0
    best_cycle = None
    for cycle in cycles:
        area = area_of_bounding_box(cycle)
        if area > max_area:
            best_cycle = cycle
            max_area = area
    print(best_cycle)
    print(max_area)

def test_14():
    poly1, poly2, answer = make_case('Fully Contained')
    cycle = merge_polygons(poly1, poly2)
    print(answer)
    print(cycle)
