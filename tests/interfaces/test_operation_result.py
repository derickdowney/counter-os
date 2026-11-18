from dataclasses import FrozenInstanceError

import pytest

from counter_os.interfaces.operation_result import (
    OperationFailure,
    OperationResult,
    OperationSuccess,
)
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel
from counter_os.interfaces.view_models.success_view_model import SuccessViewModel


def test_OperationResult_can_capture_OperationSuccess_objects():
    op_result: OperationResult = OperationSuccess(SuccessViewModel())
    assert isinstance(op_result, OperationSuccess)


def test_OperationResult_can_capture_OperationFailure_objects():
    error_vm: ErrorViewModel = ErrorViewModel("message", "code")
    op_result: OperationResult = OperationFailure(error_vm)
    assert isinstance(op_result, OperationFailure)


def test_OperationSuccess_init_with_no_args_raises_TypeError():
    with pytest.raises(TypeError):
        OperationSuccess()


def test_OperationSuccess_raises_TypeError_when_init_without_vm_class():
    with pytest.raises(TypeError):
        OperationSuccess(0)


def test_OperationSuccess_is_immutable():
    op_success = OperationSuccess(SuccessViewModel())
    with pytest.raises(FrozenInstanceError):
        op_success._success_vm = SuccessViewModel()


def test_OperationFailure_init_with_no_args_raises_TypeError():
    with pytest.raises(TypeError):
        OperationFailure()


def test_OperationFailure_raises_TypeError_when_init_without_vm_class():
    with pytest.raises(TypeError):
        OperationFailure(0)


def test_OperationFailure_is_immutable():
    op_failure: OperationFailure = OperationFailure(ErrorViewModel("", ""))
    with pytest.raises(FrozenInstanceError):
        op_failure._error_vm = ErrorViewModel("", "")


def test_OperationFailure_error_view_model_message_and_code_are_accessible():
    op_failure = OperationFailure(ErrorViewModel("some message", "some code"))
    assert op_failure.error_vm.message == "some message"
    assert op_failure.error_vm.code == "some code"


#
# def test_OperationResult_succeed_init_assigns_arg_to_success_field():
#     op_result: OperationResult[str] = OperationResult.succeed("success")
#     assert op_result._success == "success"
#     assert op_result._error is None
#
#
# def test_OperationResult_fail_init_assigns_args_to_error_view_model_field():
#     op_result: OperationResult[str] = OperationResult.fail("error msg")
#     assert isinstance(op_result._error, ErrorViewModel)
#     assert op_result._error.message == "error msg"
#     assert op_result._error.code is None
#     assert op_result._success is None
#
#
# def test_OperationResult_property_is_success():
#     op_result: OperationResult[str] = OperationResult.succeed("success")
#     assert op_result.is_success
#     assert not op_result.is_failure
#
#
# def test_OperationResult_property_is_failure():
#     op_result: OperationResult[str] = OperationResult.fail("error")
#     assert op_result.is_failure
#     assert not op_result.is_success
