import os

import typer

# NOTE: TYPER IS BUILT ON TOP OF CLICK SO I PROBABLY SHOULD HAVE JUST USED CLICK

# from counter_os.infrastructure.configuration.container import Application


class TyperCli:
    def __init__(self):
        # def __init__(self, app: Application):
        # self.app = app
        self.cli = typer.Typer()

        # Register the CLI's entry point.
        self.cli.command()(self._main)

    def run(self) -> int:
        """Entry point for running the Typer CLI."""
        return self.cli()

    def _main(self) -> int:
        """Main application loop."""
        while True:
            self._display_menu()
            self._handle_selection()

    def _display_menu(self) -> None:
        self._clear_screen()
        typer.echo("CounterOS")
        typer.echo("---------")
        typer.echo("[1] View counter")
        typer.echo("[2] Increment counter")
        typer.echo("[3] Reset counter")
        typer.echo("[q] Quit")

    def _clear_screen(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def _handle_selection(self) -> None:
        selection = typer.prompt("Select an option").strip().lower()

        if selection == "1":
            print("Selected: 1")
            # self._view_counter()

        elif selection == "2":
            print("Selected: 2")
            # self._increment_counter()

        elif selection == "3":
            print("Selected: 3")
            # self._reset_counter()

        elif selection == "q":
            raise typer.Exit()

        else:
            typer.secho("Invalid selection.", fg=typer.colors.RED)
