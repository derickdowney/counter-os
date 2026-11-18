from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.application.dtos.success_response import SuccessResponse


@dataclass(frozen=True)
class Error:
    _error: ErrorResponse

    def __post_init__(self):
        if not isinstance(self._error, ErrorResponse):
            raise TypeError("Argument must be or extend off ErrorResponse class")

    @property
    def error(self):
        return self._error


@dataclass(frozen=True)
class Success:
    _success: SuccessResponse

    def __post_init__(self):
        if not isinstance(self._success, SuccessResponse):
            raise TypeError("Argument must extend off SuccessResponse class")

    @property
    def success(self):
        return self._success


type Result = Success | Error
