from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.presenters.flask_counter_presenter import (
    FlaskCounterPresenter,
)


def test_FlaskCounterPresenter_is_child_of_CounterPresenter_ABC():
    presenter = FlaskCounterPresenter()
    assert isinstance(presenter, CounterPresenter)
