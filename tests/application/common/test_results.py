from enum import StrEnum

from counter_os.application.common.results import ErrorCode


def test_ErrorCode_is_StrEnum():
    assert isinstance(ErrorCode.COUNTER_CANNOT_BE_NEGATIVE, StrEnum)
