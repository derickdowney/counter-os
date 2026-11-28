from enum import StrEnum

from counter_os.bootstrap.application_environment_type import ApplicationEnvironmentType


def test_ApplicationEnvironment_is_StrEnum():
    assert isinstance(ApplicationEnvironmentType.DEVELOPMENT, StrEnum)


def test_ApplicationEnvironment_DEVELOPMENT():
    assert ApplicationEnvironmentType.DEVELOPMENT == "development"


def test_ApplicationEnvironment_PRODUCTION():
    assert ApplicationEnvironmentType.PRODUCTION == "production"
