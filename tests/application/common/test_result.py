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
