from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.memory_counter_repository import (
    MemoryCounterRepository,
)
from counter_os.infrastructure.persistence.repository_type import RepositoryType
from counter_os.repository_factory import create_repositories


def test_create_repositories_from_environment_variables(monkeypatch):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", RepositoryType.MEMORY)

    repositories: tuple[CounterRepository] = create_repositories()

    assert isinstance(repositories[0], MemoryCounterRepository)
