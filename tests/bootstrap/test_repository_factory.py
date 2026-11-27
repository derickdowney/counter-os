from unittest.mock import Mock

from counter_os.bootstrap.repository_factory import create_repositories
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.in_memory_counter_repository import (
    InMemoryCounterRepository,
)
from counter_os.infrastructure.persistence.postgres_counter_repository import (
    PostgresCounterRepository,
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
    monkeypatch.setenv("COUNTER_REPOSITORY_LOCATION_SQLITE_LOCAL", "test.db3")
    monkeypatch.chdir(tmp_path)
    repositories: tuple[CounterRepository] = create_repositories()
    assert isinstance(repositories[0], SqliteCounterRepository)


def test_create_repositories_creates_postgres_repo_from_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", RepositoryType.POSTGRES_LOCAL)
    monkeypatch.setenv(
        "COUNTER_REPOSITORY_LOCATION_POSTGRES_LOCAL",
        "some:test@localhost:5432/counter_os",
    )

    configured_locations: list[str] = []

    def fake_configure(self, location: str) -> None:
        configured_locations.append(location)
        self._session_factory = Mock()

    monkeypatch.setattr(
        PostgresCounterRepository, "_configure_sql_alchemy", fake_configure
    )

    monkeypatch.chdir(tmp_path)
    repositories: tuple[CounterRepository] = create_repositories()
    assert len(repositories) == 1
    assert isinstance(repositories[0], PostgresCounterRepository)
    assert configured_locations == ["some:test@localhost:5432/counter_os"]
