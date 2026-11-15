from counter_os.application.common.result import Result


def test_Result_init_with_no_args_is_success():
    result: Result = Result()
    assert result.is_success
