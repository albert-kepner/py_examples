SOLUTION: tuple[int, int, int] | None = None
PUZZLE: list[list[int]] = [[]]


def init_col() -> set[int]:
    col: set[int] = set()
    for j in range(1, 10, 1):
        col.add(j)
    return col


def init_row() -> list[set[int]]:
    cols = []
    for i in range(9):
        col = init_col()
        cols.append(col)
    return cols


def init_sets() -> list[list[set[int]]]:
    rows = []
    for i in range(9):
        row = init_row()
        rows.append(row)
    return rows


def remove_marked(set1, marked) -> bool:
    if marked in set1:
        set1.remove(marked)
        return True
    else:
        return False


def solution_at(set1: set[int], row: int, col: int) -> None:
    global SOLUTION
    if not PUZZLE[row][col]:  ## Original puzzle cells cannot be a valid solution
        SOLUTION = (row, col, list(set1)[0])
        # print(f'{SOLUTION=}')
    # sys.exit(1)


def remove_for_row(row, col, marked, possible_sets) -> None:
    for icol in range(9):
        if icol != col:
            set1: set[int] = possible_sets[row][icol]
            if remove_marked(set1, marked) and len(set1) == 1:
                solution_at(set1, row, icol)


def remove_for_col(row, col, marked, possible_sets) -> None:
    for irow in range(9):
        if irow != row:
            set1: set[int] = possible_sets[irow][col]
            if remove_marked(set1, marked) and len(set1) == 1:
                solution_at(set1, irow, col)


def get_cell_base(row, col) -> tuple[int, int]:
    return (row // 3) * 3, (col // 3) * 3


def remove_for_cell(row, col, marked, possible_sets) -> None:
    cell_pos: tuple[int, int] = get_cell_base(row, col)
    for irow in range(cell_pos[0], cell_pos[0] + 3):
        for jcol in range(cell_pos[1], cell_pos[1] + 3):
            if row != irow or col != jcol:
                set1: set[int] = possible_sets[irow][jcol]
                if remove_marked(set1, marked) and len(set1) == 1:
                    solution_at(set1, irow, jcol)


def print_rows(rows, possible_sets):
    for row in rows:
        for col in range(9):
            msg = f'pos = ({row}, {col}) set = {possible_sets[row, col]}'
            print(msg)
        print('')


def progress_v0(puzzle: list[list[int]]) -> tuple[int, int, int]:
    global PUZZLE
    PUZZLE = puzzle
    possible_sets: list[list[set[int]]] = init_sets()
    for row in range(9):
        for col in range(9):
            marked = puzzle[row][col]
            if marked:
                remove_for_row(row, col, marked, possible_sets)
                remove_for_col(row, col, marked, possible_sets)
                remove_for_cell(row, col, marked, possible_sets)
    return SOLUTION


def solution_last_element(row, col, used_set):
    global SOLUTION
    assert (len(used_set) == 8)
    not_used = [i for i in range(1, 10, 1) if i not in used_set]
    assert (len(not_used) == 1)
    SOLUTION = (row, col, not_used[0])


def check_row_last_element(row, puzzle):
    found_col = -1
    found_count = 0
    used_set = set()
    for col in range(9):
        if not puzzle[row][col]:
            found_col = col
            found_count += 1
        else:
            used_set.add(puzzle[row][col])
    if found_count == 1:
        solution_last_element(row, found_col, used_set)


def check_col_last_element(col, puzzle):
    found_row = -1
    found_count = 0
    used_set = set()
    for row in range(9):
        if not puzzle[row][col]:
            found_row = row
            found_count += 1
        else:
            used_set.add(puzzle[row][col])
    if found_count == 1:
        solution_last_element(found_row, col, used_set)

def check_box_last_element(box_pos: tuple[int,int], puzzle):
    found_pos = None
    found_count = 0
    used_set = set()
    for row in range(box_pos[0], box_pos[0]+3):
        for col in range(box_pos[1], box_pos[1]+3):
            if not puzzle[row][col]:
                found_pos = (row, col)
                found_count += 1
            else:
                used_set.add(puzzle[row][col])
    if found_count == 1:
        solution_last_element(found_pos[0], found_pos[1], used_set)


def progress(puzzle: list[list[int]]) -> tuple[int, int, int]:
    global PUZZLE
    PUZZLE = puzzle
    for row in range(9):
        check_row_last_element(row, puzzle)
    for col in range(9):
        check_col_last_element(col, puzzle)
    for row in range(0,9,3):
        for col in range(0,9,3):
            pos = (row, col)
            check_box_last_element(pos, puzzle)
    return SOLUTION