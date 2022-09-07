from pathlib import Path

import typer
from rich.console import Console

from incydr import Client
from incydr._core.settings import LogLevel

console = Console()


def init_incydr_client(
    ctx: typer.Context,
    log_level: LogLevel = typer.Option(
        help="Set level for Incydr client logging.", default="WARNING"
    ),
    log_file: Path = typer.Option(
        help="Specify file path to write log output to.", default=None
    ),
):
    log_stderr = not log_file
    ctx.obj = lambda: Client(
        log_level=log_level, log_file=log_file, log_stderr=log_stderr
    )
