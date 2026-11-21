from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.in_memory_counter_repository import (
    InMemoryCounterRepository,
)
from counter_os.infrastructure.persistence.repository_type import RepositoryType


def create_repositories() -> tuple[CounterRepository]:
    settings = ApplicationConfiguration.from_environment()
    if settings.counter_repository_type == RepositoryType.MEMORY:
        return (InMemoryCounterRepository(),)

    return (InMemoryCounterRepository(),)
