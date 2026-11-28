import argparse
import sys

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_container_factory import (
    create_application_container,
)
from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", required=False, help="Frontend")
        parser.add_argument("-r", required=False, help="Counter Repository Type")
        args = parser.parse_args()

        config = ApplicationConfiguration.from_environment(
            counter_repository_type_override=args.r,
            frontend_override=args.f,
        )
        app_container = create_application_container(config)

        if isinstance(app_container.counter_presenter, ClickCounterPresenter):
            click_cli_app = ClickCliApp(app_container)
            return click_cli_app.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    main()
