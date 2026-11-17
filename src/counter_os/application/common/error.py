from dataclasses import dataclass
from typing import Any

from counter_os.application.common.error_codes import ErrorCode
from counter_os.domain.entities.counter import Counter


@dataclass(frozen=True)
class Error:
    """Standardized error information"""

    code: ErrorCode
    message: str
    details: dict[str, Any] | None = None

    @classmethod
    def count_cannot_be_negative(cls, value: int) -> Error:
        return cls(
            code=ErrorCode.COUNT_CANNOT_BE_NEGATIVE,
            message=f"{value} is a negative value and count cannot be negative.",
        )

    @classmethod
    def count_cannot_be_greater_than_100(cls, value: int) -> Error:
        return cls(
            code=ErrorCode.COUNT_CANNOT_BE_GREATER_THAN_100,
            message=f"{value} is greater than 100 and count cannot be greater than 100.",
        )
