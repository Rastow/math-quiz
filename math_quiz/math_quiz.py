"""Math quiz module.

A math quiz consists of multiple math problems. Specifically, basic arithmetic skills are tested, including addition,
subtraction and multiplication of integers.
"""

from numbers import Number
import operator
import random
from typing import Callable


Operator = Callable[[Number, Number], Number]

# arithmetic operators supported by the problem class
OPERATORS: tuple[Operator, ...] = (operator.add, operator.sub, operator.mul)


class Problem:
    """Class representation of a simple math problem.

    Attributes
    ----------
    first_operand : int
        Integer between 1 and 10.
    second_operand : int
        Integer between 1 and 5.
    arithmetic_operator: Operator
        A arithmetic operator from the built-in ``operator`` module. Only addition, subtraction and multiplication are
        supported.
    """
    def __init__(self) -> None:
        """Math problem constructor."""
        self.first_operand = random.randint(1, 10)
        self.second_operand = random.randint(1, 5)
        self.arithmetic_operator = random.choice(OPERATORS)

    def __str__(self) -> str:
        """String representation of the math problem."""
        return f"{self.first_operand} {self.operator_symbol} {self.second_operand}"

    @property
    def operator_symbol(self) -> str:
        """String representation of the arithmetic operator.

        Raises
        ------
        ValueError
            If the arithmetic operator is unknown."""
        match self.arithmetic_operator:
            case operator.add:
                return "+"
            case operator.sub:
                return "-"
            case operator.mul:
                return "*"
            case _:
                raise ValueError("Unknown arithmetic operator.")

    def solution(self) -> int:
        """Solution of the math problem."""
        return self.arithmetic_operator(self.first_operand, self.second_operand)


class Quiz:
    """Math quiz which tests your basic arithmetic skills.

    Attributes
    ----------
    score : int
        Points collected by answering questions correctly.
    questions_asked : int
        Number of questions answered by the user.
    total_questions : int
        Total number of questions being asked.
    """
    def __init__(self) -> None:
        """Quiz initialization."""
        print("Welcome to the Math Quiz Game!")
        print("You will be presented with math problems, and you need to provide the correct answers.")

        self.score = 0
        self.questions_asked = 0
        self.total_questions = 5

        self.run()

    def run(self) -> None:
        """Starts the game."""
        while self.questions_asked < self.total_questions:
            problem = Problem()
            print(f"Question: {str(problem)}")

            answer = self._parse_answer()
            if answer == problem.solution():
                print("Correct! You earned a point.")
                self.score += 1
            else:
                print(f"Wrong answer. The correct answer is {problem.solution()}.")

            self.questions_asked += 1

        print(f"Game over! Your score is: {self.score} / {self.total_questions}")

    @staticmethod
    def _parse_answer() -> int:
        """Try to interpret user input as an integer. Retry if parsing fails.

        Returns
        -------
        int
            Parsed user input.
        """
        while True:
            try:
                return int(input("Your answer: "))
            except ValueError:
                print("Please enter an integer.")
                continue


if __name__ == "__main__":
    Quiz()
