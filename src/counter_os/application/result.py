from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.application.dtos.success_response import SuccessResponse


@dataclass(frozen=True)
class Error:
    _error_response: ErrorResponse

    def __post_init__(self):
        if not isinstance(self._error_response, ErrorResponse):
            raise TypeError("Argument must be or extend off ErrorResponse class")

    @property
    def error_response(self):
        return self._error_response


@dataclass(frozen=True)
class Success:
    _success_response: SuccessResponse

    def __post_init__(self):
        if not isinstance(self._success_response, SuccessResponse):
            raise TypeError("Argument must extend off SuccessResponse class")

    @property
    def success_response(self):
        return self._success_response


type Result = Success | Error
