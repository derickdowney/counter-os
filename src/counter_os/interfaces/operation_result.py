from dataclasses import dataclass

from counter_os.interfaces.view_models.error_view_model import ErrorViewModel
from counter_os.interfaces.view_models.success_view_model import SuccessViewModel


@dataclass(frozen=True)
class OperationFailure:
    _error_vm: ErrorViewModel  # TODO: change this to "_view_model"

    def __post_init__(self):
        if not isinstance(self._error_vm, ErrorViewModel):
            raise TypeError("Argument must be or extend off ErrorViewModel class")

    @property
    def error_vm(self):
        return self._error_vm


@dataclass(frozen=True)
class OperationSuccess:
    _success_vm: SuccessViewModel

    def __post_init__(self):
        if not isinstance(self._success_vm, SuccessViewModel):
            raise TypeError("Argument must extend off the SuccessViewModel class")

    @property
    def success_vm(self):
        return self._success_vm


type OperationResult = OperationSuccess | OperationFailure
