from dataclasses import FrozenInstanceError
from enum import StrEnum

import pytest

from counter_os.application.dtos.error_response import ErrorCode, ErrorResponse
from counter_os.application.dtos.success_response import SuccessResponse
from counter_os.application.result import (
    Error,
    Result,
    Success,
)


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
    assert error.message == "-1 is a negative value and count cannot be negative."


def test_ErrorResponse_count_cannot_be_greater_than_100():
    error = ErrorResponse.count_cannot_be_greater_than_100(101)
    assert error.code == ErrorCode.COUNT_CANNOT_BE_GREATER_THAN_100
    assert (
        error.message == "101 is greater than 100 and count cannot be greater than 100."
    )


def test_Result_can_capture_Success_objects():
    result: Result = Success(SuccessResponse())
    assert isinstance(result, Success)


def test_Result_can_capture_Failure_objects():
    result: Result = Error(ErrorResponse.count_cannot_be_greater_than_100(101))
    assert isinstance(result, Error)


def test_Success_init_with_no_args_raises_TypeError():
    with pytest.raises(TypeError):
        Success()


# def test_Success_raises_TypeError_when_init_without_Success


def test_Error_init_requires_error_arg():
    with pytest.raises(TypeError):
        Error()


def test_Error_makes_error_message_and_code_accesible():
    result: Result = Error(ErrorResponse.count_cannot_be_negative(-1))
    assert (
        result.error.message == "-1 is a negative value and count cannot be negative."
    )
    assert result.error.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE


def test_Result_Failure_is_immutable():
    result: Result = Error(ErrorResponse.count_cannot_be_negative(-1))
    error: ErrorResponse = ErrorResponse.count_cannot_be_greater_than_100(101)
    with pytest.raises(FrozenInstanceError):
        result._error = error


def test_Result_Success_is_immutable():
    result: Result = Success(SuccessResponse())
    with pytest.raises(FrozenInstanceError):
        result._success = SuccessResponse()


def test_Success_init_requires_any_arg():
    with pytest.raises(TypeError):
        Success()


# def test_Result_Success_is_accessible():
#     result: Result = Success(SuccessResponse())
#     assert isinstance(result.success, Success)
