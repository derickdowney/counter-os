import pytest

from counter_os.interfaces.controllers.counter_controller import CounterController


def test_CounterController_init_requires_counter_use_cases():
    with pytest.raises(TypeError):
        CounterController()
