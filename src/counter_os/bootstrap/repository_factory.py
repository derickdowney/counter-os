from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.counter_repository_type import (
    CounterRepositoryType,
)
from counter_os.infrastructure.persistence.in_memory_counter_repository import (
    InMemoryCounterRepository,
)
from counter_os.infrastructure.persistence.postgres_counter_repository import (
    PostgresCounterRepository,
)
from counter_os.infrastructure.persistence.sqlite_counter_repository import (
    SqliteCounterRepository,
)


def create_repositories() -> tuple[CounterRepository]:
    settings = ApplicationConfiguration.from_environment()
    match settings.counter_repository_type:
        case CounterRepositoryType.MEMORY:
            return (InMemoryCounterRepository(),)
        case CounterRepositoryType.SQLITE_LOCAL:
            return (
                SqliteCounterRepository(
                    settings.counter_repository_location_sqlite_local
                ),
            )
        case CounterRepositoryType.POSTGRES_LOCAL:
            return (
                PostgresCounterRepository(
                    settings.counter_repository_location_postgres_local
                ),
            )
        case _:
            return (InMemoryCounterRepository(),)
