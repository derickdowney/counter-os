import pytest

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.bootstrap.application_factory import create_application_container
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


@pytest.fixture
def mock_counter_presenter():
    class MockCounterPresenter(CounterPresenter):
        def present_counter_response(self, counter_response):
            pass

        def present_error_response(self, error_response):
            pass

    return MockCounterPresenter()


def test_create_application_container_factory(
    mock_counter_presenter,
):
    app: ApplicationContainer = create_application_container(mock_counter_presenter)
    assert isinstance(app, ApplicationContainer)
