import sys

from counter_os.infrastructure.typer.typer_cli_app import TyperCli


def main() -> int:
    """
    Main entry point for the CLI application.

    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    try:
        # Create application with dependencies
        # app = create_application(
        #     notification_service=NotificationRecorder(),
        #     task_presenter=CliTaskPresenter(),
        #     project_presenter=CliProjectPresenter(),
        # )

        # Create and run appropriate CLI implementation
        # cli = ClickCli(app)
        cli = TyperCli()
        return cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        # print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
