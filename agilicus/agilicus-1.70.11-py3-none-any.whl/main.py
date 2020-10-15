import json
import sys
from datetime import date, datetime, timezone
from urllib.parse import urlparse

import click
import jwt
from click_shell import shell
from prettytable import PrettyTable

from . import (
    apps,
    audits,
    challenges,
    context,
    credentials,
    catalogues,
    csv_rules,
    env_config,
    files,
    gateway,
    input_helpers,
    issuers,
    logs,
    messages,
    metrics,
    orgs,
    permissions,
    scopes,
    tokens,
    users,
    whoami,
)

from .version import __version__


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def prompt(ctx):
    issuer_host = urlparse(context.get_issuer(ctx)).netloc
    org = context.get_org(ctx)
    if not org:
        return f"{issuer_host}$ "
    return f"{issuer_host}/{org['organisation']}$ "


def app_completion(ctx, args, incomplete):
    context.setup(ctx)
    _apps = apps.query(ctx, None)
    results = []
    for _app in _apps:
        if incomplete in _app["name"]:
            results.append(_app["name"])
    return results


def env_completion(ctx, args, incomplete):
    context.setup(ctx)
    _envs = apps.env_query(ctx, None, args.pop())
    results = []
    for _env in _envs:
        if incomplete in _env["name"]:
            results.append(_env["name"])
    return results


def user_completion(ctx, args, incomplete):
    context.setup(ctx)
    _users = users.query(ctx)["users"]
    results = []
    for _user in _users:
        if incomplete in _user["email"]:
            results.append(_user["email"])
    return results


def sub_org_completion(ctx, args, incomplete):
    context.setup(ctx)
    suborgs = orgs.query_suborgs(ctx)
    results = []
    for suborg in suborgs:
        if incomplete in suborg["organisation"]:
            results.append(suborg["organisation"])
    return results


def get_user_id(ctx, id, org_id=None):
    return json.loads(users.get_user(ctx, user_id=id, org_id=org_id))


def get_user_id_from_email(ctx, email, org_id=None):
    _users = users.query(ctx, email=email, org_id=org_id)["users"]
    if len(_users) == 1:
        return _users[0]
    return {}


def get_user_from_email_or_id(ctx, user_id_or_email=None, org_id=None, **kwargs):
    """If an email address, tries to map that to a user id. If that fails,
    assumes the input is a user id
    """
    to_check = input_helpers.get_user_id_from_input_or_ctx(ctx, user_id=user_id_or_email)
    _user = None
    if "@" in to_check:
        _user = get_user_id_from_email(ctx, email=to_check, org_id=org_id)
    if not _user:
        _user = users.get_user_obj(ctx, to_check, org_id=org_id)

    return _user


def user_id_or_id_from_email(ctx, user_id_or_email=None, org_id=None, **kwargs):
    _user = get_user_from_email_or_id(ctx, user_id_or_email, org_id)
    if not _user:
        return None

    return _user["id"]


def get_org_id_by_name_or_use_given(org_by_name, org_id=None, org_name=None):
    if not org_id and org_name:
        if org_name in org_by_name:
            org_id = org_by_name[org_name]["id"]
        else:
            raise Exception("No such organisation found: {}".format(org_name))

    return org_id


def get_org_id(ctx, org_name=None, org_id=None):
    _, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)
    return get_org_id_by_name_or_use_given(org_by_name, org_id=org_id, org_name=org_name)


# @click.group()
@shell(prompt=prompt)
@click.option("--token", default=None)
@click.option("--api", default=context.API_DEFAULT)
@click.option("--cacert", default=context.CACERT_DEFAULT)
@click.option("--client_id", default=context.CLIENT_ID_DEFAULT)
@click.option("--issuer", default=context.ISSUER_DEFAULT)
@click.option("--auth_local_webserver/--noauth_local_webserver", default=True)
@click.option("--org_id", default=context.ORG_ID_DEFAULT)
@click.option("--header", default=context.HEADER_DEFAULT, type=bool)
@click.option("--scope", default=scopes.get_default_scopes(), multiple=True)
@click.option("--admin", is_flag=True)
@click.option("--output_format", default="console", type=str)
@click.pass_context
def cli(
    ctx,
    token,
    api,
    cacert,
    client_id,
    issuer,
    auth_local_webserver,
    org_id,
    header,
    scope,
    admin,
    output_format,
):
    ctx.ensure_object(dict)
    ctx.obj["TOKEN"] = token
    ctx.obj["API"] = api
    ctx.obj["CACERT"] = cacert
    ctx.obj["CLIENT_ID"] = client_id
    ctx.obj["ISSUER"] = issuer
    ctx.obj["AUTH_LOCAL_WEBSERVER"] = auth_local_webserver
    ctx.obj["ORG_ID"] = org_id
    ctx.obj["HEADER"] = header
    ctx.obj["SCOPES"] = list(scope)
    ctx.obj["ADMIN_MODE"] = admin
    ctx.obj["output_format"] = output_format
    if admin:
        # Extend the provided scopes (either default or chosen by user) with the admin
        # ones.
        ctx.obj["SCOPES"].extend(scopes.get_admin_scopes())
    context.save(ctx)

    token = whoami.whoami(ctx, False)
    org_id = context.get_org_id(ctx, token)
    if org_id:
        org = orgs.get(ctx, org_id)
        ctx.obj["ORGANISATION"] = org
    return None


@cli.command(name="use-org")
@click.pass_context
@click.argument("organisation", default=None, autocompletion=sub_org_completion)
def use_org(ctx, organisation):
    org_list = orgs.query_suborgs(ctx, organisation=organisation)
    found_org = None
    for _org in org_list:
        if _org["organisation"] == organisation:
            found_org = _org

    if not found_org:
        print(f"No sub organisation found named {organisation}")
        return

    org_id = found_org["id"]
    ctx.obj["ORG_ID"] = org_id

    token = whoami.whoami(ctx, False)
    if token:
        ctx.obj["ORGANISATION"] = found_org
    context.save(ctx)


def jsonify(ctx, entry):
    if isinstance(entry, list):
        result = []
        for n in entry:
            result.append(jsonify(ctx, n))
        return result
    else:
        if "updated" in entry and isinstance(entry["updated"], datetime):
            entry["updated"] = entry["updated"].isoformat()
        if "created" in entry and isinstance(entry["created"], datetime):
            entry["created"] = entry["created"].isoformat()
        return entry


def output_json(ctx, entry):
    print(json.dumps(jsonify(ctx, entry), sort_keys=True, indent=2))


def output_tokens_list(ctx, tokens_list):
    if ctx.obj["output_format"] == json:
        return output_json(ctx, tokens_list)
    table = PrettyTable(
        [
            "jti",
            "roles",
            "iat",
            "exp",
            "aud",
            "user",
            "session",
            "revoked",
            "scopes",
            "updated",
        ]
    )
    for token in tokens_list:
        table.add_row(
            [
                token["jti"],
                json.dumps(token["roles"], indent=2),
                token["iat"],
                token["exp"],
                json.dumps(token["aud"], indent=2),
                token["sub"],
                token["session"],
                token["revoked"],
                json.dumps(token["scopes"], indent=2),
                token["updated"],
            ]
        )
    table.align = "l"
    print(table)


@cli.command(name="delete-credentials")
@click.pass_context
def _delete_credentials(ctx, **kwargs):
    credentials.delete_credentials_with_ctx(ctx)


@cli.command(name="list-tokens")
@click.option("--limit", default=None)
@click.option("--expired-from", default=None)
@click.option("--expired-to", default=None)
@click.option("--issued-from", default=None)
@click.option("--issued-to", default=None)
@click.option("--org_id", default=None)
@click.option("--jti", default=None)
@click.option("--sub", default=None)
@click.pass_context
def list_tokens(ctx, org_id, **kwargs):
    output_tokens_list(
        ctx, json.loads(tokens.query_tokens(ctx, org_id=org_id, **kwargs))["tokens"]
    )


@cli.command(name="get-token")
@click.argument("user_id", default=None)
@click.option("--duration", default=3600, prompt=True)
@click.option(
    "--hosts",
    default='[{"upstream_host": "example.com", "allowed_list": [{"methods" : ["get"], "paths" : ["/.*"]}]}]',  # noqa
    prompt=True,
)
@click.pass_context
def token_get(ctx, user_id, duration, hosts, **kwargs):
    user = json.loads(users.get_user(ctx, user_id))
    token = tokens.get_token(ctx, user_id, user["org_id"], duration, hosts, **kwargs)
    output_entry(ctx, jwt.decode(token, verify=False))
    print(token)


def output_gw_audit_list(ctx, audit_list):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, audit_list)
    table = PrettyTable(["time", "authority", "token_id"])
    for entry in audit_list:
        table.add_row([entry["time"], entry["authority"], entry["token_id"]])
    table.align = "l"
    print(table)


@cli.command(name="gateway-audit")
@click.option("--limit", default=None)
@click.option("--token-id", default=None)
def gateway_audit(ctx, **kwargs):
    output_gw_audit_list(ctx, json.loads(gateway.query_audit(**kwargs)))


@cli.command(name="list-audit-records")
@click.option("--limit", type=int, default=50)
@click.option("--org_id", default=None)
@click.option("--dt_from", default=None)
@click.option("--dt_to", default=None)
@click.option("--user_id", default=None)
@click.option("--action", default=None)
@click.option("--target_id", default=None)
@click.option("--token_id", default=None)
@click.option("--api_name", default=None)
@click.option("--target_resource_type", default=None)
@click.option("--output_format", type=click.Choice(["json"]), default=None)
@click.pass_context
def list_audit_records(ctx, **kwargs):
    output_format = kwargs.pop("output_format", "")
    records = audits.query(ctx, **kwargs)
    if output_format == "json":
        records = [record.to_dict() for record in records]
        print(json.dumps(records, default=str))
    else:
        print(audits.format_audit_list_as_text(records))


@cli.command(name="list-auth-audit-records")
@click.option("--limit", type=int, default=50)
@click.option("--org_id", default=None)
@click.option("--dt_from", default=None)
@click.option("--dt_to", default=None)
@click.option("--user_id", default=None)
@click.option("--event", default=None)
@click.option("--session_id", default=None)
@click.option("--trace_id", default=None)
@click.option("--upstream_user_id", default=None)
@click.option("--upstream_idp", default=None)
@click.option("--login_org_id", default=None)
@click.option("--source_ip", default=None)
@click.option("--client_id", default=None)
@click.option("--event", default=None)
@click.option("--stage", default=None)
@click.pass_context
def list_auth_audit_records(ctx, **kwargs):
    records = audits.query_auth_audits(ctx, **kwargs)
    print(audits.format_auth_audit_list_as_text(records))


def output_list_users(ctx, orgs_by_id, users_list):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, users_list)
    table = PrettyTable(
        [
            "id",
            "First Name",
            "Last Name",
            "Email",
            "External_ID",
            "Organisation",
            "Status",
        ]
    )
    for entry in users_list:
        org_name = "none"

        org_id = entry.get("org_id", None)
        if org_id and org_id in orgs_by_id:
            org_name = orgs_by_id[entry["org_id"]]["organisation"]

        table.add_row(
            [
                entry["id"],
                entry["first_name"],
                entry.get("last_name", ""),
                entry["email"],
                entry.get("external_id", ""),
                org_name,
                entry.get("status", ""),
            ]
        )
    table.align = "l"
    print(table)


@cli.command(name="list-users")
@click.option("--organisation", default=None)
@click.option("--org_id", default=None)
@click.option("--email", default=None)
@click.option("--previous_email", default=None)
@click.option("--limit", type=int, default=None)
@click.option(
    "--status", multiple=True, type=click.Choice(users.STATUS_OPTIONS), default=None
)
@click.option(
    "--search_direction",
    default=None,
    type=click.Choice(["forwards", "backwards"]),
)
@click.option("--has_roles", type=bool, default=None)
@click.pass_context
def list_users(ctx, organisation, org_id, **kwargs):
    # get all orgs
    org_by_id, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)
    org_id = get_org_id_by_name_or_use_given(
        org_by_name, org_name=organisation, org_id=org_id
    )

    output_list_users(ctx, org_by_id, users.query(ctx, org_id, **kwargs)["users"])


