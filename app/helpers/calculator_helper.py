# The math happens here
import logging
import math


logger = logging.getLogger(__name__)


def add(x: float, y: float):
    logger.info(f"Performing Addition: {x} + {y}")
    return x + y


def subtract(x: float, y: float):
    logger.info(f"Performing Subtraction: {x} - {y}")
    return x - y


def multiply(x: float, y: float):
    logger.info(f"Performing Multiplication: {x} * {y}")
    return x * y


def divide(x: float, y: float):
    logger.info(f"Performing Division: {x} / {y}")

    if y == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Division by zero is not allowed")

    return x / y

def modulus(x: float, y: float):
    logger.info(f"Performing Modulus: {x} % {y}")

    if y == 0:
        logger.error("Modulus by zero attempted")
        raise ValueError("Modulus by zero is not allowed")

    return x % y


def power(x: float, y: float):

    logger.info(f"Performing Power: {x} ^ {y}")

    if  abs(y) > 100:
        logger.error(f"Exponent too large: {y}")
        raise ValueError("Exponent value too large")

    return x ** y

def square_root(x: float):
    logger.info(f"Performing Square Root: sqrt({x})")

    if x < 0:
        logger.error("Square root of negative number attempted")
        raise ValueError(
            "Square root of negative number is not allowed"
        )

    return math.sqrt(x)