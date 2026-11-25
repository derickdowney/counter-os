from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.in_memory_counter_repository import (
    InMemoryCounterRepository,
)
from counter_os.infrastructure.persistence.repository_type import RepositoryType
from counter_os.infrastructure.persistence.sqlite_counter_repository import (
    SqliteCounterRepository,
)


def create_repositories() -> tuple[CounterRepository]:
    settings = ApplicationConfiguration.from_environment()
    match settings.counter_repository_type:
        case RepositoryType.MEMORY:
            return (InMemoryCounterRepository(),)
        case RepositoryType.SQLITE_LOCAL:
            return (SqliteCounterRepository("test.db3"),)
        case _:
            return (InMemoryCounterRepository(),)
