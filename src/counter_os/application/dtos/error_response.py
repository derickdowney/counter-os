from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class ErrorCode(StrEnum):
    COUNT_CANNOT_BE_NEGATIVE = "COUNT_CANNOT_BE_NEGATIVE"
    COUNT_CANNOT_BE_GREATER_THAN_100 = "COUNT_CANNOT_BE_GREATER_THAN_100"
    VALIDATION_ERROR = "VALIDATION_ERROR"


@dataclass(frozen=True)
class ErrorResponse:
    """Standardized error response for an application-layer request"""

    code: ErrorCode
    message: str
    details: dict[str, Any] | None = None

    @classmethod
    def count_cannot_be_negative(cls, value: int) -> ErrorResponse:
        return cls(
            code=ErrorCode.COUNT_CANNOT_BE_NEGATIVE,
            message=f"{value} is a negative value and count cannot be negative",
        )

    @classmethod
    def count_cannot_be_greater_than_100(cls, value: int) -> ErrorResponse:
        return cls(
            code=ErrorCode.COUNT_CANNOT_BE_GREATER_THAN_100,
            message=f"{value} is greater than 100 and count cannot be greater than 100",
        )
