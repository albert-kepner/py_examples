def guess_number(right: list[str], wrong: list[str]) -> int | None:
    solution: int | None = None
    for i in range(2000):
        if check_right_facts(i, facts=right) and check_wrong_facts(i, facts=wrong):
            if solution is None:
                solution = i
            else:
                solution = None
                return solution
    return solution


def check_right_facts(guess: int, facts: list[str]) -> bool:
    ok: bool = True
    for fact in facts:
        ok = ok and check_right_all_true(guess, fact)
    return ok


def check_wrong_facts(guess: int, facts: list[str]) -> bool:
    ok: bool = True
    for fact in facts:
        current = check_wrong_all_false(guess, fact)
        ## print(f'wrong {fact} returns {current}')
        ok = ok and check_wrong_all_false(guess, fact)
    return ok


def check_right_all_true(guess: int, fact: str) -> bool:
    last_space_index = fact.rfind(" ")
    last_token = fact[last_space_index + 1:]
    num = None
    if last_token.isnumeric():
        num = int(last_token)
    if "odd" in fact:
        return guess % 2 == 1
    elif "even" in fact:
        return guess % 2 == 0
    elif "divisible" in fact:
        return guess % num == 0
    elif "more" in fact:
        return guess > num
    elif "less" in fact:
        return guess < num
    elif "starting" in fact:
        return str(guess).startswith(str(num))
    elif "ending" in fact:
        return str(guess).endswith(str(num))
    else:
        raise Exception(f"Unknown right fact: {fact}")


def check_wrong_all_false(guess: int, fact: str) -> bool:
    last_space_index = fact.rfind(" ")
    last_token = fact[last_space_index + 1:]
    num = None
    if last_token.isnumeric():
        num = int(last_token)
    if "odd" in fact:
        return not guess % 2 == 1
    elif "even" in fact:
        return not guess % 2 == 0
    elif "divisible" in fact:
        return not guess % num == 0
    elif "more" in fact:
        return guess < num
    elif "less" in fact:
        return guess > num
    elif "starting" in fact:
        return not str(guess).startswith(str(num))
    elif "ending" in fact:
        # print(f'ending {fact} num = {num} {last_token=} {not last_token.endswith(str(num))=}')
        return not str(guess).endswith(str(num))
    else:
        raise Exception(f"Unknown right fact: {fact}")
