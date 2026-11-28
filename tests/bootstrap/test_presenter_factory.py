from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.presenter_factory import create_presenters
from counter_os.infrastructure.frontend_type import FrontendType
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


def test_create_presenters_invalid_config(capsys):
    # Arrange
    config = ApplicationConfiguration(
        counter_repository_type="",
        counter_repository_location_sqlite_local="",
        counter_repository_location_postgres_local="",
        frontend_type="not a valid frontend",
    )

    # Act
    presenters: tuple[CounterPresenter] = create_presenters(config)

    # Assert
    output = capsys.readouterr()
    assert output.out == ""
    assert (
        output.err
        == "Invalid FRONTEND_TYPE: 'not a valid frontend'\nDefaulting to 'ClickCounterPresenter'\n"
    )
    assert len(presenters) == 1
    assert isinstance(presenters[0], ClickCounterPresenter)


def test_create_presenters_frontend_config():
    # Arrange
    config = ApplicationConfiguration(
        counter_repository_type="",
        counter_repository_location_sqlite_local="",
        counter_repository_location_postgres_local="",
        frontend_type=FrontendType.CLI,
    )

    # Act
    presenters: tuple[CounterPresenter] = create_presenters(config)

    # Assert
    assert len(presenters) == 1
    assert isinstance(presenters[0], ClickCounterPresenter)
