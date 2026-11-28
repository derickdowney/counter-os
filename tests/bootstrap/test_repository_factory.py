from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.repository_factory import create_repositories
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.in_memory_counter_repository import (
    InMemoryCounterRepository,
)
from counter_os.infrastructure.persistence.postgres_counter_repository import (
    PostgresCounterRepository,
)
from counter_os.infrastructure.persistence.sqlite_counter_repository import (
    SqliteCounterRepository,
)


def test_create_repositories_invalid_config(capsys):
    # Arrange
    config = ApplicationConfiguration(
        counter_repository_type="not a repo type",
        counter_repository_location_sqlite_local="",
        counter_repository_location_postgres_local="",
        frontend_type="",
        app_env="",
    )

    # Act
    repositories: tuple[CounterRepository] = create_repositories(config)

    # Assert
    output = capsys.readouterr()
    assert output.out == ""
    assert (
        output.err
        == "Invalid CounterRepositoryType: 'not a repo type'\nDefaulting to InMemoryCounterRepository\n"
    )
    assert len(repositories) == 1
    assert isinstance(repositories[0], InMemoryCounterRepository)


def test_create_repositories_memory_config():
    # Arrange
    config = ApplicationConfiguration(
        counter_repository_type="memory",
        counter_repository_location_sqlite_local="",
        counter_repository_location_postgres_local="",
        frontend_type="",
        app_env="",
    )

    # Act
    repositories: tuple[CounterRepository] = create_repositories(config)

    # Assert
    assert len(repositories) == 1
    assert isinstance(repositories[0], InMemoryCounterRepository)


def test_create_repositories_sqlite_local_config(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.chdir(tmp_path)
    expected_db = tmp_path / "my_data.db"
    config = ApplicationConfiguration(
        counter_repository_type="sqlite_local",
        counter_repository_location_sqlite_local="my_data.db",
        counter_repository_location_postgres_local="",
        frontend_type="",
        app_env="",
    )

    # Act
    repositories: tuple[CounterRepository] = create_repositories(config)

    # Assert
    assert len(repositories) == 1
    assert isinstance(repositories[0], SqliteCounterRepository)
    assert expected_db.is_file()


def test_create_repositories_postgres_local_config(monkeypatch):
    # Arrange
    config = ApplicationConfiguration(
        counter_repository_type="postgres_local",
        counter_repository_location_sqlite_local="",
        counter_repository_location_postgres_local="a:b@localhost:1234/c",
        frontend_type="",
        app_env="",
    )
    monkeypatch.setattr(
        PostgresCounterRepository,
        "_configure_sql_alchemy",
        lambda *args, **kwargs: False,
    )

    # Act
    repositories: tuple[CounterRepository] = create_repositories(config)

    # Assert
    assert len(repositories) == 1
    assert isinstance(repositories[0], PostgresCounterRepository)
