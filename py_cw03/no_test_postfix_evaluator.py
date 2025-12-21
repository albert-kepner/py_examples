def test_evaluate_postfix_expression():
    from postfix_evaluator import postfix_evaluator

    # Test cases
    assert postfix_evaluator("2 3 +") == 5
    assert postfix_evaluator("7 4 -") == 3
    assert postfix_evaluator("6 2 *") == 12
    assert postfix_evaluator("8 4 /") == 2
    assert postfix_evaluator("5 1 2 + 4 * + 3 -") == 14
    assert postfix_evaluator("10 2 8 * + 3 -") == 23
    assert postfix_evaluator("3 4 + 2 * 7 /") == 2.0
    assert postfix_evaluator("4 5 6 * + 7 -") == 27

    print("All tests passed!")