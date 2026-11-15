import pytest

from counter_os.application.common.error import Error
from counter_os.application.common.error_codes import ErrorCode
from counter_os.application.common.result import Result


@pytest.fixture
def error_result():
    return Result(Error(ErrorCode.COUNT_CANNOT_BE_NEGATIVE, "some error message"))
