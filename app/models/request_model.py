# request validation

from typing import Optional

from pydantic import BaseModel, field_validator


class CalculatorRequest(BaseModel):

    x: float
    y: Optional[float] = None
    operator: str

    @field_validator("operator")
    @classmethod
    def validate_operator(cls, value):

        allowed_operators = [
            "+",
            "-",
            "*",
            "/",
            "%",
            "^",
            "sqrt"
        ]

        if value not in allowed_operators:
            raise ValueError(
                "Invalid operator provided"
            )

        return value

    @field_validator("x")
    @classmethod
    def validate_x(cls, value):

        if abs(value) > 100000:
            raise ValueError(
                "x value too large"
            )

        return value

    @field_validator("y")
    @classmethod
    def validate_y(cls, value):

        if value is not None and abs(value) > 100000:
            raise ValueError(
                "y value too large"
            )

        return value