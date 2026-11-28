from enum import StrEnum

from counter_os.infrastructure.frontend_type import FrontendType


def test_FrontendType_is_StrEnum():
    assert isinstance(FrontendType.CLI, StrEnum)


def test_FrontendType_CLI_is_cli():
    assert FrontendType.CLI == "cli"


def test_FrontendType_FLASK_is_flask():
    assert FrontendType.FLASK == "flask"
