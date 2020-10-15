# Copyright 2015, Aiven, https://aiven.io/
#
# This file is under the Apache License, Version 2.0.
# See the file `LICENSE` for details.

from .argx import arg
from functools import wraps

import json as jsonlib
import os


def get_json_config(path_or_string):
    if path_or_string.startswith("@"):
        filepath = path_or_string[1:]
        with open(filepath, "r") as config_file:
            return jsonlib.load(config_file)

    return jsonlib.loads(path_or_string)


def json_path_or_string(param_name):
    def wrapper(fun):
        arg(
            param_name,
            help="JSON string or path (preceded by '@') to a JSON configuration file",
        )(fun)

        @wraps(fun)
        def wrapped(self):
            setattr(
                self.args,
                param_name,
                get_json_config(getattr(self.args, param_name, "")),
            )
            return fun(self)

        return wrapped

    return wrapper


arg.account_id = arg("account_id", help="Account identifier")
arg.authentication_id = arg("authentication_id", help="Account authentication method identifier")
arg.billing_address = arg("--billing-address", help="Physical billing address for invoices")
arg.billing_currency = arg("--billing-currency", help="Currency for charges")
arg.billing_extra_text = arg(
    "--billing-extra-text",
    help="Extra text to include in invoices (e.g. cost center id)",
)
arg.card_id = arg("--card-id", help="Card ID")
arg.cloud = arg("--cloud", help="Cloud to use (see 'cloud list' command)")
arg.config_cmdline = arg(
    "-c",
    dest="config_cmdline",
    metavar="KEY=VALUE",
    action="append",
    default=[],
    help="Additional configuration option in the form name=value",
)
arg.config_file = arg(
    "-f",
    dest="config_file",
    metavar="KEY=VALUE",
    action="append",
    default=[],
    help="Additional configuration option whose value is loaded from file in the form name=filename",
)
arg.country_code = arg("--country-code", help="Billing country code")
arg.email = arg("email", help="User email address")
arg.force = arg(
    "-f",
    "--force",
    help="Force action without interactive confirmation",
    action="store_true",
    default=False,
)
arg.index_name = arg("index_name", help="Index name")
arg.json = arg("--json", help="Raw json output", action="store_true", default=False)
arg.min_insync_replicas = arg(
    "--min-insync-replicas",
    type=int,
    help="Minimum required nodes In Sync Replicas (ISR) to produce to a partition (default: 1)",
)
arg.partitions = arg("--partitions", type=int, required=True, help="Number of partitions")
arg.project = arg(
    "--project",
    help="Project name to use, default %(default)r",
    default=os.environ.get("AIVEN_PROJECT"),
)
arg.replication = arg("--replication", type=int, required=True, help="Replication factor")
arg.retention = arg("--retention", type=int, help="Retention period in hours (default: unlimited)")
arg.retention_bytes = arg("--retention-bytes", type=int, help="Retention limit in bytes (default: unlimited)")
arg.service_name = arg("name", help="Service name")
arg.service_type = arg("-t", "--service-type", help="Type of service (see 'service list-types')")
arg.team_name = arg("--team-name", help="Team name", required=True)
arg.team_id = arg("--team-id", help="Team identifier", required=True)
arg.timeout = arg("--timeout", type=int, help="Wait for up to N seconds (default: infinite)")
arg.topic = arg("topic", help="Topic name")
arg.user_config = arg(
    "-c",
    dest="user_config",
    metavar="KEY=VALUE",
    action="append",
    default=[],
    help="Apply a configuration setting. See 'avn service types -v' for available values.",
)
arg.user_id = arg("--user-id", help="User identifier", required=True)
arg.user_option_remove = arg(
    "--remove-option",
    dest="user_option_remove",
    action="append",
    default=[],
    help="Remove a configuration setting. See 'avn service types -v' for available settings.",
)
arg.vat_id = arg("--vat-id", help="VAT ID of an EU VAT area business")
arg.verbose = arg("-v", "--verbose", help="Verbose output", action="store_true", default=False)
arg.connector_name = arg("connector", help="Connector name")
arg.json_path_or_string = json_path_or_string
arg.subject = arg("--subject", required=True, help="Subject name")
arg.version_id = arg("--version-id", required=True, help="Subject version")
arg.compatibility = arg(
    "--compatibility",
    required=True,
    choices=["BACKWARD", "FORWARD", "FULL", "NONE"],
    help="Choose a compatibility level for the subject",
)
arg.schema = arg("--schema", required=True, help="Schema string quote escaped")

arg.source_cluster = arg("-s", "--source-cluster", required=True, help="Source cluster alias")
arg.target_cluster = arg("-t", "--target-cluster", required=True, help="Target cluster alias")
