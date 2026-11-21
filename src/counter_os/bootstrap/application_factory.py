from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.bootstrap.repository_factory import create_repositories
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


def create_application_container(
    counter_presenter: CounterPresenter,
) -> ApplicationContainer:
    repositories: tuple[CounterRepository] = create_repositories()
    return ApplicationContainer(
        counter_repository=repositories[0], counter_presenter=counter_presenter
    )
