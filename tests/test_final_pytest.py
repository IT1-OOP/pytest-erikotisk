import pytest
from src import final_pytest

@pytest.mark.parametrize(
    "a, b, c, expected_exception, expected_message",
    [
        ("Yip-Yap :3", 2, 1, TypeError, "All coefficients must be of type float or int!"),
        (0, 4, 4, SyntaxError, "Cannot solve quadratic formula with a = 0!"),
        (9, 5, 0, NameError, "I don't like when b = 5!"),
        (4, 4, 99999, ValueError, "Cannot solve quadratic formula with negative discriminant!")
    ],
)
def test_solve_quadratic_formula_errors(a, b, c, expected_exception, expected_message):
    with pytest.raises(expected_exception) as exc:
        final_pytest.solve_quadratic_formula(a, b, c)
    assert str(exc.value) == expected_message


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (2, 20, 0, (0.0, -10.0)),
        (1, -5, 6, (3.0, 2.0)),
        (1, -7, 10, (5.0, 2.0)),
    ]
)

def test_solve_quadratic_formute(a, b, c, expected):
    assert final_pytest.solve_quadratic_formula(a,b,c) == expected