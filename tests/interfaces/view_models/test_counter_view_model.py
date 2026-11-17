import pytest

from counter_os.interfaces.view_models.counter_view_model import CounterViewModel


def test_CounterViewModel_init_requires_count_integer():
    with pytest.raises(TypeError):
        CounterViewModel()
