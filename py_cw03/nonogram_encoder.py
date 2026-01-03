def encode(nonogram):
    rows = len(nonogram)
    cols = len(nonogram[0])
    row_hints = []
    for irow in range(rows):
        row_gen = row_items(nonogram, irow)
        row_hints.append(count_ones(row_gen))
    row_hints = tuple(row_hints)
    col_hints = []
    for icol in range(cols):
        col_gen = column_items(nonogram, icol)
        col_hints.append(count_ones(col_gen))
    col_hints = tuple(col_hints)
    return (col_hints , row_hints)


def row_items(nonogram, irow):
    for item in nonogram[irow]:
        yield item

def column_items(nonogram, icol):
    for row in nonogram:
        yield row[icol]

def count_ones(item_gen):
    result = []
    one_count = 0
    for item in item_gen:
        if item == 1:
            one_count += 1
        elif item == 0:
            if one_count > 0:
                result.append(one_count)
                one_count = 0
    if one_count > 0:
        result.append(one_count)
    return tuple(result)
