def postfix_evaluator(expr: str) -> int:
    tokens = expr.split(' ')
    result = eval_tokens(tokens)
    return result

def eval_tokens(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if is_number(token):
            n = get_number(token);
            stack.append(n)
        elif is_operator(token):
            n1 = stack.pop()
            n2 = stack.pop()
            n3 = apply_operator(token, n1, n2)
            stack.append(n3)
        else:
            raise Exception(f'Unexpected token: {token}')

    assert len(stack) == 1
    return stack.pop()

def is_number(token: str) -> bool:
    try:
        int(token)
        return True
    except ValueError:
        return False

def get_number(token: str) -> int:
    return int(token)

def is_operator(token: str) -> bool:
    return token in ('+', '-', '*', '/')

def apply_operator (op: str, n1: int, n2: int) -> int:
    if op == '+':
        return n2 + n1
    elif op == '-':
        return n2 - n1
    elif op == '*':
        return n2 * n1
    elif op == '/':
        return n2 // n1
    else:
        raise Exception(f'Unexpected operator: {op}')