def solution(args):
    start = None
    current = None
    previous = None
    in_range: bool = False
    recent_range: bool = False
    range_end = None
    out = []
    ## print('input:', args)
    for ix, n in enumerate(args):
        lookahead = args[ix+1] if ix+1 < len(args) else None
        if in_range:
            ## print(f'*** in_range: {current=} {n=} {lookahead=} {recent_range=}')
            if lookahead is None or lookahead > n + 1 : ## conditions to end current range
                out.append( (start, n))
                in_range = False
                range_end = n
            else:
                pass
        else:
            ## print(f'not in_range: {current=} {n=} {lookahead=} {recent_range=}')
            if current and lookahead and n == current + 1 and lookahead == n + 1 and not in_range: ## conditions to start a new range
                start = current
                in_range = True
            else: # if current is not part of a range
                if current and not current == range_end:
                    out.append(current)
        previous = current
        current = n
        recent_range = in_range  ## remember most recent range condition in case it changes
    ## All elements have been scanned, process remaining elements
    ## print('all elements scanned: output:', out)
    if in_range:
        out.append( (start, current) )
    else:  # if current is not part of a range
        if current and not current == range_end:
            out.append(current)
    ## print(f'out: {out}')
    return ','.join(map(range_or_str, out))

def range_or_str(item):
    if isinstance(item, int):
        return str(item)
    elif isinstance(item, tuple):
        return f'{item[0]}-{item[1]}'
    else:
        raise Exception(f'{item} is not known')


