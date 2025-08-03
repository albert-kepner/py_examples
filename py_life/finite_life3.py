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

    def as_lists1(self, cells: list[list[int]]):
        n_rows = len(cells)
        n_cols = len(cells[0])
        cells = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        for cell in self.cell_set:
            cells[cell[0]][cell[1]] = 1
        return cells

    def as_lists2(self):
        min_row = min_col = sys.maxsize
        max_row = max_col = - sys.maxsize
        for cell in self.cell_set:
            min_row = min(min_row, cell[0])
            min_col = min(min_col, cell[1])
            max_row = max(max_row, cell[0])
            max_col = max(max_col, cell[1])
        n_rows = max_row - min_row + 1
        n_cols = max_col - min_col + 1
        cells = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        base = (- min_row, - min_col)
        for cell in self.cell_set:
            loc = addtups(cell, base)
            cells[loc[0]][loc[1]] = 1
        return cells

    def add(self, cell: Tuple[int, int]):
        self.cell_set.add(cell)

    def contains(self, cell: Tuple[int, int]):
        return cell in self.cell_set


NEIGHBOR_TUPS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    sparce_result = None
    if generations <= 0:
        return cells
    sparce_cells: SparceCells = SparceCells(cells)
    for i in range(generations):
        sparce_result = next_gen2(sparce_cells)
        sparce_cells = sparce_result
    return sparce_result.as_lists2()


def next_gen(cells: list[list[int]]) -> list[list[int]]:
    sparce_cells: SparceCells = SparceCells(cells)
    sparce_result = next_gen2(sparce_cells)
    return sparce_result.as_lists2()


def next_gen2(sparce_cells: SparceCells) -> SparceCells:
    empty_neighbors: SparceCells = SparceCells()
    next_gen_cells: SparceCells = SparceCells()
    for cell in sparce_cells.cell_set:
        neighbor_count = 0
        for neighbor in NEIGHBOR_TUPS:
            other = addtups(cell, neighbor)
            if other in sparce_cells.cell_set:
                neighbor_count += 1
            else:
                empty_neighbors.add(other)
        if neighbor_count in [2, 3]:
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


def addtups(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

