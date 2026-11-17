from dataclasses import FrozenInstanceError

import pytest

from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


def test_ErrorViewModel_init_requires_message():
    with pytest.raises(TypeError):
        ErrorViewModel()


def test_ErrorViewModel_is_immutable():
    error_vm = ErrorViewModel("msg1")
    with pytest.raises(FrozenInstanceError):
        error_vm.message = "msg2"
