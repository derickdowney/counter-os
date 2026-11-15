from dataclasses import dataclass
from typing import Any

from counter_os.application.common.error_codes import ErrorCode


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
