import pytest

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.configuration.application_container import (
    ApplicationContainer,
)
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


@pytest.fixture
def counter_repository():
    class FakeCounterRepo(CounterRepository):
        def save(self, counter: Counter):
            pass

        def get(self):
            pass

    return FakeCounterRepo()


@pytest.fixture
def counter_presenter():
    class FakeCounterPresenter(CounterPresenter):
        def present_counter_response(self, counter_response: CounterResponse):
            pass

        def present_error_response(self, error_response: ErrorResponse):
            pass

    return FakeCounterPresenter()


def test_ApplicationContainer_init_requires_args():
    with pytest.raises(TypeError):
        ApplicationContainer()


def test_ApplicationCounter_init_requires_repo_and_presenter(
    counter_repository, counter_presenter
):
    app = ApplicationContainer(counter_repository, counter_presenter)
    assert isinstance(app.counter_repository, CounterRepository)
    assert isinstance(app.counter_presenter, CounterPresenter)
