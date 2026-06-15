# handles Buisness logic

import logging

from app.helpers.calculator_helper import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    square_root
)

logger = logging.getLogger(__name__)


def calculate(x: float, y: float = None, operator: str = ""):

    logger.info(
        f"Calculation request received | "
        f"x={x}, y={y}, operator={operator}"
    )
        # Validation for operators requiring y

    binary_operators = [
        "+",
        "-",
        "*",
        "/",
        "%",
        "^"
    ]

    if operator in binary_operators and y is None:

        logger.error(
            f"{operator} operator requires y value"
        )

        raise ValueError(
            f"{operator} operator requires y value"
        )

    # Validation for sqrt operation

    if operator == "sqrt" and y is not None:

        logger.error(
            "sqrt operation should not receive y value"
        )

        raise ValueError(
            "sqrt operation does not require y"
        )

    # Addition
    if operator == "+":
        logger.info("Calling add function")
        return add(x, y)

    # Subtraction
    elif operator == "-":
        logger.info("Calling subtract function")
        return subtract(x, y)

    # Multiplication
    elif operator == "*":
        logger.info("Calling multiply function")
        return multiply(x, y)

    # Division
    elif operator == "/":
        logger.info("Calling divide function")
        return divide(x, y)

    # Modulus
    elif operator == "%":
        logger.info("Calling modulus function")
        return modulus(x, y)

    # Power
    elif operator == "^":
        logger.info("Calling power function")
        return power(x, y)

    # Square Root
    elif operator == "sqrt":
        logger.info("Calling square_root function")
        return square_root(x)

    # Invalid Operator
    else:
        logger.error(
            f"Invalid operator received: {operator}"
        )

        raise ValueError(
            "Invalid operator. "
            "Use +, -, *, /, %, ^, sqrt"
        )