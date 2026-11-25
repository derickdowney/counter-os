from dataclasses import FrozenInstanceError

import pytest

import counter_os.bootstrap.application_configuration
from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.infrastructure.persistence.repository_type import RepositoryType


def test_ApplicationConfiguration_use_default_settings_when_no_env_file(monkeypatch):
    monkeypatch.delenv("COUNTER_REPOSITORY_TYPE", raising=False)
    monkeypatch.setattr(
        counter_os.bootstrap.application_configuration,
        "load_dotenv",
        lambda *args, **kwargs: False,
    )
    settings: ApplicationConfiguration = ApplicationConfiguration.from_environment()
    assert settings.counter_repository_type == RepositoryType.MEMORY


def test_ApplicationConfiguration_ensure_from_environment_pulls_actual_env_var(
    monkeypatch,
):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", "test_repo_type")

    settings: ApplicationConfiguration = ApplicationConfiguration.from_environment()

    assert settings.counter_repository_type == "test_repo_type"


def test_ApplicationConfiguration_is_immutable():
    settings = ApplicationConfiguration.from_environment()
    with pytest.raises(FrozenInstanceError):
        settings.counter_repository_type = "test"
