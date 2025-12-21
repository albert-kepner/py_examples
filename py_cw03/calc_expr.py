VERBOSE = False

def calc(expression):
    ## First break the input expression up into tokens
    ## 1) Replace all spaces with nothing
    ## 2) Replace leading - with negation, and --, +-, /-, *-, (-
    ##    with appropriate combinations of negation and operators.
    ## Use ! as the negation operator.
    ## 3) Scan the input separating the operators as strings
    ## and replacing numeric strings with numbers using parse_number()
    expr1 = string_replacements(expression)
    tokens = []
    num_buffer = ""
    operators = set("+-*/()!")
    for char in expr1:
        if char in operators:
            if num_buffer:
                tokens.append(parse_number(num_buffer))
                num_buffer = ""
            tokens.append(char)
        else:
            num_buffer += char
    if num_buffer:
        tokens.append(parse_number(num_buffer))
    ## 4) Convert the token list into Reverse Polish Notation (RPN)
    ## using the Shunting Yard algorithm.
    output_queue = []
    operator_stack = []
    precedence = {'!': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    right_associative = {'!'}
    for token in tokens:
        if VERBOSE:
            print(f'{token=}')
            print(f'{output_queue=}')
            print(f'{operator_stack=}')
        if isinstance(token, (int, float)):
            if VERBOSE:
                print('adding number to output queue')
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   (precedence[operator_stack[-1]] > precedence[token] or
                    (precedence[operator_stack[-1]] == precedence[token] and token not in right_associative))):
                output_queue.append(operator_stack.pop())
                if VERBOSE:
                    print(f'popped operator {output_queue[-1]} to output queue')
            operator_stack.append(token)
            if VERBOSE:
                print(f'adding operator {token} to operator stack')
        elif token == '(':
            if VERBOSE:
                print(f'adding ( to operator stack')
            operator_stack.append(token)
        elif token == ')':
            assert '(' in operator_stack, "Mismatched parentheses"
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Pop the '('
    while operator_stack:
        output_queue.append(operator_stack.pop())
    ## 5) Evaluate the RPN expression and return the result.
    if VERBOSE:
        print(f'RPN output queue: {output_queue}')
    eval_stack = []
    for token in output_queue:
        if isinstance(token, (int, float)):
            eval_stack.append(token)
        elif token == '!':
            val = eval_stack.pop()
            eval_stack.append(-val)
        else:
            right = eval_stack.pop()
            left = eval_stack.pop()
            if token == '+':
                eval_stack.append(left + right)
            elif token == '-':
                eval_stack.append(left - right)
            elif token == '*':
                eval_stack.append(left * right)
            elif token == '/':
                eval_stack.append(left / right)
    assert len(eval_stack) == 1
    assert isinstance(eval_stack[0], (int, float))
    result = eval_stack[0]
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    if isinstance(result, float):
       result = round(result, 6)
    return result

def string_replacements(expression: str) -> str:
    ## Replace all spaces with nothing
    expression = expression.replace(" ", "")
    ## Replace leading - with negation, and --, +-, /-, *-, (-
    ## with appropriate combinations of negation and operators.
    expression = expression.replace("--", "+")
    expression = expression.replace("+-", "-")
    expression = expression.replace("-+", "-")
    expression = expression.replace("/-", "/!")
    expression = expression.replace("*-", "*!")
    expression = expression.replace("(-", "(!")
    if expression.startswith("-"):
        expression = "!" + expression[1:]
    return expression


def parse_number(s):
    num = float(s)
    return int(num) if num.is_integer() else num
