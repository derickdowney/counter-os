from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.presenters.typer_counter_presenter import (
    TyperCounterPresenter,
)


def test_TyperCounterPresenter_extends_CounterPresenter():
    assert isinstance(TyperCounterPresenter(), CounterPresenter)
