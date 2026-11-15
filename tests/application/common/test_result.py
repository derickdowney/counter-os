from dataclasses import FrozenInstanceError

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


def test_Result_error_code_and_message_are_accessible(error_result):
    assert error_result.error.code == "COUNT_CANNOT_BE_NEGATIVE"
    assert error_result.error.message == "some error message"


def test_Result_is_immutable(error_result):
    new_error: Error = Error(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, "new message")
    with pytest.raises(FrozenInstanceError):
        error_result.error = new_error
