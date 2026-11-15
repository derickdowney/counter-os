from dataclasses import FrozenInstanceError

import pytest

from counter_os.application.common.error import Error
from counter_os.application.common.error_codes import ErrorCode


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
    assert error.message == "-1 is negative value and count cannot be negative."
