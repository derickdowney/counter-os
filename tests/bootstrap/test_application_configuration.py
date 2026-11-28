from dataclasses import FrozenInstanceError

import pytest

import counter_os.bootstrap.application_configuration
from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_environment_type import ApplicationEnvironmentType
from counter_os.infrastructure.frontend_type import FrontendType
from counter_os.infrastructure.persistence.counter_repository_type import (
    CounterRepositoryType,
)


@pytest.fixture
def clean_counter_env(monkeypatch) -> None:
    monkeypatch.setattr(
        counter_os.bootstrap.application_configuration,
        "load_dotenv",
        lambda: None,
    )
    for var in (
        "COUNTER_REPOSITORY_TYPE",
        "COUNTER_REPOSITORY_LOCATION_SQLITE_LOCAL",
        "COUNTER_REPOSITORY_LOCATION_POSTGRES_LOCAL",
        "FRONTEND_TYPE",
        "APP_ENV",
    ):
        monkeypatch.delenv(var, raising=False)


def test_ApplicationConfiguration_use_default_settings_when_no_env_file(
    clean_counter_env,
):
    # Arrange
    clean_counter_env

    # Act
    settings: ApplicationConfiguration = ApplicationConfiguration.from_environment()

    # Assert
    assert settings.counter_repository_type == CounterRepositoryType.MEMORY
    assert settings.counter_repository_location_sqlite_local == "data.sqlite3"
    assert settings.counter_repository_location_postgres_local == (
        "user:password@localhost:5432/counter_os"
    )
    assert settings.frontend_type == FrontendType.CLI
    assert settings.app_env == ApplicationEnvironmentType.DEVELOPMENT


def test_ApplicationConfiguration_ensure_from_environment_pulls_actual_env_var(
    clean_counter_env,
    monkeypatch,
):
    # Arrange
    clean_counter_env
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", "test_repo_type")
    monkeypatch.setenv("COUNTER_REPOSITORY_LOCATION_SQLITE_LOCAL", "sqlite location")
    monkeypatch.setenv(
        "COUNTER_REPOSITORY_LOCATION_POSTGRES_LOCAL", "postgres location"
    )
    monkeypatch.setenv("FRONTEND_TYPE", "some frontend")
    monkeypatch.setenv("APP_ENV", "some environment")

    # Act
    settings: ApplicationConfiguration = ApplicationConfiguration.from_environment()

    # Assert
    assert settings.counter_repository_type == "test_repo_type"
    assert settings.counter_repository_location_sqlite_local == "sqlite location"
    assert settings.counter_repository_location_postgres_local == "postgres location"
    assert settings.frontend_type == "some frontend"
    assert settings.app_env == "some environment"


def test_ApplicationConfiguration_is_immutable():
    settings = ApplicationConfiguration.from_environment()
    with pytest.raises(FrozenInstanceError):
        settings.counter_repository_type = "test"
