import pytest

from calc_expr import calc


def test_calc_malformed_expressions3():
    with pytest.raises(Exception):
        calc("4 + 3)")
