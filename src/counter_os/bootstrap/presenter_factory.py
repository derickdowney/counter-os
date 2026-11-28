import sys

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.infrastructure.frontend_type import FrontendType
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


def create_presenters(config: ApplicationConfiguration) -> tuple[CounterPresenter]:
    match config.frontend_type:
        case FrontendType.CLI:
            return (ClickCounterPresenter(),)
        case _:
            print(
                f"Invalid FRONTEND_TYPE: '{config.frontend_type}'",
                file=sys.stderr,
            )
            print("Defaulting to 'ClickCounterPresenter'", file=sys.stderr)
            return (ClickCounterPresenter(),)
