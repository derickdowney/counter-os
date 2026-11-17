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
