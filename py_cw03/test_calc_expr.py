import pytest

from calc_expr import calc


def test_calc_basic_operations():
    assert calc("2 + 3") == 5
    assert calc("5 - 2") == 3
    assert calc("4 * 3") == 12
    assert calc("8 / 2") == 4


def test_calc_operator_precedence():
    assert calc("2 + 3 * 4") == 14
    assert calc("10 - 2 / 2") == 9
    assert calc("5 + 6 * 2 - 3") == 14


def test_calc_parentheses():
    assert calc("(2 + 3) * 4") == 20
    assert calc("10 / (5 - 3)") == 5
    assert calc("((1 + 2) * (3 + 4))") == 21


def test_calc_unary_negation():
    assert calc("-5 + 3") == -2
    assert calc("4 * -2") == -8
    assert calc("-(3 + 2) * 2") == -10


def test_calc_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc("5 / 0")
    with pytest.raises(ZeroDivisionError):
        calc("10 / (5 - 5)")


def test_calc_float_numbers():
    assert calc("2.5 + 3.5") == 6.0
    assert calc("5.0 - 2.0") == 3.0
    assert calc("4.2 * 3.0") == 12.6
    assert calc("8.4 / 2.0") == 4.2


def test_calc_malformed_expressions3():
    with pytest.raises(Exception):
        calc("4 + 3)")

def test_calc_malformed_expressions1():
    with pytest.raises(Exception):
        calc("2 + * 3")


def test_calc_malformed_expressions2():
    with pytest.raises(Exception):
        calc("5 / (2 - 2")

def test_calc_whitespace_handling():
    assert calc("  2   +    3 ") == 5
    assert calc("  (  4  *  2 )  ") == 8
    assert calc(" - 5 +   3 ") == -2


def test_calc_combined_operators():
    assert calc("3 + -2 * 4") == -5
    assert calc("10 / -2 + 3") == -2.0
    assert calc("-5 + 6 / -3") == -7.0


def test_calc_nested_parentheses():
    assert calc("((2 + 3) * (4 - 1)) / (1 + 1)") == 7.5
    assert calc("-( (1 + 2) * (3 + (4 - 1)) )") == -18
    assert calc("(((-5)))") == -5


def test_calc_large_expression():
    expr = "3 + 5 * (2 - 8) / (4 + 1) + -7 * (3 - 1) + (6 / 2) * (1 + 1)"
    assert calc(expr) == -11.0


def test_calc_zero_and_negative_results():
    assert calc("0 + 0") == 0
    assert calc("5 - 5") == 0
    assert calc("3 * 0") == 0
    assert calc("0 / 5") == 0
    assert calc("2 - 5") == -3
    assert calc("-3 + -2") == -5
    assert calc("-4 * 2") == -8
    assert calc("-10 / 2") == -5.0


def test_calc_edge_cases():
    assert calc("0") == 0
    assert calc("-0") == 0
    assert calc("-(0)") == 0
    assert calc("((0))") == 0
    assert calc("1 + -0") == 1
    assert calc("-(-0)") == 0
    assert calc("-(1 - 1)") == 0


def test_calc_large_numbers():
    assert calc("1000000 + 2000000") == 3000000
    assert calc("5000000 - 3000000") == 2000000
    assert calc("4000 * 3000") == 12000000
    assert calc("8000000 / 2") == 4000000.0
    assert calc("-1000000 + 500000") == -500000
    assert calc("-(2000000 - 3000000)") == 1000000
    assert calc("1000000 * -3") == -3000000
    assert calc("-4000000 / 2") == -2000000.0


def test_calc_decimal_precision():
    assert calc("0.1 + 0.2") == pytest.approx(0.3)
    assert calc("1.333 + 2.667") == pytest.approx(4.0)
    assert calc("5.555 - 2.222") == pytest.approx(3.333)
    assert calc("3.14 * 2") == pytest.approx(6.28)
    assert calc("7.5 / 2.5") == pytest.approx(3.0)
    assert calc("-0.1 + 0.1") == pytest.approx(0.0)
    assert calc("-(1.5 - 2.5)") == pytest.approx(1.0)
    assert calc("2.5 * -4") == pytest.approx(-10.0)


def test_calc_multiple_unary_negations():
    assert calc("-(-3 + 2)") == 1


def test_calc_complex_expressions():
    assert calc("3 + 4 * 2 / (1 - 5) + -3") == -2
    assert calc("-(2 + 3) * (4 - 1) / -5") == 3
    assert calc("5 + ((1 + 2) * 4) - 3") == 14
