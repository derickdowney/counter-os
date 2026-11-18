from dataclasses import FrozenInstanceError
from enum import StrEnum

import pytest

from counter_os.application.dtos.error_response import ErrorCode, ErrorResponse


def test_ErrorCode_is_StrEnum():
    assert isinstance(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, StrEnum)


def test_ErrorResponse_init_requires_args():
    with pytest.raises(TypeError):
        ErrorResponse()


def test_ErrorResponse_is_immutable():
    error = ErrorResponse(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, "old message")
    with pytest.raises(FrozenInstanceError):
        error.message = "new message"


def test_ErrorResponse_count_cannot_be_negative():
    error = ErrorResponse.count_cannot_be_negative(-1)
    assert error.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE
    assert error.message == "-1 is a negative value and count cannot be negative"


def test_ErrorResponse_count_cannot_be_greater_than_100():
    error = ErrorResponse.count_cannot_be_greater_than_100(101)
    assert error.code == ErrorCode.COUNT_CANNOT_BE_GREATER_THAN_100
    assert (
        error.message == "101 is greater than 100 and count cannot be greater than 100"
    )
