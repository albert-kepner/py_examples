from pathlib import Path
import typer

app = typer.Typer()

APP_VERSION = "1.0.0"


def version_callback(value: bool):
    if value:
        typer.echo(APP_VERSION)
        raise typer.Exit()


@app.command()
def main(
    path: Path | None = typer.Argument(
        None,
        help="Optional path to a file or directory",
    ),
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output",
    ),
):
    if verbose:
        typer.echo("Verbose mode enabled")

    if path is not None:
        # ✅ This is the key behavior you asked for
        typer.echo(f"Path: {path}")
    else:
        typer.echo("No path provided")


if __name__ == "__main__":
    app()

app = typer.Typer()

APP_VERSION = "1.0.0"


def version_callback(value: bool):
    if value:
        typer.echo(APP_VERSION)
        raise typer.Exit()


@app.command()
def main(
    path: Path | None = typer.Argument(
        None,
        help="Optional path to a file or directory",
    ),
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output",
    ),
):
    if verbose:
        typer.echo("Verbose mode enabled")

    if path is not None:
        # ✅ This is the key behavior you asked for
        typer.echo(f"Path: {path}")
    else:
        typer.echo("No path provided")


if __name__ == "__main__":
    app()