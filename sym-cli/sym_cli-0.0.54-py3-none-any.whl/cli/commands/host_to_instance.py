from json import dumps

import click

from ..decorators import loses_interactivity, require_login
from ..errors import InstanceNotFound
from ..helpers import boto, threading
from ..helpers.global_options import GlobalOptions
from ..helpers.options import resource_argument
from .sym import sym


@sym.command(short_help="Get an Instance ID for a host")
@click.option("--json", is_flag=True, hidden=True)
@click.option("--find-region", is_flag=True, hidden=True)
@resource_argument
@click.argument("host")
@click.make_pass_decorator(GlobalOptions)
@loses_interactivity
@require_login
def host_to_instance(
    options: GlobalOptions,
    resource: str,
    host: str,
    json: bool,
    find_region: bool,
) -> None:
    client = options.create_saml_client(resource)

    if find_region:
        [region, instance] = boto.search_for_host(client, host)
    else:
        instance = boto.host_to_instance(client, host)
        region = boto.get_region(client)

    if json:
        click.echo(dumps({"instance": instance, "region": region}))
    else:
        click.echo(instance)
