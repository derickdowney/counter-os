import sys

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_factory import create_application_container
from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)


def main() -> int:
    """
    Main entry point for the CLI application.

    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    try:
        config = ApplicationConfiguration.from_environment()
        app_container = create_application_container(
            config=config,
            counter_presenter=ClickCounterPresenter(),
        )
        click_cli_app = ClickCliApp(app_container)
        return click_cli_app.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
