from dataclasses import FrozenInstanceError

import pytest

from counter_os.bootstrap.application_settings import ApplicationSettings
from counter_os.infrastructure.persistence.repository_type import RepositoryType


def test_ApplicationSettings_use_default_settings_when_no_env_file(monkeypatch):
    monkeypatch.delenv("COUNTER_REPOSITORY_TYPE", raising=False)

    settings: ApplicationSettings = ApplicationSettings.from_environment()

    assert settings.counter_repository_type == RepositoryType.MEMORY


def test_ApplicationSettings_ensure_from_environment_pulls_actual_env_var(monkeypatch):
    monkeypatch.setenv("COUNTER_REPOSITORY_TYPE", "test_repo_type")

    settings: ApplicationSettings = ApplicationSettings.from_environment()

    assert settings.counter_repository_type == "test_repo_type"


def test_ApplicationSettings_is_immutable():
    settings = ApplicationSettings.from_environment()
    with pytest.raises(FrozenInstanceError):
        settings.counter_repository_type = "test"
