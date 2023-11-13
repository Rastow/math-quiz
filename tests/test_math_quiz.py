import itertools
import operator

import pytest

from math_quiz import Problem


@pytest.fixture
def problem() -> Problem:
    return Problem()


def test_problem_invalid_operator(problem):
    problem.arithmetic_operator = operator.truediv
    with pytest.raises(ValueError) as exc_info:
        print(problem.operator_symbol)
        assert "Unknown operator." in str(exc_info.value)


@pytest.fixture
def problems() -> list[Problem]:
    return [Problem() for _ in range(100)]


def test_problem_valid_integers(problems):
    for problem in problems:
        assert 1 <= problem.first_operand <= 10
        assert 1 <= problem.second_operand <= 5


def test_problem_valid_operator(problems):
    for problem in problems:
        assert problem.operator_symbol in ("+", "-", "*")
        assert problem.arithmetic_operator in (operator.add, operator.sub, operator.mul)


def test_problem_solution(problems):
    for problem in problems:
        match problem.operator_symbol:
            case "+":
                assert problem.solution() == problem.first_operand + problem.second_operand
            case "-":
                assert problem.solution() == problem.first_operand - problem.second_operand
            case "*":
                assert problem.solution() == problem.first_operand * problem.second_operand
            case _:
                pytest.fail("Unknown operator.")
