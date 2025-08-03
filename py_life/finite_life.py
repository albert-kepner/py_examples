def next_gen(cells: list[list[int]]) -> list[list[int]]:
    n_rows = len(cells)
    n_cols = len(cells[0])
    new_cells = [[0 for j in range(n_cols)] for i in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            count = count_neighbors(cells, i,j)
            ## print(f'{i=} {j=} {count=}')
            if cells[i][j] == 1:
                life_value_live = count in [2,3]
                new_cells[i][j] = 1 if life_value_live else 0
            else:
                new_cells[i][j] = 1 if count == 3 else 0
    return new_cells

def count_neighbors(cells: list[list[int]], i: int, j: int) -> int:
    n_rows = len(cells)
    n_cols = len(cells[0])
    count = 0
    for ix in range(-1,2,1):
        for jx in range(-1,2,1):
            if ix or jx:
                i_next = i + ix
                j_next = j + jx
                if i_next < 0 or i_next >= n_rows:
                    continue
                if j_next < 0 or j_next >= n_cols:
                    continue
                count += cells[i_next][j_next]
    return count

