import pytest

from counter_os.application.common.error import Error
from counter_os.application.common.error_codes import ErrorCode
from counter_os.application.common.result import Result


def test_Result_init_with_no_args_is_success():
    result: Result = Result()
    assert result.is_success


def test_Result_failure_init_requires_error_arg():
    with pytest.raises(TypeError):
        Result.failure()


def test_Result_error_code_and_message_are_accessible():
    error: Error = Error(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, "test message")
    result: Result = Result.failure(error)
    assert result.error.code == "COUNT_CANNOT_BE_NEGATIVE"
    assert result.error.message == "test message"
