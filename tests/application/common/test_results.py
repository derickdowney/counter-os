from dataclasses import FrozenInstanceError
from enum import StrEnum

import pytest

from counter_os.application.common.results import Error, ErrorCode


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
