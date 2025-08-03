from typing import Tuple
import sys

class SparceCells:

    def __init__(self, cells=None):
        self.cell_set = set()
        if cells:
            self._init_from_lists(cells)

    cell_set: set[Tuple[int, int]]
    n_rows: int | None = None
    n_cols: int | None = None

    def _init_from_lists(self, cells: list[list[int]]) -> None:
        n_rows = len(cells)
        n_cols = len(cells[0])
        self.n_rows = n_rows
        self.n_cols = n_cols
        for i in range(n_rows):
            for j in range(n_cols):
                if cells[i][j] == 1:
                    self.add((i, j))

    def add(self, cell: Tuple[int, int]):
        self.cell_set.add(cell)

    def remove(self, cell: Tuple[int, int]):
        self.cell_set.fremove(cell)

    def contains(self, cell: Tuple[int, int]):
        return cell in self.cell_set



NEIGHBOR_TUPS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def addtups(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def form_group(start_cell: Tuple[int,int], unused:SparceCells) -> list[Tuple[int,int]]:
    group: list[Tuple[int,int]] = [start_cell]
    queue: list[Tuple[int,int]] = [start_cell]
    while queue:
        cell = queue.pop()
        ## make sure the cell is remove from unused, if not already done
        unused.cell_set.discard(cell)

        for tup in NEIGHBOR_TUPS:
            loc = addtups(tup, cell)
            ## found a neighbor of the current cell
            if unused.contains(loc):
                unused.cell_set.discard(cell)
                queue.append(loc)
                group.append(loc)

    return group


def valid_group(group: list[Tuple[int,int]]) -> bool:
    sorted_group = sorted(group, key=lambda x: (x[1], x[0]))
    min_row = min_col = sys.maxsize
    max_row = max_col = - sys.maxsize
    for cell in sorted_group:
        min_row = min(min_row, cell[0])
        min_col = min(min_col, cell[1])
        max_row = max(max_row, cell[0])
        max_col = max(max_col, cell[1])
    n_rows = max_row - min_row + 1
    n_cols = max_col - min_col + 1
    if n_rows > 1 and n_cols > 1:
        return False
    target_size = max(n_rows, n_cols)
    if len(group) != target_size:
        return False
    if n_rows == 1 and n_cols == 1 and len(group) == 1:
        return True
    if n_rows == 1:
        for ix, cell in enumerate(sorted_group):
            # Check that columns are correct ascending sequence
            if cell[1] != min_col + ix:
                return False
    else:
        for ix, cell in enumerate(sorted_group):
            # Check that columns are correct ascending sequence
            if cell[0] != min_row + ix:
                return False
    return True




def validate_groups(groups: list[list[Tuple[int,int]]]) -> bool:
    for group in groups:
        if not valid_group(group):
            return False
    return True


def size_up_groups(groups):
    sizes = [len(group) for group in groups]
    sizes.sort()
    return sizes


def validate_battlefield(field: list[list[int]]) -> bool:
    unused: SparceCells = SparceCells(field)
    groups: list[list[Tuple[int,int]]] = []
    while unused.cell_set:
        next_cell = unused.cell_set.pop()
        group = form_group(next_cell, unused)
        groups.append(group)

    ok = validate_groups(groups)
    if not ok:
        return False

    sizes = size_up_groups(groups)

    ok = sizes == [1,1,1,1,2,2,2,3,3,4]

    return ok