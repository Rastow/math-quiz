from numbers import Number
import operator
import random
from typing import Callable


Operator = Callable[[Number, Number], Number]

OPERATORS: tuple[Operator, ...] = (operator.add, operator.sub, operator.mul)


class Problem:
    """Simple math problem."""

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
        """String representation of the arithmetic operator."""
        match self.arithmetic_operator:
            case operator.add:
                return "+"
            case operator.sub:
                return "-"
            case operator.mul:
                return "*"
            case _:
                raise ValueError("Unknown operator.")

    def solution(self) -> int:
        """Solution of the math problem."""
        return self.arithmetic_operator(self.first_operand, self.second_operand)


def quiz() -> None:
    """Math quiz game."""
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    score: int = 0
    questions_asked: int = 0
    total_questions: int = 5

    while questions_asked < total_questions:
        problem = Problem()
        print(f"Question: {str(problem)}")

        # parse user input as an integer, retry if parsing fails
        while True:
            try:
                answer = int(input("Your answer: "))
            except ValueError:
                print("Please enter an integer.")
                continue
            else:
                break

        if answer == problem.solution():
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {problem.solution()}.")

        questions_asked += 1

    print(f"Game over! Your score is: {score} / {total_questions}")


if __name__ == "__main__":
    quiz()