def output_entry(ctx, entry):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, entry)
    table = PrettyTable(["field", "value"])
    for k, v in list(entry.items()):
        if k == "nbf" or k == "exp" or k == "iat":
            _t = datetime.fromtimestamp(v, timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S %z (%Z)"
            )  # noqa
            table.add_row([k, json.dumps(_t, indent=4)])
        elif k == "created" or k == "updated":
            table.add_row([k, v])
        else:
            table.add_row([k, json.dumps(v, indent=4, default=str)])
    table.align = "l"
    print(table)


@cli.command(name="show-user")
@click.argument("email", autocompletion=user_completion)
@click.option("--org_id", default=None)
@click.pass_context
def show_user(ctx, email, org_id):
    _user = get_user_id_from_email(ctx, email=email, org_id=org_id)
    if not _user:
        _user = get_user_id(ctx, id=email, org_id=org_id)
    if _user:
        output_entry(ctx, _user)


@cli.command(name="add-user")
@click.argument("first-name")
@click.argument("last_name")
@click.argument("email")
@click.argument("org_id")
@click.option("--external-id", default=None)
@click.option("--enabled", type=bool, default=None)
@click.option("--status", type=click.Choice(users.STATUS_OPTIONS), default=None)
@click.pass_context
def add_user(ctx, first_name, last_name, email, org_id, **kwargs):
    output_entry(
        ctx, users.add_user(ctx, first_name, last_name, email, org_id, **kwargs)
    )


@cli.command(name="update-user")
@click.argument("email", autocompletion=user_completion)
@click.option("--org_id", default=None)
@click.option("--email", default=None)
@click.option("--first-name", default=None)
@click.option("--last-name", default=None)
@click.option("--external-id", default=None)
@click.option("--auto_created", type=bool, default=None)
@click.option("--enabled", type=bool, default=None)
@click.option("--status", type=click.Choice(users.STATUS_OPTIONS), default=None)
@click.pass_context
def update_user(ctx, email, org_id, **kwargs):
    _user = get_user_id_from_email(ctx, email, org_id)
    if _user:
        output_entry(
            ctx, users.update_user(ctx, user_id=_user["id"], org_id=org_id, **kwargs)
        )


@cli.command(name="delete-user")
@click.argument("email", autocompletion=user_completion)
@click.pass_context
def delete_user(ctx, email):
    _user = get_user_id_from_email(ctx, email)
    if _user:
        users.delete_user(ctx, _user["id"])


@cli.command(name="add-user-role")
@click.argument("email", autocompletion=user_completion)
@click.argument("application", autocompletion=app_completion)
@click.option("--role", multiple=True)
@click.option("--org_id", default=None)
@click.pass_context
def add_user_role(ctx, email, application, role, org_id):
    _user = get_user_from_email_or_id(ctx, email, org_id=org_id)
    if _user:
        roles = []
        for _role in role:
            roles.append(_role)
        users.add_user_role(ctx, _user["id"], application, roles, org_id=org_id)
        output_entry(
            ctx,
            json.loads(
                users.get_user(ctx, _user["id"], org_id=org_id, type=_user["type"])
            ),
        )


@cli.command(name="list-user-roles")
@click.argument("email", autocompletion=user_completion)
@click.option("--org_id", default=None)
@click.pass_context
def list_user_role(ctx, email, org_id):
    _user = get_user_id_from_email(ctx, email, org_id)
    if _user:
        roles = json.loads(users.list_user_roles(ctx, _user["id"], org_id))
        table = PrettyTable(["application/service", "roles"])
        table.align = "l"
        for app, rolelist in roles.items():
            table.add_row([app, rolelist])
        print(table)


def output_list_orgs(ctx, orgs_list):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, orgs_list)
    table = PrettyTable(["id", "Organisation", "issuer", "subdomain"])
    for entry in orgs_list:
        subdomain = entry.get("subdomain", None)
        if "subdomain" not in entry:
            subdomain = None
        table.add_row([entry["id"], entry["organisation"], entry["issuer"], subdomain])
    table.align = "l"
    print(table)


def output_list_groups(ctx, orgs_by_id, groups_list):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, groups_list)
    table = PrettyTable(["id", "Email", "members"])
    for entry in groups_list:
        _members = []
        for _member in entry["member_of"]:
            _members.append(_member["email"])
        table.add_row(
            [
                entry["id"],
                entry["email"],
                "\n".join(_members),
            ]
        )
    table.align = "l"
    print(table)


@cli.command(name="list-groups")
@click.option("--organisation", default=None)
@click.option("--org_id", default=None)
@click.option("--type", multiple=True, default=["group"])
@click.option("--limit", default=500)
@click.option("--previous_email", default=None)
@click.option(
    "--search_direction",
    default="forwards",
    type=click.Choice(["forwards", "backwards"]),
)
@click.pass_context
def list_groups(ctx, organisation, org_id, type, **kwargs):
    # get all orgs
    org_by_id, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)

    org_id = get_org_id_by_name_or_use_given(
        org_by_name, org_name=organisation, org_id=org_id
    )
    users_groups = users.query(ctx, org_id, type=type, **kwargs)
    output_list_groups(ctx, org_by_id, users_groups["users"])


@cli.command(name="list-sysgroups")
@click.option("--organisation", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def list_sysgroups(ctx, organisation, org_id, **kwargs):
    # get all orgs
    org_by_id, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)
    org_id = get_org_id_by_name_or_use_given(
        org_by_name, org_name=organisation, org_id=org_id
    )
    users_groups = users.query(ctx, org_id, type="sysgroup", **kwargs)
    output_list_groups(ctx, org_by_id, users_groups["users"])


@cli.command(name="add-group")
@click.argument("first-name")
@click.option("--org_id")
@click.pass_context
def add_group(ctx, first_name, org_id):
    output_entry(ctx, users.add_group(ctx, first_name, org_id))


@cli.command(name="add-group-member")
@click.argument("group_id", default=None)
@click.option("--org_id", default=None)
@click.option("--member_org_id", default=None)
@click.option("--member", multiple=True)
@click.pass_context
def add_group_member(ctx, group_id, org_id, member, member_org_id):
    users.add_group_member(ctx, group_id, member, org_id, member_org_id)


@cli.command(name="delete-group-member")
@click.argument("group_id", default=None)
@click.option("--member", multiple=True)
@click.option("--org_id", default=None)
@click.pass_context
def delete_group_member(ctx, group_id, org_id, member):
    users.delete_group_member(ctx, group_id, member, org_id)


@cli.command(name="delete-group")
@click.argument("group_id", default=None)
@click.pass_context
def delete_group(ctx, group_id):
    users.delete_user(ctx, group_id, type="group")


@cli.command(name="list-orgs")
@click.option("--org_id", default=None)
@click.option("--issuer", default=None)
@click.pass_context
def list_orgs(ctx, **kwargs):
    output_list_orgs(ctx, orgs.query(ctx, **kwargs))


@cli.command(name="list-sub-orgs")
@click.option("--org_id", default=None)
@click.pass_context
def list_sub_orgs(ctx, **kwargs):
    output_list_orgs(ctx, orgs.query_suborgs(ctx, **kwargs))


@cli.command(name="show-org")
@click.argument("org_id", default=None)
@click.pass_context
def show_org(ctx, org_id, **kwargs):
    output_entry(ctx, orgs.get(ctx, org_id, **kwargs))


@cli.command(name="update-org")
@click.argument("org_id", default=None)
@click.option("--auto_create", type=bool, default=None)
@click.option("--issuer", default=None)
@click.option("--issuer_id", default=None)
@click.option("--contact_id", default=None)
@click.option("--subdomain", default=None)
@click.option("--external_id", default=None)
@click.option("--trust_on_first_use_duration", type=int, default=None)
@click.pass_context
def update_org(
    ctx,
    org_id,
    auto_create,
    issuer,
    issuer_id,
    contact_id,
    subdomain,
    external_id,
    **kwargs,
):
    orgs.update(
        ctx,
        org_id,
        auto_create=auto_create,
        issuer=issuer,
        issuer_id=issuer_id,
        contact_id=contact_id,
        subdomain=subdomain,
        external_id=external_id,
        **kwargs,
    )
    output_entry(ctx, orgs.get(ctx, org_id))


@cli.command(name="set-feature")
@click.argument("feature")
@click.argument("enabled", type=bool)
@click.option("--org_id", default=None)
@click.pass_context
def set_feature(ctx, feature, enabled, org_id, **kwargs):
    result = orgs.set_feature(
        ctx, feature=feature, enabled=enabled, org_id=org_id, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="remove-feature")
@click.argument("feature")
@click.option("--org_id", default=None)
@click.pass_context
def remove_feature(ctx, feature, org_id, **kwargs):
    result = orgs.remove_feature(ctx, feature=feature, org_id=org_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="add-org")
@click.argument("organisation")
@click.argument("issuer")
@click.option("--issuer_id", default=None)
@click.option("--auto_create", type=bool, default=True)
@click.option("--contact_id", default=None)
@click.option("--subdomain", default=None)
@click.pass_context
def add_org(
    ctx, organisation, issuer, issuer_id, contact_id, auto_create, subdomain, **kwargs
):
    output_entry(
        ctx,
        orgs.add(
            ctx,
            organisation,
            issuer,
            issuer_id,
            contact_id,
            auto_create,
            subdomain=subdomain,
            **kwargs,
        ),
    )


@cli.command(name="add-sub-org")
@click.argument("organisation")
@click.option("--auto_create", type=bool, default=True)
@click.option("--contact_id", default=None)
@click.option("--subdomain", default=None)
@click.pass_context
def add_sub_org(ctx, organisation, contact_id, auto_create, subdomain, **kwargs):
    output_entry(
        ctx,
        orgs.add_suborg(ctx, organisation, contact_id, auto_create, subdomain, **kwargs),
    )


@cli.command(name="delete-sub-org")
@click.argument("org_id")
@click.pass_context
def delete_sub_org(ctx, org_id):
    orgs.delete_suborg(ctx, org_id)


@cli.command(name="delete-org")
@click.argument("org_id", default=None)
@click.pass_context
def delete_org(ctx, org_id, **kwargs):
    orgs.delete(ctx, org_id, **kwargs)


def output_list_apps(ctx, orgs_by_id, apps_list):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, apps_list)
    table = PrettyTable(["id", "Application", "Organisation"])
    for entry in apps_list:

        org_name = "none"
        org_id = entry.get("org_id", None)
        if org_id and org_id in orgs_by_id:
            org_name = orgs_by_id[org_id]["organisation"]

        table.add_row([entry["id"], entry["name"], org_name])
    table.align = "l"
    print(table)


@cli.command(name="list-applications")
@click.option("--organisation", default=None)
@click.option("--org_id", default=None)
@click.option("--updated_since", default=None)
@click.pass_context
def list_applications(ctx, organisation, org_id, **kwargs):
    # get all orgs
    org_by_id, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)
    org_id = get_org_id_by_name_or_use_given(
        org_by_name, org_name=organisation, org_id=org_id
    )

    output_list_apps(ctx, org_by_id, apps.query(ctx, org_id, **kwargs))


@cli.command(name="list-environments")
@click.argument("application", autocompletion=app_completion)
@click.option("--organisation", default=None)
@click.option("--org_id", default=None)
@click.option("--filter", default=None)
@click.pass_context
def list_environments(ctx, organisation, org_id, filter, **kwargs):
    org_by_id, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)
    if not org_id and organisation:
        if organisation in org_by_name:
            org_id = org_by_name[organisation]["id"]
        else:
            Exception("No such organisation found: {}".format(organisation))
    data = []
    table = PrettyTable(
        ["Name", "Assignments", "Services"],
        header=context.header(ctx),
        border=context.header(ctx),
    )
    for env in apps.env_query(ctx, org_id, **kwargs):
        _services = []
        for service in env.get("application_services", []):
            _services.append(service["name"])
        data.append(env)
        table.add_row([env["name"], env.get("assignments", None), _services])
    table.align = "l"
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, data)
    if filter:
        print(table.get_string(fields=filter.split(",")))
    else:
        print(table)


@cli.command(name="list-application-services")
@click.option("--org_id", default=None)
@click.pass_context
def list_application_services(ctx, **kwargs):
    table = PrettyTable(
        [
            "id",
            "name",
            "hostname",
            "ipv4_addresses",
            "name_resolution",
            "port",
            "protocol",
        ]
    )
    services = apps.get_application_services(ctx, **kwargs)
    for obj in services:
        service = obj.to_dict()
        table.add_row(
            [
                service["id"],
                service["name"],
                service["hostname"],
                service["ipv4_addresses"],
                service["name_resolution"],
                service["port"],
                service["protocol"],
            ]
        )
    table.align = "l"
    print(table)


