from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


def test_ClickCounterPresenter_extends_CounterPresenter():
    assert isinstance(ClickCounterPresenter(), CounterPresenter)


def test_ClickCounterPresenter_present_counter_response():
    response = CounterResponse(10)
    presenter = ClickCounterPresenter()
    counter_vm: CounterViewModel = presenter.present_counter_response(response)
    assert counter_vm.current_count == 10


def test_ClickCounterPresenter_present_counter_error():
    response = ErrorResponse.count_cannot_be_negative(-1)
    presenter = ClickCounterPresenter()
    error_vm: ErrorViewModel = presenter.present_error_response(response)
    assert error_vm.message == "-1 is a negative value and count cannot be negative"
    assert error_vm.code == "COUNT_CANNOT_BE_NEGATIVE"
