from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.presenters.flask_counter_presenter import (
    FlaskCounterPresenter,
)


def test_FlaskCounterPresenter_is_child_of_CounterPresenter_ABC():
    presenter = FlaskCounterPresenter()
    assert isinstance(presenter, CounterPresenter)


def test_FlaskCounterPresenter_present_counter_response():
    counter_vm = FlaskCounterPresenter().present_counter_response(
        CounterResponse.from_entity(Counter(Count(79)))
    )
    assert counter_vm.current_count == 79
