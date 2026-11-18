from dataclasses import FrozenInstanceError

import pytest

from counter_os.application.dtos.error_response import ErrorCode, ErrorResponse
from counter_os.application.dtos.success_response import SuccessResponse
from counter_os.application.result import (
    Error,
    Result,
    Success,
)


def test_Result_can_capture_Success_objects():
    result: Result = Success(SuccessResponse())
    assert isinstance(result, Success)


def test_Result_can_capture_Error_objects():
    result: Result = Error(ErrorResponse.count_cannot_be_greater_than_100(101))
    assert isinstance(result, Error)


def test_Success_init_raises_TypeError_when_no_args():
    with pytest.raises(TypeError):
        Success()


def test_Error_init_raises_TypeError_when_no_args():
    with pytest.raises(TypeError):
        Error()


def test_Error_makes_error_message_and_code_accesible():
    result: Result = Error(ErrorResponse.count_cannot_be_negative(-1))
    assert (
        result.error_response.message
        == "-1 is a negative value and count cannot be negative."
    )
    assert result.error_response.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE


def test_Result_Error_is_immutable():
    result: Result = Error(ErrorResponse.count_cannot_be_negative(-1))
    error: ErrorResponse = ErrorResponse.count_cannot_be_greater_than_100(101)
    with pytest.raises(FrozenInstanceError):
        result._error_response = error


def test_Result_Success_is_immutable():
    result: Result = Success(SuccessResponse())
    with pytest.raises(FrozenInstanceError):
        result._success_response = SuccessResponse()
