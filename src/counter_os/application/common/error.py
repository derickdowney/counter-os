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
    def count_cannot_be_negative(cls, value: int) -> Self:
        return cls(
            code=ErrorCode.COUNT_CANNOT_BE_NEGATIVE,
            message=f"{value} is negative value and count cannot be negative.",
        )

    @classmethod
    def counter_cannot_decrement_below_zero(cls, counter: Counter) -> Self:
        return cls(
            code=ErrorCode.COUNTER_CANNOT_DECREMENT_BELOW_ZERO,
            message=f"Counter has a count value of {counter.count.value} and cannot be decremented below zero.",
        )
