#!/usr/bin/env python

import click
from . import utils
from . import remote
import pandas as pd

@click.group()
def cli():
    pass


@cli.command()
@click.option('--raw', is_flag=True, help="Present raw results?")
def me(raw=False):
    """Show my account's info """
    data = remote.api.get("/me")

    if raw:
        click.echo(utils.to_json(data))
        return

    df = pd.DataFrame([data])
    df.columns = [col.replace("_", " ").title() for col in df.columns]
    click.echo(utils.to_table(df.T, showindex=True, showheaders=False))

