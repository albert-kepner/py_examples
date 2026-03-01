def count_components(components: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
    dict1: dict[int, int] = {}
    for component in components:
        count1 = len(component)
        dict1[count1] = dict1.get(count1, 0) + 1
    counts: list[tuple[int,int]] = []
    for size1, count2 in dict1.items():
        counts.append((size1, count2))
    counts.sort(reverse=True)
    return counts


def components(input1: str) -> list[tuple[int, int]]:
    lines = parse_lines(input1)
    ## print(f'{len(lines)=}')
    rows = int((len(lines) - 1) / 2)
    cols = int((len(lines[0]) - 1) / 3)
    print(f'{rows=}, {cols=}')
    grid = populate_grid(rows, cols, lines)
    print(f'{grid=}')
    components = find_components(rows, cols, grid)
    print(f'{components=}')
    counts: list[tuple[int,int]] = count_components(components)
    return counts


def find_components(rows: int, cols: int, grid: list[list[list[tuple[int, int]]]]) -> list[list[tuple[int, int]]]:
    components = []
    explored: set[tuple[int, int]] = set()
    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            if node in explored:
                continue
            component = create_component(node, grid, explored)
            components.append(component)
    return components


def create_component(node: tuple[int, int],
                     grid: list[list[list[tuple[int, int]]]],
                     explored: set[tuple[int, int]]) -> list[tuple[int, int]]:
    component = []
    queue: list[tuple[int, int]] = [node]
    while queue:
        node = queue.pop()
        if not node in explored:
            explored.add(node)
            component.append(node)
        neighbors = grid[node[0]][node[1]]
        for neighbor in neighbors:
            if neighbor not in explored:
                queue.append(neighbor)
    return component


def parse_lines(lines: str) -> list[str]:
    # print(f'{lines=}')
    lines = lines.split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    # for idx, line in enumerate(lines):
    #     print(f'{idx=} {line=} {len(line)=}')
    assert len(lines) % 2 == 1
    for line in lines:
        assert line != ""
        assert len(line) == len(lines[0])
    return lines


def create_grid(rows: int, cols: int) -> list[list[list[tuple[int, int]]]]:
    grid = []
    for i in range(rows):
        row = [[] for _ in range(cols)]
        grid.append(row)
    return grid


def populate_grid(rows: int, cols: int, lines: list[str]) -> list[list[list[tuple[int, int]]]]:
    grid = create_grid(rows, cols)
    for i in range(rows):
        for j in range(cols - 1):
            pair = connect_right(i, j, lines)
            # print(f'connect_right = {i=} {j=} {pair=}')
            connect(grid, pair)

    for i in range(rows - 1):
        for j in range(cols):
            pair = connect_down(i, j, lines)
            # print(f'connect_down = {i=} {j=} {pair=}')
            connect(grid, pair)
    return grid


def connect(grid: list[list[list[tuple[int, int]]]], pair: list[tuple[int, int]]) -> None:
    if pair:
        i, j = pair[0]
        grid[i][j].append(pair[1])
        i, j = pair[1]
        grid[i][j].append(pair[0])


def connect_right(i: int, j: int, lines: list[str]) -> list[tuple[int, int]]:
    line_row = i * 2 + 1
    line_col = j * 3 + 3
    if lines[line_row][line_col] == ' ':
        result = [(i, j), (i, j + 1)]
    else:
        result = []
    return result


def connect_down(i: int, j: int, lines: list[str]) -> list[tuple[int, int]]:
    line_row = i * 2 + 2
    line_col = j * 3 + 1
    if lines[line_row][line_col] == ' ':
        result = [(i, j), (i + 1, j)]
    else:
        result = []
    return result
