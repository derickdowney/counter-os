from enum import StrEnum

from counter_os.application.common.error_codes import ErrorCode


def test_ErrorCode_is_StrEnum():
    assert isinstance(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, StrEnum)
