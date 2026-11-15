from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class ErrorCode(StrEnum):
    COUNTER_CANNOT_BE_NEGATIVE = "COUNTER_CANNOT_BE_NEGATIVE"


@dataclass(frozen=True)
class Error:
    code: ErrorCode
    message: str
    details: dict[str, Any] | None = None
