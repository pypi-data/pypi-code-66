import json

import click

from jatime import __version__
from jatime.analyzer import analyze
from jatime.server import app


@click.group()
@click.version_option(__version__)
def cli():
    pass


@cli.command(name="analyze", help="Analyze Japanese time expressions from the string.")
@click.option("--format-json", is_flag=True, help="Output in json format.")
@click.argument("string")
def _analyze(format_json: bool, string: str) -> None:
    result = analyze(string)
    if format_json:
        click.echo(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        click.echo(result)


@cli.command(help="Start an HTTP server.")
@click.option("--host", default="localhost", show_default=True)
@click.option("--port", type=int, default=1729, show_default=True)
def serve(host: str, port: int):
    app.run(host=host, port=port)
