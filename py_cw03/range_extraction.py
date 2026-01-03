def solution(args):
    start = None
    current = None
    output = ''

    def add_to_range(n: int) -> None:
        nonlocal start
        nonlocal current
        nonlocal output
        if start is None:
            start = n
            current = n
            return

        if n > current + 1:
            do_output(n)
        current = n

    def do_output(n: int, final=False) -> None:
        nonlocal start
        nonlocal current
        nonlocal output
        if start is None:
            start = n
            current = n
        comma_before = "," if len(output) > 0 else ""
        if final:
            if current == start and current == n: ## Single number at the end
                msg = f'{comma_before}{start}'
            elif current > start + 1: ## Range already in progress
                if n > current + 1: ## Range plus final number
                    msg = f'{comma_before}{start}-{current},{n}'
                else: # n added to range
                    msg = f'{comma_before}{start}-{n}'
            else:
                if n == start + 2 and current == start + 1: # n completes a range of 3 numbers
                    msg = f'{comma_before}{start}-{n}'
                elif current == start: ## only have 2 numbers
                    msg = f'{comma_before}{start},{n}'
                else: ## have 3 numbers
                    msg = f'{comma_before}{start},{current},{n}'
        else:
            if current > start + 1:
                msg = f'{comma_before}{start}-{current}'
            elif current == start: ## current same as start os output 1 number
                msg = f"{comma_before}{start}"
            else:  ## current is only one more than start so output 2 numbers
                msg = f"{comma_before}{start},{current}"
        output = output + msg
        start = n
        current = n

    for ix, n in enumerate(args):
        ## print(f'Before: {ix=} {n=} {start=} {current=} {output=}')
        if ix + 1 == len(args):
            do_output(n, final=True)
        else:
            add_to_range(n)
        ## print(f'After: {ix=} {n=} {start=} {current=} {output=}')
    return output
