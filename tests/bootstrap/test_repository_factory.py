from counter_os.bootstrap.repository_factory import create_repositories
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.in_memory_counter_repository import (
    InMemoryCounterRepository,
)
from counter_os.infrastructure.persistence.repository_type import RepositoryType
from counter_os.infrastructure.persistence.sqlite_counter_repository import (
    SqliteCounterRepository,
)


def test_create_repositories_from_environment_variables(monkeypatch):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", RepositoryType.MEMORY)
    repositories: tuple[CounterRepository] = create_repositories()
    assert isinstance(repositories[0], InMemoryCounterRepository)


def test_create_repositories_creates_memory_repo_when_no_valid_env_var(monkeypatch):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", "not_a_valid_type")
    repositories: tuple[CounterRepository] = create_repositories()
    assert isinstance(repositories[0], InMemoryCounterRepository)


def test_create_repositories_creates_sqlite_repo_from_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", RepositoryType.SQLITE_LOCAL)
    monkeypatch.setenv("COUNTER_REPOSITORY_LOCATION", "test.db3")
    monkeypatch.chdir(tmp_path)
    repositories: tuple[CounterRepository] = create_repositories()
    assert isinstance(repositories[0], SqliteCounterRepository)
