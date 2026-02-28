import math

MAX_LEN_RECURSE = 8
PARTITION_N = 8

def closest_pair(points):
    print(f'{len(points)=}')

    p1, p2, _ = partition_n_by_n(list(points))

    return [p1, p2]

def xy_range(points):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')
    for point in points:
        min_x = min(min_x, point[0])
        min_y = min(min_y, point[1])
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])
    return min_x, min_y, max_x, max_y

def distance_squared(p1, p2):
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return (p2_x - p1_x) * (p2_x - p1_x)  + (p2_y - p1_y) * (p2_y - p1_y)

def closest_pair_recur(points: list[tuple[int, int]]):
    if len(points) == 2 or len(points) > MAX_LEN_RECURSE:
        return points[0], points[1], distance_squared(points[0], points[1])
    points = points.copy()
    ## Otherwise compute the distance from points[-1] to each other point
    last = points.pop()
    min_dsq = float('inf')
    best_pair = []
    for p in points:
        dsq = distance_squared(last, p)
        if dsq < min_dsq:
            best_pair = [last, p]
            min_dsq = dsq
        p1, p2, dsq = closest_pair_recur(points)
        if dsq < min_dsq:
            best_pair = [p1, p2]
            min_dsq = dsq
    return [best_pair[0], best_pair[1], min_dsq]

def partition_n_by_n(points: list[tuple[int, int]]):
    if len(points) <= MAX_LEN_RECURSE:
        return closest_pair_recur(points)
    min_x, min_y, max_x, max_y = xy_range(points)
    ## Need to set up an N by N grid.
    N = PARTITION_N
    grid = []
    for i in range(N):
        row = []
        grid.append(row)
        for j in range(N):
            row.append([])
    for p in points:
        i, j = partition_index(p, min_x, min_y, max_x, max_y)
        grid[i][j].append(p)
    best_pair = []
    min_dsq = float('inf')
    for i in range(N):
        for j in range(N):
            g = grid[i][j]
            if len(g) == 2:
                dsq = distance_squared(g[0], g[1])
                if dsq < min_dsq:
                    best_pair = [g[0], g[1]]
                    min_dsq = dsq
            elif len(g) >= 3:
                p1, p2, dsq = partition_n_by_n(g)
                if dsq < min_dsq:
                    best_pair = [p1, p2]
                    min_dsq = dsq
    return best_pair[0], best_pair[1], min_dsq



def partition_index(p, min_x, min_y, max_x, max_y):
    i = math.floor((p[0]-min_x)/(max_x-min_x) * PARTITION_N)
    j = math.floor((p[1]-min_y)/(max_y-min_y) * PARTITION_N)
    return i, j