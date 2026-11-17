import pytest

from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


def test_CounterPresenter_is_abstract():
    with pytest.raises(TypeError):
        CounterPresenter()