@cli.command(name="add-application-service")
@click.argument("name", default=None)
@click.argument("hostname", default=None)
@click.argument("port", type=int, default=None)
@click.option("--org_id", default=None)
@click.option("--ipv4_addresses", default=None)
@click.option("--name_resolution", default=None)
@click.option("--protocol", default=None)
@click.pass_context
def add_application_service(ctx, name, hostname, port, org_id, **kwargs):
    output_entry(
        ctx,
        apps.add_application_service(
            ctx, name, hostname, port, org_id=org_id, **kwargs
        ).to_dict(),
    )


@cli.command(name="update-application-service")
@click.argument("id", default=None)
@click.option("--name", default=None)
@click.option("--hostname", default=None)
@click.option("--port", type=int, default=None)
@click.option("--org_id", default=None)
@click.option("--ipv4_addresses", default=None)
@click.option("--name_resolution", default=None)
@click.option("--protocol", default=None)
@click.pass_context
def update_application_service(ctx, id, **kwargs):
    output_entry(ctx, (apps.update_application_service(ctx, id, **kwargs)))


@cli.command(name="add-application-service-assignment")
@click.argument("app_service_name", default=None)
@click.argument("app", default=None)
@click.argument("environment_name", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def add_application_service_assignment(ctx, **kwargs):
    output_entry(ctx, apps.add_application_service_assignment(ctx, **kwargs))


@cli.command(name="delete-application-service-assignment")
@click.argument("app_service_name", default=None)
@click.argument("app", default=None)
@click.argument("environment_name", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_application_service_assignment(ctx, **kwargs):
    apps.delete_application_service_assignment(ctx, **kwargs)


@cli.command(name="show-application-service")
@click.argument("id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def show_application_service(ctx, id, org_id, **kwargs):
    output_entry(
        ctx, apps.get_application_service(ctx, id, org_id=org_id, **kwargs).to_dict()
    )


@cli.command(name="delete-application-service")
@click.argument("name", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_application_service(ctx, name, org_id, **kwargs):
    print(apps.delete_application_service(ctx, name, org_id=org_id, **kwargs))


def output_environment_entries(ctx, entry):
    if ctx.obj["output_format"] == "json":
        return output_json(ctx, entry)
    table = PrettyTable(["field", "value"])
    for k, v in list(entry.items()):
        table.add_row([k, v])
    table.align = "l"
    print(table)


@cli.command(name="show-environment")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.pass_context
def show_environment(ctx, application, env_name, org_id, **kwargs):
    output_environment_entries(
        ctx, apps.get_env(ctx, application, env_name, org_id, **kwargs)
    )


@cli.command(name="delete-environment")
@click.argument("app", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.pass_context
def delete_environment(ctx, app, **kwargs):
    _app = _get_app(ctx, app, **kwargs)
    if _app:
        _env = [env for env in _app["environments"] if env["name"] == kwargs["env_name"]]
        if click.confirm(
            "Do you want to delete this environment?:\n"
            f"{json.dumps(_env, indent=4, sort_keys=True)}"
        ):
            resp = apps.delete_environment(ctx, app_id=_app["id"], **kwargs)
            click.echo(resp)
    else:
        click.echo(f"app {app} not found")


@cli.command(name="update-environment")
@click.argument("app", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.option("--version_tag", default=None)
@click.option("--serverless_image", default=None)
@click.option("--config_mount_path", default=None)
@click.option("--config_as_mount", help="json string", default=None)
@click.option("--config_as_env", help="json string", default=None)
@click.option("--secrets_mount_path", default=None)
@click.option("--secrets_as_mount", default=None)
@click.option("--secrets_as_env", default=None)
@click.pass_context
def update_environment(
    ctx,
    app,
    env_name,
    org_id,
    version_tag,
    config_mount_path,
    config_as_mount,
    config_as_env,
    secrets_mount_path,
    secrets_as_mount,
    secrets_as_env,
    **kwargs,
):
    _app = _get_app(ctx, app, org_id=org_id)
    if _app:
        apps.update_env(
            ctx,
            _app["id"],
            env_name,
            org_id,
            version_tag,
            config_mount_path,
            config_as_mount,
            config_as_env,
            secrets_mount_path,
            secrets_as_mount,
            secrets_as_env,
            **kwargs,
        )


@cli.command(name="set-env-runtime-status")
@click.argument("app", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.option("--overall_status", default=None)
@click.option("--running_replicas", default=None)
@click.option("--error_message", default=None)
@click.option("--restarts", help="json string", default=None)
@click.option("--cpu", help="json string", default=None)
@click.option("--memory", default=None)
@click.option("--running_image", default=None)
@click.option("--running_hash", default=None)
@click.pass_context
def update_environment_status(
    ctx,
    app,
    env_name,
    org_id,
    **kwargs,
):
    _app = _get_app(ctx, app, org_id=org_id)
    _env = [env for env in _app["environments"] if env["name"] == env_name][0]
    if _app:
        status = apps.update_env_runtime_status(
            ctx,
            _app["id"],
            env_name,
            _env["maintenance_org_id"],
            **kwargs,
        )
        click.echo(status)


@cli.command(name="get-env-status")
@click.argument("app", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.option("--organisation", default=None)
@click.pass_context
def get_environment_status(
    ctx,
    app,
    env_name,
    org_id,
    organisation,
    **kwargs,
):
    org_id = get_org_id(ctx, org_name=organisation, org_id=org_id)
    _app = _get_app(ctx, app, org_id=org_id)
    _env = [env for env in _app["environments"] if env["name"] == env_name][0]
    output_entry(ctx, _env["status"])


@cli.command(name="delete-application")
@click.argument("app", autocompletion=app_completion)
@click.option("--org_id", default=None)
@click.pass_context
def delete_application(ctx, app, **kwargs):
    _app = _get_app(ctx, app, **kwargs)
    if _app:
        if click.confirm(
            "Do you want to delete this app?:"
            f"\n{json.dumps(_app, indent=4, sort_keys=True)}"
        ):
            kwargs.setdefault(_app["org_id"])
            resp = apps.delete(ctx, _app["id"], **kwargs)
            click.echo(resp)


@cli.command(name="add-application")
@click.argument("name")
@click.argument("org_id")
@click.argument("category")
@click.option("--published", type=click.Choice(["no", "public"]), default=None)
@click.option("--default_role_id", default=None)
@click.option("--icon_url", default=None)
@click.option("--location", type=click.Choice(["hosted", "external"]), default=None)
@click.pass_context
def add_application(ctx, name, org_id, category, **kwargs):
    output_entry(ctx, json.loads(apps.add(ctx, name, org_id, category, **kwargs)))


@cli.command(name="assign-application")
@click.argument("env_name")
@click.argument("app_id")
@click.argument("org_id")
@click.argument("assigned_org_id")
@click.option("--admin-org-id", default=None)
@click.pass_context
def assign_application(ctx, env_name, app_id, org_id, assigned_org_id, admin_org_id):
    output_entry(
        ctx,
        json.loads(
            apps.update_assignment(
                ctx,
                env_name,
                app_id,
                org_id,
                assigned_org_id,
                admin_org_id=admin_org_id,
            )
        ),
    )


@cli.command(name="unassign-application")
@click.argument("env_name")
@click.argument("app_id")
@click.argument("org_id")
@click.argument("assigned_org_id")
@click.pass_context
def unassign_application(ctx, env_name, app_id, org_id, assigned_org_id):
    output_entry(
        ctx,
        json.loads(
            apps.update_assignment(
                ctx, env_name, app_id, org_id, assigned_org_id, unassign=True
            )
        ),
    )


def _get_app(ctx, app, app_id=None, org_id=None, **kwargs):
    _app = apps.get_app(ctx, org_id, app)
    if _app:
        return _app
    else:
        print(f"Application '{app}' not found")


@cli.command(name="show-application")
@click.argument("app", autocompletion=app_completion)
@click.option("--org_id", default=None)
@click.pass_context
def show_application(ctx, app, **kwargs):
    _app = _get_app(ctx, app, **kwargs)
    if _app:
        output_entry(ctx, _app)


@cli.command(name="update-application")
@click.argument("app", autocompletion=app_completion)
@click.option("--image", default=None)
@click.option("--port", type=int, default=None)
@click.option("--org_id", default=None)
@click.option("--published", type=click.Choice(["no", "public"]), default=None)
@click.option("--default_role_id", default=None)
@click.option("--icon_url", default=None)
@click.option("--location", type=click.Choice(["hosted", "external"]), default=None)
@click.pass_context
def update_application(ctx, app, org_id, **kwargs):
    _app = _get_app(ctx, app, org_id=org_id)
    if _app:
        apps.update_application(ctx, _app["id"], org_id, **kwargs)
        output_entry(ctx, json.loads(apps.get(ctx, _app["id"])))


@cli.command(name="add-role")
@click.argument("app", autocompletion=app_completion)
@click.argument("role-name")
@click.pass_context
def add_role(ctx, app, role_name):
    _app = _get_app(ctx, app)
    if _app:
        apps.add_role(ctx, _app["id"], role_name)
        output_entry(ctx, json.loads(apps.get(ctx, _app["id"])))


@cli.command(name="rules-from-csv")
@click.argument("app", autocompletion=app_completion)
@click.argument("role-name")
@click.option("--file-name", default="-")
@click.option("--org_id", default=None)
@click.option("--hostname", default=None)
@click.pass_context
def rules_from_csv(ctx, app, role_name, file_name, org_id, hostname):
    _app = _get_app(ctx, app, org_id=org_id)
    if _app:
        result = csv_rules.add_rules_to_app(
            ctx, _app["id"], role_name, file_name, org_id, hostname
        )
        output_entry(ctx, result)


@cli.command(name="add-definition")
@click.argument("app", autocompletion=app_completion)
@click.argument("key")
@click.argument("json-path")
@click.pass_context
def add_definition(ctx, app, key, json_path):
    _app = _get_app(ctx, app)
    if _app:
        apps.add_definition(ctx, _app["id"], key, json_path)
        output_entry(ctx, json.loads(apps.get(ctx, _app["id"])))


@cli.command(name="add-rule")
@click.argument("app", autocompletion=app_completion)
@click.argument("role-name")
@click.argument("method")
@click.argument("path-regex")
@click.option("--query-param", "-q", type=click.Tuple([str, str]), multiple=True)
@click.option("--json-pointer", "-j", type=click.Tuple([str, str]), multiple=True)
@click.option("--rule-name", default=None)
@click.option("--host", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def add_rule(
    ctx,
    app,
    role_name,
    method,
    path_regex,
    query_param,
    json_pointer,
    **kwargs,
):
    apps.add_rule(
        ctx,
        app,
        role_name,
        method,
        path_regex,
        query_param,
        json_pointer,
        **kwargs,
    )


@cli.command(name="list-rules")
@click.argument("app", autocompletion=app_completion)
@click.option("--org_id", default=None)
@click.pass_context
def list_rules(ctx, **kwargs):
    table = PrettyTable(
        ["role", "name", "host", "method", "path", "query_param", "json_body"]
    )
    for role in apps.get_roles(ctx, **kwargs):
        for rule in role.get("rules", []):
            body = rule.get("body", {})
            json_body = None
            if body:
                json_body = body.get("json", None)
            table.add_row(
                [
                    role["name"],
                    rule["name"],
                    rule.get("host", ""),
                    rule["method"],
                    rule["path"],
                    rule.get("query_parameters", None),
                    json_body,
                ]
            )
    table.align = "l"
    print(table)


# Rows is a list of dictonaries with the same keys
def _format_subtable_objs(rows):
    return _format_subtable([row.to_dict() for row in rows])


def _format_subtable(rows):
    if not rows:
        return None

    column_names = [k for k, _ in rows[0].items()]
    table = PrettyTable(column_names)
    table.align = "l"
    for row in rows:  # dict
        values = [v for _, v in row.items()]
        table.add_row(values)
    return table


@cli.command(name="list-mfa-challenge-methods")
@click.argument("user-id", default=None)
@click.option("--challenge_type", default=None)
@click.option("--method_status", type=bool, default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_mfa_challenge_methods(ctx, user_id, **kwargs):
    methods = users.list_mfa_challenge_methods(ctx, user_id, **kwargs)
    table = PrettyTable(
        ["ID", "nickname", "challenge_type", "priority", "endpoint", "enabled"]
    )
    for method in methods:
        md = method.metadata
        spec = method.spec
        table.add_row(
            [
                md.id,
                spec.nickname,
                spec.challenge_type,
                spec.priority,
                spec.endpoint,
                spec.enabled,
            ]
        )
    table.align = "l"
    print(table)


@cli.command(name="add-mfa-challenge-method")
@click.argument("user-id", default=None)
@click.option(
    "--challenge_type",
    type=click.Choice(["web_push", "totp", "webauthn"]),
    default=None,
)
@click.option("--priority", type=int, default=None)
@click.option("--endpoint", default=None)
@click.option("--nickname", default=None)
@click.option("--enabled/--disabled", default=None)
@click.pass_context
def add_mfa_challenge_method(ctx, user_id, **kwargs):
    result = users.add_mfa_challenge_method(ctx, user_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-mfa-challenge-method")
@click.argument("user-id", default=None)
@click.argument("challenge-method-id", default=None)
@click.pass_context
def show_mfa_challenge_method(ctx, user_id, challenge_method_id, **kwargs):
    result = users.show_mfa_challenge_method(ctx, user_id, challenge_method_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-mfa-challenge-method")
@click.argument("user-id", default=None)
@click.argument("challenge-method-id", default=None)
@click.pass_context
def delete_mfa_challenge_method(ctx, user_id, challenge_method_id, **kwargs):
    users.delete_mfa_challenge_method(ctx, user_id, challenge_method_id, **kwargs)


@cli.command(name="reset-user-mfa-challenge-methods")
@click.argument("user-id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def reset_user_mfa_challenge_methods(ctx, user_id, **kwargs):
    users.reset_user_mfa_challenge_methods(ctx, user_id, **kwargs)


@cli.command(name="update-mfa-challenge-method")
@click.argument("user-id", default=None)
@click.argument("challenge-method-id", default=None)
@click.option("--challenge_type", type=click.Choice(["web_push"]), default=None)
@click.option("--priority", type=int, default=None)
@click.option("--endpoint", default=None)
@click.option("--nickname", default=None)
@click.option("--enabled/--disabled", default=None)
@click.pass_context
def update_mfa_challenge_method(ctx, user_id, challenge_method_id, **kwargs):
    result = users.update_mfa_challenge_method(
        ctx, user_id, challenge_method_id, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="list-app-rules")
@click.argument("app-id", default=None)
@click.option("--org_id", default=None)
@click.option("--scope", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_app_rules(ctx, app_id, **kwargs):
    app_rules = apps.list_app_rules(ctx, app_id, **kwargs)
    table = PrettyTable(
        [
            "app_id",
            "rule_id",
            "org_id",
            "scope",
            "rule_type",
            "methods",
            "path",
            "query_param",
            "json_body",
        ]
    )
    for rule in app_rules:
        spec = rule.spec
        cond = spec.condition
        table.add_row(
            [
                spec.app_id,
                rule.metadata.id,
                spec.org_id,
                spec.scope,
                cond.rule_type,
                cond.methods,
                cond.path_regex,
                _format_subtable_objs(cond.query_parameters),
                _format_subtable_objs(cond.body.json),
            ]
        )

    table.align = "l"
    print(table)


@cli.command(name="list-combined-rules")
@click.option("--org_id", default=None)
@click.option("--scopes", multiple=True, default=None)
@click.option("--assigned", is_flag=True)
@click.option("--app_id", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_combined_rules(ctx, **kwargs):
    rules = apps.list_combined_rules(ctx, **kwargs)
    table = PrettyTable(["app_id", "role_id", "role_name", "org_id", "scope", "rules"])
    for rule in rules:
        status = rule.status
        table.add_row(
            [
                status.app_id,
                status.role_id,
                status.role_name,
                status.org_id,
                status.scope,
                _format_subtable_objs(
                    [sub_rule.spec.condition for sub_rule in status.rules]
                ),
            ]
        )

    table.align = "l"
    print(table)


@cli.command(name="add-http-rule")
@click.argument("app-id")
@click.argument("path-regex")
@click.argument("methods", nargs=-1)
@click.option("--rule_type", default="HttpRule")
@click.option("--comments", default=None)
@click.option("--org_id", default=None)
@click.option("--rule_scope", default=None)
@click.pass_context
def add_http_rule(ctx, app_id, **kwargs):
    result = apps.add_http_rule(ctx, app_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-rule-v2")
@click.argument("app-id")
@click.argument("rule-id")
@click.option("--org_id", default=None)
@click.pass_context
def show_rule_v2(ctx, app_id, rule_id, **kwargs):
    result = apps.show_rule_v2(ctx, app_id, rule_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-rule-v2")
@click.argument("app-id")
@click.argument("rule-id")
@click.option("--org_id", default=None)
@click.pass_context
def delete_rule_v2(ctx, app_id, rule_id, **kwargs):
    apps.delete_rule_v2(ctx, app_id, rule_id, **kwargs)


@cli.command(name="update-http-rule")
@click.argument("app-id")
@click.argument("rule-id")
@click.option("--path_regex", default=None)
@click.option("--rule_type", default="HttpRule")
@click.option("--comments", default=None)
@click.option("--org_id", default=None)
@click.option("--rule_scope", default=None)
@click.pass_context
def update_http_rule(ctx, app_id, rule_id, rule_scope, **kwargs):
    result = apps.update_http_rule(ctx, app_id, rule_id, scope=rule_scope, **kwargs)
    output_entry(ctx, result)


@cli.command(name="update-http-rule-methods")
@click.argument("app-id")
@click.argument("rule-id")
@click.option("--methods", multiple=True, default=[])
@click.option("--org_id", default=None)
@click.pass_context
def update_http_rule_methods(ctx, app_id, rule_id, methods, **kwargs):
    result = apps.update_http_rule(ctx, app_id, rule_id, methods=methods, **kwargs)
    output_entry(ctx, result)


@cli.command(name="update-http-rule-query-params")
@click.argument("app-id")
@click.argument("rule-id")
@click.option(
    "--query-param",
    "-q",
    type=click.Tuple([str, str]),
    multiple=True,
    default=[],
    help="A pair of strings representing the query parameter name, match value",
)
@click.option("--org_id", default=None)
@click.pass_context
def update_http_rule_query_params(ctx, app_id, rule_id, query_param, **kwargs):
    result = apps.update_http_rule(
        ctx, app_id, rule_id, query_params=query_param, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="update-http-rule-body-params")
@click.argument("app-id")
@click.argument("rule-id")
@click.option(
    "--body_param",
    "-bp",
    type=click.Tuple([str, str, str, str]),
    multiple=True,
    help="A tuple of strings representing the name, value to match against, match type, and json pointer path",  # noqa
)
@click.option("--org_id", default=None)
@click.pass_context
def update_http_rule_body_params(ctx, app_id, rule_id, body_param, **kwargs):
    result = apps.update_http_rule(
        ctx, app_id, rule_id, body_params=body_param, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="list-roles")
@click.argument("app-id", default=None)
@click.option("--org_id", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_roles(ctx, app_id, **kwargs):
    roles = apps.list_roles(ctx, app_id, **kwargs)
    table = PrettyTable(["app_id", "role_id", "name", "org_id", "included_roles"])
    for role in roles:
        spec = role.spec
        table.add_row(
            [
                spec.app_id,
                role.metadata.id,
                spec.name,
                spec.org_id,
                _format_subtable_objs(spec.included),
            ]
        )

    table.align = "l"
    print(table)


@cli.command(name="add-role-v2")
@click.argument("app-id", default=None)
@click.argument("name", default=None)
@click.option("--org_id", default=None)
@click.option("--comments", default=None)
@click.option("--included", multiple=True)
@click.pass_context
def add_role_v2(ctx, app_id, name, **kwargs):
    result = apps.add_role_v2(ctx, app_id, name, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-role-v2")
@click.argument("app-id", default=None)
@click.argument("role-id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def show_role(ctx, app_id, role_id, **kwargs):
    result = apps.show_role_v2(ctx, app_id, role_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-role-v2")
@click.argument("app-id", default=None)
@click.argument("role-id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_role(ctx, app_id, role_id, **kwargs):
    apps.delete_role_v2(ctx, app_id, role_id, **kwargs)


@cli.command(name="update-role-v2")
@click.argument("app-id", default=None)
@click.argument("role-id", default=None)
@click.option("--name", default=None)
@click.option("--comments", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def update_role(ctx, app_id, role_id, **kwargs):
    result = apps.update_role_v2(ctx, app_id, role_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="update-role-includes")
@click.argument("app-id", default=None)
@click.argument("role-id", default=None)
@click.option("--included", multiple=True, default=[])
@click.pass_context
def update_role_includes(ctx, app_id, role_id, included, **kwargs):
    result = apps.update_role_v2(ctx, app_id, role_id, included=included, **kwargs)
    output_entry(ctx, result)


@cli.command(name="list-roles-to-rules")
@click.argument("app-id", default=None)
@click.option("--org_id", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_roles_to_rules(ctx, app_id, **kwargs):
    roles = apps.list_roles_to_rules(ctx, app_id, **kwargs)
    table = PrettyTable(["role_to_rule_id", "role_id", "rule_id", "org_id", "included"])
    for role in roles:
        spec = role.spec
        table.add_row(
            [role.metadata.id, spec.role_id, spec.rule_id, spec.org_id, spec.included]
        )

    table.align = "l"
    print(table)


@cli.command(name="add-role-to-rule")
@click.argument("app-id", default=None)
@click.argument("role-id", default=None)
@click.argument("rule-id", default=None)
@click.option("--org_id", default=None)
@click.option("--included/--excluded", default=True)
@click.pass_context
def add_role_to_rule(ctx, app_id, role_id, rule_id, **kwargs):
    result = apps.add_role_to_rule(ctx, app_id, role_id, rule_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-role-to-rule")
@click.argument("app-id", default=None)
@click.argument("role-to-rule-id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def show_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs):
    result = apps.show_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-role-to-rule")
@click.argument("app-id", default=None)
@click.argument("role-to-rule-id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs):
    apps.delete_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs)


@cli.command(name="update-role-to-rule")
@click.argument("app-id", default=None)
@click.argument("role-to-rule-id", default=None)
@click.option("--org_id", default=None)
@click.option("--included/--excluded", default=True)
@click.pass_context
def update_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs):
    result = apps.update_role_to_rule(ctx, app_id, role_to_rule_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-rule")
@click.argument("app", autocompletion=app_completion)
@click.argument("role_name")
@click.argument("rule_name")
@click.option("--org_id", default=None)
@click.pass_context
def delete_rule(ctx, **kwargs):
    apps.delete_rule(ctx, **kwargs)


@cli.command(name="whoami")
@click.option("--refresh/--no-refresh", default=False)
@click.pass_context
def get_whoami(ctx, refresh=None, **kwargs):
    token = whoami.whoami(ctx, refresh, **kwargs)
    print("Token:")
    output_entry(ctx, jwt.decode(token, verify=False))
    # print("Whoami response data:")
    # output_entry(access.get_whoami_resp(ctx))


@cli.command(name="show-token-introspection")
@click.option("--refresh", default=False)
@click.option("--token", default=None)
@click.option("--exclude_roles", default=False, type=bool)
@click.pass_context
def show_token_introspection(
    ctx, refresh=None, token=None, exclude_roles=False, **kwargs
):
    my_token = token
    if not my_token:
        my_token = whoami.whoami(ctx, refresh, **kwargs)
    result = tokens.get_introspect(ctx, my_token, exclude_roles, **kwargs)
    print(result)


@cli.command(name="get-token")
@click.pass_context
def get_token(ctx, **kwargs):
    token = whoami.whoami(ctx, False, **kwargs)
    if not token:
        print("No token found", file=sys.stderr)
        sys.exit(1)

    print(token)


@cli.command(name="create-token")
@click.argument("user")
@click.argument("org_id", type=str)
@click.option("--role", "-r", type=click.Tuple([str, str]), multiple=True)
@click.option("--duration", type=int, default=3600)
@click.option("--aud", type=str, multiple=True)
@click.pass_context
def create_token(ctx, user, org_id, role, duration, aud):
    roles = {endpoint: role_name for endpoint, role_name in role}
    token = tokens.create_token(ctx, user, roles, duration, aud, org_id=org_id)
    if not token:
        sys.exit(1)

    print(token)


@cli.command(name="list-files")
@click.option("--org_id", default=None)
@click.option("--tag", default=None)
@click.pass_context
def list_files(ctx, **kwargs):
    _files = files.query(ctx, **kwargs)
    table = PrettyTable(
        ["id", "name", "tag", "label", "created", "last_accessed", "size", "visibility"]
    )
    table.align = "l"
    for _file in _files:
        _file["tag"] = _file["tag"] if "tag" in _file else ""
        _file["label"] = _file["label"] if "label" in _file else ""
        table.add_row(
            [
                _file["id"],
                _file["name"],
                _file["tag"],
                _file["label"],
                _file["created"],
                _file["last_access"],
                _file["size"],
                _file["visibility"],
            ]
        )
    print(table)


@cli.command(name="upload-file")
@click.argument("filename", type=click.Path(exists=True))
@click.option("--org_id", default=None)
@click.option("--name", default=None)
@click.option("--label", default=None)
@click.option("--tag", default=None)
@click.option("--region", default=None)
@click.option("--visibility", type=click.Choice(["public", "private"]), default=None)
@click.pass_context
def upload_file(ctx, **kwargs):
    output_entry(ctx, files.upload(ctx, **kwargs))


@cli.command(name="download-file")
@click.argument("file_id")
@click.option("--org_id", default=None)
@click.option("--destination", default=None)
@click.pass_context
def download_file(ctx, **kwargs):
    files.download(ctx, **kwargs)


@cli.command(name="delete-file")
@click.argument("file_ids", nargs=-1)
@click.option("--org_id", default=None)
@click.pass_context
def delete_file(ctx, file_ids, **kwargs):
    for file_id in file_ids:
        files.delete(ctx, file_id=file_id, **kwargs)


@cli.command(name="show-file")
@click.argument("file_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def show_file(ctx, **kwargs):
    output_entry(ctx, files.get(ctx, **kwargs))


@cli.command(name="list-config")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.pass_context
def list_config(ctx, **kwargs):
    configs = env_config.query(ctx, **kwargs)

    table = PrettyTable(
        [
            "id",
            "config_type",
            "host",
            "src_mount",
            "domain",
            "share",
            "username",
            "password",
            "dest_mount",
            "file_store_uri",
        ]
    )
    table.align = "l"
    for config in configs:
        table.add_row(
            [
                config.id,
                config.config_type,
                config.mount_hostname,
                config.mount_src_path,
                config.mount_domain,
                config.mount_share,
                config.mount_username,
                config.mount_password,
                config.mount_path,
                config.file_store_uri,
            ]
        )
    print(table)


@cli.command(name="add-config")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.option("--filename", default=None)
@click.option(
    "--config_type",
    type=click.Choice(
        [
            "configmap_mount",
            "configmap_env",
            "secret_mount",
            "secret_env",
            "mount_smb",
            "mount_tmpdir",
            "file_mount",
        ]
    ),
    prompt=True,
)
@click.option("--mount_path", default=None, prompt=True)
@click.option("--mount_src_path", default=None)
@click.option("--username", default=None)
@click.option("--hostname", default=None)
@click.option("--password", default=None)
@click.option("--share", default=None)
@click.option("--domain", default=None)
@click.option("--file_store_uri", default=None)
@click.pass_context
def add_config(ctx, **kwargs):
    output_entry(ctx, env_config.add(ctx, **kwargs).to_dict())


@cli.command(name="update-config")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.argument("id", default=None)
@click.option("--org_id", default=None)
@click.option(
    "--config_type",
    type=click.Choice(
        [
            "configmap_mount",
            "configmap_env",
            "secret_mount",
            "secret_env",
            "file_mount",
        ]
    ),
)
@click.option("--mount_path", default=None)
@click.option("--mount_src_path", default=None)
@click.option("--username", default=None)
@click.option("--password", default=None)
@click.option("--share", default=None)
@click.option("--domain", default=None)
@click.option("--file_store_uri", default=None)
@click.pass_context
def update_config(ctx, **kwargs):
    output_entry(ctx, env_config.update(ctx, **kwargs).to_dict())


@cli.command(name="delete-config")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.argument("id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_config(ctx, **kwargs):
    env_config.delete(ctx, **kwargs)


@cli.command(name="list-env-vars")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.option("--org_id", default=None)
@click.option("--secret", default=True)
@click.pass_context
def list_env_vars(ctx, **kwargs):
    envVar = env_config.EnvVarConfigObj(ctx, **kwargs)
    new_envs = envVar.get_env_list()

    table = PrettyTable(["key", "value"])
    table.align = "l"
    for env in new_envs:
        table.add_row([env.name, env.value])
    print(table)


@cli.command(name="add-env-var")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.argument("env_config_name", default=None)
@click.argument("env_config_value", default=None)
@click.option("--org_id", default=None)
@click.option("--secret", default=True)
@click.pass_context
def add_env_var(ctx, env_config_name, env_config_value, **kwargs):
    envVar = env_config.EnvVarConfigObj(ctx, **kwargs)
    envVar.add_env_var(env_config_name, env_config_value)


@cli.command(name="delete-env-var")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.argument("env_var_name", default=None)
@click.option("--org_id", default=None)
@click.option("--secret", default=True)
@click.pass_context
def delete_env_var(ctx, env_var_name, **kwargs):
    envVar = env_config.EnvVarConfigObj(ctx, **kwargs)
    envVar.del_env_var(env_var_name)


@cli.command(name="update-env-var")
@click.argument("application", autocompletion=app_completion)
@click.argument("env_name", autocompletion=env_completion)
@click.argument("env_config_name", default=None)
@click.argument("env_config_value", default=None)
@click.option("--secret", default=True)
@click.pass_context
def update_env_var(ctx, env_config_name, env_config_value, **kwargs):
    envVar = env_config.EnvVarConfigObj(ctx, **kwargs)
    envVar.update_env_var(env_config_name, env_config_value)


@cli.command(name="get-logs")
@click.argument("org_id", default=None)
@click.option("--sub_org_id", default=None)
@click.option("--app", default=None)
@click.option("--dt_from", default=None)
@click.option("--dt_to", default=None)
@click.option("--dt_sort", default="asc")
@click.option("--limit", default=None)
@click.pass_context
def get_logs(ctx, **kwargs):
    _logs = logs.get(ctx, **kwargs)
    print(_logs)


@cli.command(name="get-top-users")
@click.argument("org_id", default=None)
@click.option("--dt_from", default=None)
@click.option("--dt_to", default=None)
@click.option("--app_id", default=None)
@click.option("--sub_org_id", default=None)
@click.option("--interval", default=None)
@click.option("--limit", default=None)
@click.pass_context
def get_top_users(ctx, **kwargs):
    _metrics = metrics.query_top(ctx, **kwargs)
    table = PrettyTable(["user_id", "email", "count"])
    table.align = "l"
    if _metrics is not None:
        for _metric in _metrics:
            table.add_row([_metric.user_id, _metric.email, _metric.count])
    print(table)


@cli.command(name="get-active-users")
@click.argument("org_id", default=None)
@click.option("--dt_from", default=None)
@click.option("--dt_to", default=None)
@click.option("--app_id", default=None)
@click.option("--sub_org_id", default=None)
@click.option("--interval", default=None)
@click.pass_context
def get_active_users(ctx, **kwargs):
    _metrics = metrics.query_active(ctx, **kwargs)
    table = PrettyTable(["time", "metric"])
    table.align = "l"
    if _metrics is not None:
        for _metric in _metrics:
            table.add_row([_metric.time, _metric.metric])
    print(table)


def _format_catalogue_entries_subtable(entries):
    table = PrettyTable(["name", "tag", "content"])
    table.align = "l"
    if entries:
        for entry in entries:
            table.add_row([entry.name, entry.tag, entry.content])
    return table


@cli.command(name="list-catalogues")
@click.option("--catalogue_category", default=None)
@click.option("--limit", default=25, type=int)
@click.pass_context
def list_catalogues(ctx, **kwargs):
    cats = catalogues.query(ctx, **kwargs)
    table = PrettyTable(["id", "category", "entries summary"])
    table.align = "l"
    for cat in cats:
        table.add_row(
            [
                cat.id,
                cat.category,
                _format_catalogue_entries_subtable(cat.catalogue_entries),
            ]
        )
    print(table)


@cli.command(name="show-catalogue")
@click.argument("catalogue_id", default=None)
@click.pass_context
def show_catalogue(ctx, **kwargs):
    output_entry(ctx, catalogues.show(ctx, **kwargs))


@cli.command(name="add-catalogue")
@click.argument("category", default=None)
@click.pass_context
def add_catalogue(ctx, **kwargs):
    output_entry(ctx, catalogues.add(ctx, **kwargs))


@cli.command(name="update-catalogue")
@click.argument("catalogue_id", default=None)
@click.option("--category", default=None)
@click.pass_context
def update_catalogue(ctx, **kwargs):
    output_entry(ctx, catalogues.update(ctx, **kwargs))


@cli.command(name="delete-catalogue")
@click.argument("catalogue_id", default=None)
@click.pass_context
def delete_catalogue(ctx, **kwargs):
    catalogues.delete(ctx, **kwargs)


@cli.command(name="list-catalogue-entries")
@click.option("--catalogue_id", default=None)
@click.option("--catalogue_category", default=None)
@click.option("--catalogue_entry_name", default=None)
@click.option("--limit", default=50, type=int)
@click.pass_context
def list_catalogue_entries(ctx, **kwargs):
    catalogue_id = kwargs.pop("catalogue_id", None)
    entries = catalogues.query_entries(ctx, catalogue_id=catalogue_id, **kwargs)
    table = PrettyTable(
        [
            "id",
            "catalogue_id",
            "category",
            "name",
            "content",
            "tag",
            "short desc",
            "long desc",
        ]
    )
    table.align = "l"
    for entry in entries:
        table.add_row(
            [
                entry.id,
                entry.catalogue_id,
                entry.catalogue_category,
                entry.name,
                entry.content,
                entry.tag,
                entry.short_description,
                entry.long_description,
            ]
        )
    print(table)


@cli.command(name="show-catalogue-entry")
@click.argument("catalogue_id", default=None)
@click.argument("entry_id", default=None)
@click.pass_context
def show_catalogue_entry(ctx, **kwargs):
    output_entry(ctx, catalogues.show_entry(ctx, **kwargs))


@cli.command(name="add-catalogue-entry")
@click.argument("catalogue_id", default=None)
@click.argument("name", default=None)
@click.option("--content", default=None)
@click.option("--tag", default=None)
@click.option("--short_description", default=None)
@click.option("--long_description", default=None)
@click.pass_context
def add_catalogue_entry(ctx, **kwargs):
    output_entry(ctx, catalogues.add_entry(ctx, **kwargs))


@cli.command(name="update-catalogue-entry")
@click.argument("catalogue_id", default=None)
@click.argument("entry_id", default=None)
@click.option("--name", default=None)
@click.option("--content", default=None)
@click.option("--tag", default=None)
@click.option("--short_description", default=None)
@click.option("--long_description", default=None)
@click.pass_context
def update_catalogue_entry(ctx, **kwargs):
    output_entry(ctx, catalogues.update_entry(ctx, **kwargs))


@cli.command(name="delete-catalogue-entry")
@click.argument("catalogue_id", default=None)
@click.argument("entry_id", default=None)
@click.pass_context
def delete_catalogue_entry(ctx, **kwargs):
    catalogues.delete_entry(ctx, **kwargs)


def _format_flat_list(items):
    return [item for item in items]


@cli.command(name="list-issuers")
@click.option("--org_id", default=None)
@click.option("--limit", default=25, type=int)
@click.pass_context
def list_issuers(ctx, **kwargs):
    _issuers = issuers.query(ctx, **kwargs)
    table = PrettyTable(
        [
            "issuer-id",
            "issuer",
            "enabled",
            "client-id",
            "client",
            "org",
            "secret",
            "application",
            "organisation_scope",
            "redirects",
            "restricted_organisations",
        ]
    )
    table.align = "l"
    for issuer in _issuers:
        if len(issuer.clients):
            for client in issuer.clients:
                table.add_row(
                    [
                        issuer.id,
                        issuer.issuer,
                        issuer.enabled,
                        client.id,
                        client.name,
                        client.org_id,
                        client.secret,
                        client.application,
                        client.organisation_scope,
                        _format_flat_list(client.redirects),
                        _format_flat_list(client.restricted_organisations),
                    ]
                )
        else:
            table.add_row(
                [
                    issuer.id,
                    issuer.issuer,
                    issuer.enabled,
                    "-",
                    "-",
                    issuer.org_id,
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                ]
            )
    print(table)


@cli.command(name="show-issuer")
@click.argument("issuer_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def show_issuer(ctx, **kwargs):
    output_entry(ctx, issuers.show(ctx, **kwargs))


@cli.command(name="show-wellknown-issuer-info")
@click.argument("issuer_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def show_well_known_issuer_info(ctx, **kwargs):
    output_entry(ctx, issuers.show_well_known(ctx, **kwargs))


@cli.command(name="list-wellknown-issuer-info")
@click.option("--org_id", default=None)
@click.pass_context
def list_well_known_issuer_info(ctx, **kwargs):
    result = issuers.list_well_known(ctx, **kwargs)
    print(issuers.format_well_known_issuer_info(result))


@cli.command(name="add-issuer")
@click.argument("issuer", default=None)
@click.argument("org_id", default=None)
@click.pass_context
def add_issuer(ctx, **kwargs):
    output_entry(ctx, issuers.add(ctx, **kwargs))


@cli.command(name="update-issuer-root")
@click.argument("issuer_id", default=None)
@click.option("--issuer", default=None)
@click.option("--org_id", default=None)
@click.option("--theme_file_id", type=str, default=None)
@click.option("--upstream_redirect_uri", default=None)
@click.option("--enabled/--disabled", default=None)
@click.pass_context
def update_issuer_root(ctx, issuer_id, **kwargs):
    output_entry(ctx, issuers.update_root(ctx, issuer_id, **kwargs))


@cli.command(name="update-issuer")
@click.argument("issuer_id", default=None)
@click.option("--theme_file_id", default=None)
@click.option("--org_id", default=None)
@click.option("--enabled/--disabled", default=None)
@click.pass_context
def update_issuer_extension(ctx, issuer_id, **kwargs):
    output_entry(ctx, issuers.update_extension(ctx, issuer_id, **kwargs))


@cli.command(name="delete-issuer")
@click.argument("issuer_id", default=None)
@click.pass_context
def delete_issuer(ctx, **kwargs):
    issuers.delete(ctx, **kwargs)


@cli.command(name="list-clients")
@click.option("--org_id", default=None)
@click.option("--limit", default=25, type=int)
@click.option("--summarize_collection", default=True, type=bool)
@click.pass_context
def list_clients(ctx, **kwargs):
    _clients = issuers.query_clients(ctx, **kwargs)
    table = PrettyTable(
        [
            "id",
            "issuer_id",
            "org_id",
            "name",
            "secret",
            "application",
            "organisation_scope",
            "mfa_challenge",
            "redirects",
            "restricted_organisations",
        ]
    )
    table.align = "l"
    for client in _clients:
        table.add_row(
            [
                client.id,
                client.issuer_id,
                client.org_id,
                client.name,
                client.secret,
                client.application,
                client.organisation_scope,
                client.mfa_challenge,
                _format_flat_list(client.redirects),
                _format_flat_list(client.restricted_organisations),
            ]
        )
    print(table)


@cli.command(name="show-client")
@click.argument("client_id", default=None)
@click.option("--org_id", default=None)
@click.option("--summarize_collection", default=True, type=bool)
@click.pass_context
def show_client(ctx, **kwargs):
    output_entry(ctx, issuers.show_client(ctx, **kwargs))


@cli.command(name="add-client")
@click.argument("issuer_id", default=None)
@click.argument("name", default=None)
@click.option("--secret", default=None)
@click.option("--application", default=None)
@click.option("--org_id", default=None)
@click.option(
    "--organisation_scope",
    default=None,
    type=click.Choice(["any", "here_and_down", "here_only"]),
)
@click.option(
    "--mfa_challenge",
    default=None,
    type=click.Choice(["always", "trust_upstream", "user_preference"]),
)
@click.option("--redirect_url", default=None, multiple=True)
@click.option("--restricted_org_id", default=None, multiple=True)
@click.option("--metadata_file", default=None)
@click.option("--metadata_text", default=None)
@click.pass_context
def add_client(ctx, redirect_url, restricted_org_id, **kwargs):
    output_entry(
        ctx,
        issuers.add_client(
            ctx,
            restricted_organisations=restricted_org_id,
            redirects=redirect_url,
            **kwargs,
        ),
    )


@cli.command(name="update-client")
@click.argument("client_id", default=None)
@click.option("--name", default=None)
@click.option("--secret", default=None)
@click.option("--application", default=None)
@click.option("--org_id", default=None)
@click.option("--issuer_id", default=None)
@click.option(
    "--organisation_scope",
    default=None,
    type=click.Choice(["any", "here_and_down", "here_only"]),
)
@click.option(
    "--mfa_challenge",
    default=None,
    type=click.Choice(["always", "trust_upstream", "user_preference"]),
)
@click.option("--metadata_file", default=None)
@click.option("--metadata_text", default=None)
@click.pass_context
def update_client(ctx, **kwargs):
    output_entry(
        ctx,
        issuers.update_client(
            ctx,
            **kwargs,
        ),
    )


@cli.command(name="delete-client")
@click.argument("client_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_client(ctx, **kwargs):
    issuers.delete_client(ctx, **kwargs)


@cli.command(name="add-redirect")
@click.argument("client_id", default=None)
@click.argument("redirect_url", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def add_redirect(ctx, **kwargs):
    output_entry(ctx, issuers.add_redirect(ctx, **kwargs))


@cli.command(name="delete-redirect")
@click.argument("client_id", default=None)
@click.argument("redirect_url", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_redirect(ctx, **kwargs):
    output_entry(ctx, issuers.delete_redirect(ctx, **kwargs))


@cli.command(name="replace-redirects")
@click.argument("client_id", default=None)
@click.option("--redirect_url", default=None, multiple=True)
@click.option("--org_id", default=None)
@click.pass_context
def replace_redirets(ctx, redirect_url=None, **kwargs):
    output_entry(ctx, issuers.update_client(ctx, redirects=redirect_url, **kwargs))


@cli.command(name="add-restricted-org")
@click.argument("client_id", default=None)
@click.argument("restricted_org_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def add_restricted_org(ctx, **kwargs):
    output_entry(ctx, issuers.add_restricted_organisation(ctx, **kwargs))


@cli.command(name="delete-restricted-org")
@click.argument("client_id", default=None)
@click.argument("restricted_org_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_restricted_org(ctx, **kwargs):
    output_entry(ctx, issuers.delete_restricted_organisation(ctx, **kwargs))


@cli.command(name="replace-restricted-orgs")
@click.argument("client_id", default=None)
@click.option("--restricted_org_id", default=None, multiple=True)
@click.option("--org_id", default=None)
@click.pass_context
def replace_restricted_orgs(ctx, restricted_org_id, **kwargs):
    output_entry(
        ctx,
        issuers.update_client(ctx, restricted_organisations=restricted_org_id, **kwargs),
    )


@cli.command(name="set-attribute-mapping")
@click.argument("client_id", default=None)
@click.argument("attribute_name", default=None)
@click.argument("attribute_path", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def set_attribute_mapping(ctx, client_id, attribute_name, attribute_path, **kwargs):
    result = issuers.set_attribute_mapping(
        ctx,
        client_id,
        attribute_name,
        attribute_path,
        **kwargs,
    )

    print(issuers.format_attributes(result))


@cli.command(name="delete-attribute-mapping")
@click.argument("client_id", default=None)
@click.argument("attribute_name", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_attribute_mapping(ctx, client_id, attribute_name, **kwargs):
    result = issuers.delete_attribute_mapping(
        ctx,
        client_id,
        attribute_name,
        **kwargs,
    )

    print(issuers.format_attributes(result))


@cli.command(name="list-managed-upstream-providers")
@click.argument("issuer_id", default=None)
@click.pass_context
def list_managed_upstream_providers(ctx, issuer_id=None, **kwargs):
    issuer = issuers.show(ctx, issuer_id, **kwargs)
    upstreams = issuer.get("managed_upstreams", [])
    table = PrettyTable(["Name", "enabled"])
    table.align = "l"
    for upstream in upstreams:
        table.add_row([upstream["name"], upstream["enabled"]])
    print(table)


@cli.command(name="update-managed-upstream-provider")
@click.argument("issuer_id", default=None)
@click.argument("name", default=None)
@click.option("--enabled/--disabled", required=True, default=None)
@click.option("--org_id", default=None)
@click.pass_context
def update_managed_upstream_provider(
    ctx, issuer_id=None, name=None, enabled=None, **kwargs
):
    issuer = issuers.update_managed_upstreams(ctx, issuer_id, name, enabled, **kwargs)
    if issuer:
        output_entry(ctx, issuer)


@cli.command(name="list-oidc-upstream-providers")
@click.argument("issuer_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def list_oidc_upstream_providers(ctx, issuer_id=None, **kwargs):
    issuer = issuers.show(ctx, issuer_id, **kwargs)
    upstreams = issuer.get("oidc_upstreams", [])
    table = PrettyTable(
        [
            "name",
            "issuer",
            "icon",
            "client_id",
            "client_secret",
            "issuer_external_host",
            "username_key",
            "user_id_key",
            "email_key",
            "email_verification_required",
            "request_user_info",
            "auto_create_status",
        ]
    )
    table.align = "l"
    for upstream in upstreams:
        table.add_row(
            [
                upstream["name"],
                upstream["issuer"],
                upstream["icon"],
                upstream["client_id"],
                upstream["client_secret"],
                upstream["issuer_external_host"],
                upstream["username_key"],
                upstream["user_id_key"],
                upstream["email_key"],
                upstream["email_verification_required"],
                upstream["request_user_info"],
                upstream.get("auto_create_status", "---"),
            ]
        )
    print(table)


@cli.command(name="update-oidc-upstream-provider")
@click.argument("issuer_id", default=None)
@click.argument("name", default=None)
@click.option("--icon", default=None)
@click.option("--issuer", default=None)
@click.option("--client_id", default=None)
@click.option("--client_secret", default=None)
@click.option("--issuer_external_host", default=None)
@click.option("--username_key", default=None)
@click.option("--user_id_key", default=None)
@click.option("--email_key", default=None)
@click.option("--email_verification_required", type=bool, default=None)
@click.option("--request_user_info", type=bool, default=None)
@click.option(
    "--auto_create_status", type=click.Choice(users.STATUS_OPTIONS), default=None
)
@click.option("--org_id", default=None)
@click.pass_context
def update_oidc_upstream_provider(
    ctx,
    issuer_id=None,
    name=None,
    icon=None,
    issuer=None,
    client_id=None,
    client_secret=None,
    issuer_external_host=None,
    username_key=None,
    user_id_key=None,
    email_key=None,
    email_verification_required=None,
    request_user_info=None,
    auto_create_status=None,
    **kwargs,
):
    issuer = issuers.update_oidc_upstreams(
        ctx,
        issuer_id,
        name,
        icon,
        issuer,
        client_id,
        client_secret,
        issuer_external_host,
        username_key,
        user_id_key,
        email_key,
        email_verification_required,
        request_user_info,
        auto_create_status,
        **kwargs,
    )
    if issuer:
        output_entry(ctx, issuer)


@cli.command(name="add-oidc-upstream-provider")
@click.argument("issuer_id", default=None)
@click.argument("name", default=None)
@click.option("--issuer", default=None)
@click.option("--icon", default=None)
@click.option("--client_id", default=None)
@click.option("--client_secret", default=None)
@click.option("--issuer_external_host", default=None)
@click.option("--username_key", default=None)
@click.option("--user_id_key", default=None)
@click.option("--email_key", default=None)
@click.option("--email_verification_required", type=bool, default=None)
@click.option("--request_user_info", type=bool, default=None)
@click.option(
    "--auto_create_status", type=click.Choice(users.STATUS_OPTIONS), default=None
)
@click.option("--org_id", type=str, default=None)
@click.pass_context
def add_oidc_upstream_provider(
    ctx,
    issuer_id=None,
    name=None,
    icon=None,
    issuer=None,
    client_id=None,
    client_secret=None,
    issuer_external_host=None,
    username_key=None,
    user_id_key=None,
    email_key=None,
    email_verification_required=None,
    request_user_info=None,
    auto_create_status=None,
    **kwargs,
):
    issuer = issuers.add_oidc_upstreams(
        ctx,
        issuer_id,
        name,
        icon,
        issuer,
        client_id,
        client_secret,
        issuer_external_host,
        username_key,
        user_id_key,
        email_key,
        email_verification_required,
        request_user_info,
        auto_create_status,
        **kwargs,
    )
    if issuer:
        output_entry(ctx, issuer)


@cli.command(name="delete-oidc-upstream-provider")
@click.argument("issuer_id", default=None)
@click.argument("name", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_oidc_upstream_provider(ctx, issuer_id=None, name=None, **kwargs):
    issuers.delete_oidc_upstreams(ctx, issuer_id, name, **kwargs)


def _format_roles(roles):
    table = PrettyTable(["application", "roles"])
    table.align = "l"
    for k, v in roles.items():
        table.add_row([k, v])
    return table


@cli.command(name="list-elevated-permissions")
@click.option("--user_id", default=None)
@click.option("--limit", default=25, type=int)
@click.pass_context
def list_elevated_permissions(ctx, **kwargs):
    perms = permissions.query(ctx, **kwargs)
    table = PrettyTable(["user_id", "roles"])
    table.align = "l"
    for user_roles in perms:
        table.add_row(
            [
                user_roles.user_id,
                _format_roles(user_roles.roles),
            ]
        )
    print(table)


def _show_elevated_permissions(ctx, user_id, **kwargs):
    perms = permissions.show(ctx, user_id, **kwargs)
    output_entry(ctx, perms.to_dict())


@cli.command(name="show-elevated-permissions")
@click.argument("user_id")
@click.pass_context
def show_elevated_permissions(ctx, user_id, **kwargs):
    _show_elevated_permissions(ctx, user_id, **kwargs)


@cli.command(name="add-elevated-permissions")
@click.argument("user_id")
@click.argument("application")
@click.argument("name")
@click.pass_context
def add_elevated_permissions(ctx, user_id, application, name, **kwargs):
    permissions.add(ctx, user_id, application, name, **kwargs)
    _show_elevated_permissions(ctx, user_id, **kwargs)


@cli.command(name="delete-elevated-permissions")
@click.argument("user_id")
@click.argument("application")
@click.argument("name")
@click.pass_context
def delete_elevated_permissions(ctx, user_id, application, name, **kwargs):
    permissions.delete(ctx, user_id, application, name, **kwargs)
    _show_elevated_permissions(ctx, user_id, **kwargs)


@cli.command(name="clear-elevated-permissions")
@click.argument("user_id")
@click.pass_context
def clear_elevated_permissions(ctx, user_id, **kwargs):
    permissions.clear(ctx, user_id, **kwargs)
    _show_elevated_permissions(ctx, user_id, **kwargs)


@cli.command(name="create-challenge")
@click.argument("user_id")
@click.argument("response_uri")
@click.argument("origin")
@click.option(
    "--challenge-type",
    type=click.Choice(["web_push", "totp", "webauthn"]),
    multiple=True,
)
@click.option("--timeout-seconds", type=int, default=None)
@click.option("--send-now", is_flag=True)
@click.option(
    "--challenge-endpoint",
    type=click.Tuple([str, click.Choice(["web_push", "totp", "webauthn"])]),
    multiple=True,
    help="A pair of strings representing the endpoint id, and endpoint type",
)
@click.pass_context
def create_challenge(ctx, user_id, challenge_type, origin, **kwargs):
    challenge = challenges.create_challenge(
        ctx, user_id, challenge_types=challenge_type, origin=origin, **kwargs
    )
    output_entry(ctx, challenge.to_dict())


@cli.command(name="get-challenge")
@click.argument("challenge_id")
@click.pass_context
def get_challenge(ctx, challenge_id, **kwargs):
    challenge = challenges.get_challenge(ctx, challenge_id, **kwargs)
    output_entry(ctx, challenge.to_dict())


@cli.command(name="answer-challenge")
@click.argument("challenge_id")
@click.argument("challenge_answer")
@click.argument("user_id")
@click.argument("allowed", type=bool)
@click.argument("challenge_type", type=click.Choice(["web_push", "totp", "webauthn"]))
@click.pass_context
def answer_challenge(
    ctx, challenge_id, challenge_answer, user_id, allowed, challenge_type, **kwargs
):
    challenge = challenges.get_challenge_answer(
        ctx, challenge_id, challenge_answer, user_id, allowed, challenge_type, **kwargs
    )
    output_entry(ctx, challenge.to_dict())


@cli.command(name="delete-challenge")
@click.argument("challenge_id")
@click.pass_context
def delete_challenge(ctx, challenge_id, **kwargs):
    challenges.delete_challenge(ctx, challenge_id, **kwargs)


@cli.command(name="replace-challenge")
@click.argument("challenge_id")
@click.option("--send-now", is_flag=True)
@click.pass_context
def replace_challenge(ctx, challenge_id, **kwargs):
    challenge = challenges.replace_challenge(ctx, challenge_id, **kwargs)
    output_entry(ctx, challenge.to_dict())


@cli.command(name="create-challenge-enrollment")
@click.argument("user_id")
@click.pass_context
def create_challenge_enrollment(ctx, user_id, **kwargs):
    challenge_enrollment = challenges.create_challenge_enrollment(ctx, user_id, **kwargs)
    output_entry(ctx, challenge_enrollment.to_dict())


@cli.command(name="get-challenge-enrollment")
@click.argument("enrollment_id")
@click.option("--user-id")
@click.pass_context
def get_challenge_enrollment(ctx, enrollment_id, **kwargs):
    challenge_enrollment = challenges.get_challenge_enrollment(
        ctx, enrollment_id, **kwargs
    )
    output_entry(ctx, challenge_enrollment.to_dict())


@cli.command(name="delete-challenge-enrollment")
@click.argument("enrollment_id")
@click.option("--user-id")
@click.pass_context
def delete_challenge_enrollment(ctx, enrollment_id, **kwargs):
    challenges.delete_challenge_enrollment(ctx, enrollment_id, **kwargs)


@cli.command(name="update-challenge-enrollment")
@click.argument("enrollment_id")
@click.argument("user_id")
@click.argument("answer")
@click.pass_context
def update_challenge_enrollment(ctx, enrollment_id, user_id, answer, **kwargs):
    result = challenges.update_challenge_enrollment(
        ctx, enrollment_id, user_id, answer, **kwargs
    )
    output_entry(ctx, result.to_dict())


@cli.command(name="list-combined-user-details")
@click.option("--organisation", default=None)
@click.option("--org_id", default=None)
@click.option("--user_id", default=None)
@click.option("--email", default=None)
@click.option("--previous_email", default=None)
@click.option("--limit", type=int, default=None)
@click.option("--mfa_enrolled", type=bool, default=None)
@click.option("--auto_created", type=bool, default=None)
@click.option(
    "--status", multiple=True, type=click.Choice(users.STATUS_OPTIONS), default=None
)
@click.option(
    "--search_direction",
    default="forwards",
    type=click.Choice(["forwards", "backwards"]),
)
@click.pass_context
def list_combined_user_details(ctx, organisation, org_id, **kwargs):
    # get all orgs
    org_by_id, org_by_name = orgs.get_org_by_dictionary(ctx, org_id)
    org_id = get_org_id(ctx, org_name=organisation, org_id=org_id)

    results = users.list_combined_user_details(ctx, org_id=org_id, **kwargs)
    print(users.format_combined_user_details_as_text(results))


@cli.command(name="list-totp-enrollments")
@click.option("--user_id", default=None)
@click.option("--limit", type=int, default=500)
@click.pass_context
def list_totp_enrollments(ctx, **kwargs):
    results = challenges.list_totp_enrollments(ctx, **kwargs)
    print(challenges.format_totp_enrollments(results))


@cli.command(name="list-webauthn-enrollments")
@click.option("--user_id", default=None)
@click.option("--limit", type=int, default=500)
@click.pass_context
def list_webauthn_enrollments(ctx, **kwargs):
    results = challenges.list_webauthn_enrollments(ctx, **kwargs)
    print(challenges.format_webauthn_enrollments(results))


@cli.command(name="get-message-endpoint")
@click.argument("message_endpoint_id")
@click.option("--user_id", default=None)
@click.pass_context
def get_message_endpoint(ctx, **kwargs):
    result = messages.get_message_endpoint(ctx, **kwargs)
    print(result)


@cli.command(name="list-message-endpoints")
@click.option("--user_id", default=None)
@click.option("--limit", type=int, default=500)
@click.pass_context
def list_message_endpoints(ctx, **kwargs):
    results = messages.list_message_endpoints(ctx, **kwargs)
    print(messages.format_message_endpoints(results))


@cli.command(name="delete-message-endpoint")
@click.argument("message_endpoint_id")
@click.option("--user-id")
@click.pass_context
def delete_message_endpoint(ctx, message_endpoint_id, **kwargs):
    messages.delete_message_endpoint(ctx, message_endpoint_id, **kwargs)


@cli.command(name="list-upstream-user-identities")
@click.option("--user-id", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_upstream_user_identities(ctx, user_id, **kwargs):
    ids = users.list_upstream_user_identities(ctx, user_id, **kwargs)
    table = users.format_upstream_user_identities_as_text(ids)
    print(table)


@cli.command(name="add-upstream-user-identity")
@click.argument("upstream-user-id")
@click.argument("upstream-idp-id")
@click.option("--user-id", default=None)
@click.pass_context
def add_upstream_user_identity(ctx, user_id, **kwargs):
    result = users.add_upstream_user_identity(ctx, user_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="update-upstream-user-identity")
@click.argument("upstream-user-identity-id")
@click.option("--upstream-user-id", default=None)
@click.option("--upstream-idp-id", default=None)
@click.option("--user-id", default=None)
@click.pass_context
def update_upstream_user_identity(ctx, upstream_user_identity_id, user_id, **kwargs):
    result = users.update_upstream_user_identity(
        ctx, upstream_user_identity_id, user_id, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="show-upstream-user-identity")
@click.argument("upstream-user-identity-id")
@click.option("--user-id", default=None)
@click.pass_context
def show_upstream_user_identity(ctx, user_id, upstream_user_identity_id, **kwargs):
    result = users.show_upstream_user_identity(
        ctx, upstream_user_identity_id, user_id, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="delete-upstream-user-identity")
@click.argument("upstream-user-identity-id")
@click.option("--user-id", default=None)
@click.pass_context
def delete_upstream_user_identity(ctx, user_id, upstream_user_identity_id, **kwargs):
    users.delete_upstream_user_identity(
        ctx, upstream_user_identity_id, user_id, **kwargs
    )


@cli.command(name="list-user-requests")
@click.option("--user-id", default=None)
@click.option("--org-id", default=None)
@click.option("--request_type", default=None)
@click.option("--request_state", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_user_requests(ctx, **kwargs):
    ids = users.list_user_requests(ctx, **kwargs)
    table = users.format_user_requests_as_text(ids)
    print(table)


@cli.command(name="add-user-request")
@click.argument("user-id")
@click.argument("org-id")
@click.argument("requested_resource")
@click.argument("requested_resource_type", type=click.Choice(["application_access"]))
@click.option("--request_information", default=None)
@click.option("--requested_sub_resource", type=str, default=None)
@click.pass_context
def add_user_request(
    ctx, user_id, org_id, requested_resource, requested_resource_type, **kwargs
):
    result = users.add_user_request(
        ctx, user_id, org_id, requested_resource, requested_resource_type, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="update-user-request")
@click.argument("user-request-id")
@click.option("--org_id", default=None)
@click.option("--requested_resource", default=None)
@click.option("--requested_sub_resource", type=str, default=None)
@click.option(
    "--requested_resource_type", type=click.Choice(["application_access"]), default=None
)
@click.option("--request_information", default=None)
@click.pass_context
def update_user_request(ctx, user_request_id, **kwargs):
    result = users.update_user_request(ctx, user_request_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="action-user-request")
@click.argument("user-request-id")
@click.argument("state", type=click.Choice(["approved", "declined"]))
@click.option("--org_id", default=None)
@click.option("--requested_resource", default=None)
@click.option(
    "--requested_resource_type", type=click.Choice(["application_access"]), default=None
)
@click.option("--request_information", default=None)
@click.pass_context
def action_user_request(ctx, user_request_id, state, **kwargs):
    result = users.action_user_request(ctx, user_request_id, state, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-user-request")
@click.argument("user-request-id")
@click.option("--user-id", default=None)
@click.pass_context
def show_user_request(ctx, user_request_id, **kwargs):
    result = users.show_user_request(ctx, user_request_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-user-request")
@click.argument("user-request-id")
@click.option("--user-id", default=None)
@click.pass_context
def delete_user_request(ctx, user_request_id, **kwargs):
    users.delete_user_request(ctx, user_request_id, **kwargs)


@cli.command(name="list-access-requests")
@click.option("--org_id", default=None)
@click.option("--user_id", default=None)
@click.option("--request_type", default=None)
@click.option("--request_state", default=None)
@click.option("--limit", default=500)
@click.option("--email", default=None)
@click.option(
    "--search_direction",
    default="forwards",
    type=click.Choice(["forwards", "backwards"]),
)
@click.pass_context
def list_access_requests(ctx, org_id, **kwargs):
    requests_list = users.list_access_requests(ctx, org_id, **kwargs)
    table = PrettyTable(
        [
            "id",
            "email",
            "org_id",
            "user_status",
            "user_requests",
        ]
    )
    for entry in requests_list:
        table.add_row(
            [
                entry.metadata.id,
                entry.status.user.email,
                entry.status.user.org_id,
                entry.status.user.status,
                entry.status.user_requests,
            ]
        )
    table.align = "l"
    print(table)


@cli.command(name="version")
@click.pass_context
def version(ctx):
    print(__version__)


@cli.command(name="upload-upstream-user-identity-list")
@click.argument("org-id")
@click.argument("upstream_user_idp_id")
@click.argument("email-to-id-mapping")
@click.pass_context
def upload_upstream_user_identity_list(
    ctx, org_id, upstream_user_idp_id, email_to_id_mapping
):
    """
    Updates the upstream identity for many users. This command takes a csv file as
    input as the email-to-id-mapping argument. If the argument is '-', the file will
    be read from stdin. The file must be csv formatted, containing a mapping between
    email address and upstream user id. The file must start with a header with
    "email" and "upstream_user_id" for the two columns.

    Example:

    "email","upstream_user_id"

    "foo@example.com","1234-4567"

    "bar@example.com","5023-1235"
    """
    users.upload_upstream_user_identity_list(
        ctx, org_id, upstream_user_idp_id, email_to_id_mapping
    )


@cli.command(name="list-user-application-access-info")
@click.option("--user", default=None)
@click.option("--org-id", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_user_application_access_info(ctx, user, org_id, **kwargs):
    user_id = user_id_or_id_from_email(ctx, user_id_or_email=user, org_id=org_id)
    info = users.list_user_application_access_info(ctx, user_id, org_id=org_id, **kwargs)
    table = users.format_user_application_access_info_as_text(info)
    print(table)


@cli.command(name="list-application-summaries")
@click.option("--org-id", default=None)
@click.option("--assigned-org-id", multiple=True, default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_application_summaries(ctx, org_id, assigned_org_id, **kwargs):
    summaries = apps.list_application_summaries(
        ctx, org_id=org_id, assigned_org_ids=assigned_org_id, **kwargs
    )
    table = apps.format_application_summaries_as_text(summaries)
    print(table)


@cli.command(name="list-auth-policies")
@click.option("--org-id", default=None)
@click.option("--limit", default=500)
@click.option("--policy-name", default=None)
@click.pass_context
def list_auth_policies(ctx, **kwargs):
    policies = issuers.list_auth_policies(ctx, **kwargs)
    print(issuers.format_policy_table(policies))


@cli.command(name="list-auth-policy-rules")
@click.option("--org-id", default=None)
@click.option("--limit", default=500)
@click.option("--policy-name", default=None)
@click.pass_context
def list_auth_policy_rules(ctx, **kwargs):
    policies = issuers.list_auth_policies(ctx, **kwargs)
    print(issuers.format_policy_rules_table(policies))


@cli.command(name="add-auth-policy")
@click.argument("issuer_id")
@click.argument(
    "default_action",
    type=click.Choice(["do_mfa", "deny_login", "allow_login", "dont_mfa"]),
)
@click.argument(
    "supported_mfa_methods",
    type=click.Choice(["web_push", "totp", "webauthn"]),
    nargs=-1,
)
@click.option("--org-id", default=None)
@click.option("--name", default=None)
@click.pass_context
def add_auth_policy(ctx, issuer_id, default_action, supported_mfa_methods, **kwargs):
    result = issuers.add_auth_policy(
        ctx, issuer_id, default_action, supported_mfa_methods, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="update-auth-policy")
@click.argument("policy-id")
@click.option(
    "--default-action",
    type=click.Choice(["do_mfa", "deny_login", "allow_login", "dont_mfa"]),
)
@click.option("--issuer-id", default=None)
@click.option("--org-id", default=None)
@click.option("--name", default=None)
@click.option(
    "--supported_mfa_methods",
    type=click.Choice(["web_push", "totp", "webauthn"]),
    multiple=True,
)
@click.pass_context
def update_auth_policy(ctx, policy_id, **kwargs):
    result = issuers.update_auth_policy(ctx, policy_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-auth-policy")
@click.argument("policy-id")
@click.option("--org-id", default=None)
@click.pass_context
def get_auth_policy(ctx, policy_id, **kwargs):
    result = issuers.get_auth_policy(ctx, policy_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-auth-policy")
@click.argument("policy-id")
@click.option("--org-id", default=None)
@click.pass_context
def delete_auth_policy(ctx, policy_id, **kwargs):
    issuers.delete_auth_policy(ctx, policy_id, **kwargs)


@cli.command(name="add-auth-policy-rule")
@click.argument("policy_id")
@click.argument("action")
@click.option("--name", default=None)
@click.option("--org-id", default=None)
@click.pass_context
def add_auth_policy_rule(ctx, policy_id, action, **kwargs):
    result = issuers.add_auth_policy_rule(ctx, policy_id, action, **kwargs)
    output_entry(ctx, result)


@cli.command(name="update-auth-policy-rule")
@click.argument("policy_id")
@click.argument("policy_rule_id")
@click.option("--action")
@click.option("--name", default=None)
@click.option("--org-id", default=None)
@click.pass_context
def update_auth_policy_rule(ctx, policy_id, policy_rule_id, **kwargs):
    result = issuers.update_auth_policy_rule(ctx, policy_id, policy_rule_id, **kwargs)
    output_entry(ctx, result)


def convert_condition_value(value_type, value):
    if value_type == "bool":
        str_val = value[0]
        if str_val.lower() == "true":
            return json.dumps(True)
        elif str_val.lower() == "false":
            return json.dumps(False)
        raise ValueError
    if value_type == "int":
        return json.dumps(int(value[0]))
    if value_type == "str":
        return json.dumps(str(value[0]))
    if value_type == "list":
        return json.dumps(list(value))
    raise ValueError(f"value_type {value_type} not known")


@cli.command(name="add-auth-policy-conditions")
@click.argument("policy_id")
@click.argument("policy_rule_id")
@click.argument("condition_type")
@click.argument(
    "condition_value_type", type=click.Choice(["bool", "int", "str", "list"])
)
@click.argument("condition_value", nargs=-1)
@click.option("--operator", default=None)
@click.option("--field", default=None)
@click.option("--org-id", default=None)
@click.pass_context
def add_auth_policy_condition(
    ctx,
    policy_id,
    policy_rule_id,
    condition_type,
    condition_value_type,
    condition_value,
    **kwargs,
):
    value = convert_condition_value(condition_value_type, condition_value)
    result = issuers.add_auth_policy_condition(
        ctx, policy_id, policy_rule_id, condition_type, value=value, **kwargs
    )
    output_entry(ctx, result)


@cli.command(name="delete-auth-policy-conditions")
@click.argument("policy_id")
@click.argument("policy_rule_id")
@click.argument("condition_type")
@click.pass_context
def delete_auth_policy_condition(ctx, policy_id, policy_rule_id, **kwargs):
    issuers.delete_auth_policy_condition(ctx, policy_id, policy_rule_id, **kwargs)


@cli.command(name="show-auth-policy-rule")
@click.argument("policy_id")
@click.argument("policy_rule_id")
@click.pass_context
def get_auth_policy_rule(ctx, policy_id, policy_rule_id, **kwargs):
    result = issuers.get_auth_policy_rule(ctx, policy_id, policy_rule_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-auth-policy-rule")
@click.argument("policy_id")
@click.argument("policy_rule_id")
@click.pass_context
def delete_auth_policy_rule(ctx, policy_id, policy_rule_id, **kwargs):
    issuers.delete_auth_policy_rule(ctx, policy_id, policy_rule_id, **kwargs)


@cli.command(name="add-auth-policy-group")
@click.argument("policy_id")
@click.option("--name")
@click.option("--rule-id", multiple=True, default=[])
@click.option("--org-id", default=None)
@click.option(
    "--insertion-index",
    type=int,
    help="""The index to insert this group at.
         If not set the group will be added to the end""",
    default=None,
)
@click.pass_context
def add_auth_policy_group(
    ctx,
    policy_id,
    **kwargs,
):
    kwargs["rule_ids"] = kwargs.pop("rule_id", [])
    result = issuers.add_auth_policy_group(ctx, policy_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-auth-policy-group")
@click.argument("policy_id")
@click.argument("policy_group_id")
@click.option("--org-id", default=None)
@click.pass_context
def delete_auth_policy_group(ctx, policy_id, policy_group_id, **kwargs):
    issuers.delete_auth_policy_group(ctx, policy_id, policy_group_id, **kwargs)


@cli.command(name="list-user-metadata")
@click.option("--user_id", default=None)
@click.option("--org_id", default=None)
@click.option("--data_type", default=None)
@click.option("--app_id", default=None)
@click.option("--limit", default=500)
@click.pass_context
def list_user_metadata(ctx, **kwargs):
    ids = users.list_user_metadata(ctx, **kwargs)
    table = users.format_user_metadata_as_text(ids)
    print(table)


@cli.command(name="add-user-metadata")
@click.argument("user_id")
@click.argument("org_id")
@click.argument(
    "data_type",
    type=click.Choice(["mfa_enrollment_expiry", "user_app_data", "user_org_data"]),
)
@click.argument("data")
@click.option(
    "--app_id",
    default=None,
    help="excluding the app_id will be interpretted as an organisation level metadata setting",  # noqa
)
@click.option("--name", default=None)
@click.pass_context
def add_user_metadata(ctx, user_id, org_id, data_type, data, **kwargs):
    result = users.add_user_metadata(ctx, user_id, org_id, data_type, data, **kwargs)
    output_entry(ctx, result)


@cli.command(name="update-user-metadata")
@click.argument("user-metadata-id")
@click.option("--org_id", default=None)
@click.option("--user_id", default=None)
@click.option(
    "--data_type",
    type=click.Choice(["mfa_enrollment_expiry", "user_app_data", "user_org_data"]),
)
@click.option("--data")
@click.option("--app_id", default=None)
@click.option("--name", default=None)
@click.pass_context
def update_user_metadata(ctx, user_metadata_id, **kwargs):
    result = users.update_user_metadata(ctx, user_metadata_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="show-user-metadata")
@click.argument("user-metadata-id")
@click.option("--user_id", default=None)
@click.pass_context
def show_user_metadata(ctx, user_metadata_id, **kwargs):
    result = users.show_user_metadata(ctx, user_metadata_id, **kwargs)
    output_entry(ctx, result)


@cli.command(name="delete-user-metadata")
@click.argument("user-metadata-id")
@click.option("--user_id", default=None)
@click.option("--org_id", default=None)
@click.pass_context
def delete_user_metadata(ctx, user_metadata_id, **kwargs):
    users.delete_user_metadata(ctx, user_metadata_id, **kwargs)


@cli.command(name="bulk-set-metadata")
@click.argument("org_id")
@click.argument(
    "data_type",
    type=click.Choice(["mfa_enrollment_expiry", "user_app_data", "user_org_data"]),
)
@click.argument("data")
@click.option("--app_id", default=None)
@click.option("--name", default=None)
@click.pass_context
def bulk_set_user_metadata(ctx, org_id, data_type, data, **kwargs):
    users.bulk_set_user_metadata(ctx, org_id, data_type, data, **kwargs)


def main():
    cli(auto_envvar_prefix="AGILICUS")


if __name__ == "__main__":
    main()
