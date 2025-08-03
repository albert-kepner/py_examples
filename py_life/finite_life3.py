from typing import Tuple


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

    def as_lists1(self, cells: list[list[int]]):
        n_rows = len(cells)
        n_cols = len(cells[0])
        cells = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        for cell in self.cell_set:
            cells[cell[0]][cell[1]] = 1
        return cells

    def add(self, cell: Tuple[int, int]):
        self.cell_set.add(cell)

    def contains(self, cell: Tuple[int, int]):
        return cell in self.cell_set

NEIGHBOR_TUPS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def next_gen(cells: list[list[int]]) -> list[list[int]]:
    sparce_cells: SparceCells = SparceCells(cells)
    sparce_result = next_gen2(cells, sparce_cells)
    return sparce_result.as_lists1(cells)

def next_gen2(cells: list[list[int]], sparce_cells: SparceCells) -> SparceCells:
    empty_neighbors: SparceCells = SparceCells()
    next_gen_cells: SparceCells = SparceCells()
    n_rows = len(cells)
    n_cols = len(cells[0])
    for cell in sparce_cells.cell_set:
        neighbor_count = 0
        for neighbor in NEIGHBOR_TUPS:
            other = addtups(cell, neighbor)
            if other in sparce_cells.cell_set:
                neighbor_count += 1
            else:
                if in_range(other, n_rows, n_cols):
                    empty_neighbors.add(other)
        if neighbor_count in [2,3]:
            next_gen_cells.add(cell)
    for cell in empty_neighbors.cell_set:
        neighbor_count = 0
        for neighbor in NEIGHBOR_TUPS:
            other = addtups(cell, neighbor)
            if other in sparce_cells.cell_set:
                neighbor_count += 1
        if neighbor_count == 3:
            next_gen_cells.add(cell)
    return next_gen_cells

def addtups(a: Tuple[int,int], b: Tuple[int,int]) -> Tuple[int,int]:
    return a[0]+b[0], a[1]+b[1]

def in_range(a:Tuple[int,int], n_rows: int, n_cols: int) -> bool:
    return a[0] >= 0 and a[0] < n_rows and a[1] >= 0 and a[1] < n_cols


