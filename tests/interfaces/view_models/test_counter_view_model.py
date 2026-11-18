from dataclasses import FrozenInstanceError

import pytest

from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.success_view_model import SuccessViewModel


def test_CounterViewModel_init_requires_count_integer():
    with pytest.raises(TypeError):
        CounterViewModel()


def test_CounterViewModel_is_immutable():
    counter_vm = CounterViewModel(0)
    with pytest.raises(FrozenInstanceError):
        counter_vm.count = 1


def test_CounterViewModel_is_in_SuccessViewModel_class():
    counter_vm = CounterViewModel(0)
    assert isinstance(counter_vm, SuccessViewModel)
