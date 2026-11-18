from dataclasses import FrozenInstanceError
from enum import StrEnum

import pytest

from counter_os.application.result import (
    Error,
    ErrorCode,
    Failure,
    Result,
    Success,
)


@pytest.fixture()
def result_failure() -> Failure:
    return Failure(Error.count_cannot_be_negative(-1))


def test_ErrorCode_is_StrEnum():
    assert isinstance(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, StrEnum)


def test_Error_init_requires_error_code_and_error_message_and_optional_details():
    Error(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, "Test")
    with pytest.raises(TypeError):
        Error()


def test_Error_is_immutable():
    error: Error = Error(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, "old message")
    with pytest.raises(FrozenInstanceError):
        error.message = "new message"


def test_Error_count_cannot_be_negative():
    error: Error = Error.count_cannot_be_negative(-1)
    assert error.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE
    assert error.message == "-1 is a negative value and count cannot be negative."


def test_Error_count_cannot_be_greater_than_100():
    error: Error = Error.count_cannot_be_greater_than_100(101)
    assert error.code == ErrorCode.COUNT_CANNOT_BE_GREATER_THAN_100
    assert (
        error.message == "101 is greater than 100 and count cannot be greater than 100."
    )


def test_Result_can_capture_Success_objects():
    result: Result = Success(0)
    assert isinstance(result, Success)


def test_Result_can_capture_Failure_objects():
    result: Result = Failure(Error.count_cannot_be_greater_than_100(101))
    assert isinstance(result, Failure)


def test_Result_init_with_no_args_raises_TypeError():
    with pytest.raises(TypeError):
        Result()


def test_Failure_init_requires_error_arg():
    with pytest.raises(TypeError):
        Failure()


def test_Result_Failure_makes_error_message_and_code_accesible(result_failure):
    assert (
        result_failure.error.message
        == "-1 is a negative value and count cannot be negative."
    )
    assert result_failure.error.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE


def test_Result_Failure_is_immutable(result_failure):
    error: Error = Error.count_cannot_be_greater_than_100(101)
    with pytest.raises(FrozenInstanceError):
        result_failure.error = error


def test_Result_Success_is_immutable():
    result: Result = Success(0)
    with pytest.raises(FrozenInstanceError):
        result.success = 1


def test_Success_init_requires_any_arg():
    with pytest.raises(TypeError):
        Success()


def test_Result_Success_is_accessible():
    result: Result = Success("some value")
    assert isinstance(result.success, str)
    assert result.success == "some value"
