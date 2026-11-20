from counter_os.application_settings import ApplicationSettings


def test_ApplicationSettings_use_default_settings_when_no_env_file(monkeypatch):
    monkeypatch.delenv("COUNTER_REPOSITORY_TYPE", raising=False)

    settings: ApplicationSettings = ApplicationSettings.from_environment()

    assert settings.counter_repository_type == "memory"
