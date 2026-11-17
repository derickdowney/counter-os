import pytest

from counter_os.interfaces.view_models.error_view_model import ErrorViewModel
from counter_os.interfaces.view_models.operation_result import OperationResult


def test_OperationResult_init_requires_either_success_or_error_but_never_both():
    success: str = "success"
    error_vm: ErrorViewModel = ErrorViewModel("error")
    OperationResult(success=success)  # should not raise ValueError
    OperationResult(error=error_vm)  # should not raise ValueError
    with pytest.raises(ValueError):
        OperationResult()
    with pytest.raises(ValueError):
        OperationResult(success=success, error=error_vm)


def test_OperationResult_succeed_init_assigns_arg_to_success_field():
    op_result: OperationResult[str] = OperationResult.succeed("success")
    assert op_result._success == "success"
    assert op_result._error is None


def test_OperationResult_fail_init_assigns_args_to_error_view_model_field():
    op_result: OperationResult[str] = OperationResult.fail("error msg")
    assert isinstance(op_result._error, ErrorViewModel)
    assert op_result._error.message == "error msg"
    assert op_result._error.code is None
    assert op_result._success is None
