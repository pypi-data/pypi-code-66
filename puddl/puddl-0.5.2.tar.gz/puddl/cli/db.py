import logging
import subprocess

import click

from puddl import get_config

log = logging.getLogger(__name__)


@click.group()
def db():
    pass


@db.command()
def health():
    conf = get_config()

    import psycopg2
    # consumes PG* env vars
    connection = psycopg2.connect(conf.db_url)
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
    log.info('database available')


@db.command()
@click.option('--app')
def shell(app):
    if app is None:
        db_env = get_config(app='db shell').db_env
    else:
        from puddl.db.alchemy import App
        db_env = App(app).db_config.to_dict()
    # want to see good error handling for this kind of thing?
    # https://github.com/pallets/click/blob/19fdc8509a1b946c088512e0e5e388a8d012f0ce/src/click/_termui_impl.py#L472-L487
    subprocess.Popen('psql', env=db_env).wait()


@db.command()
@click.option('--app')
def url(app):
    """
    print DB URL

    Useful for things like this:

        from sqlalchemy import create_engine
        database_url = 'postgresql://puddl:aey1Ki4oaZohseWod2ri@localhost:13370/puddl'
        engine = create_engine(database_url, echo=False)
        df.to_sql('bp', engine)
    """
    conf = get_config(app=app)
    print(conf.db_url)


@db.command()
def env():
    """
    Prints the database's environment.
    WARNING: This dumps your password. Use it like this:

        source <(puddl db env)
    """
    conf = get_config()
    for k, v in conf.db_env.items():
        print(f'export {k}={v}')


@db.command()
def sessions():
    """
    Lists active sessions.
    """
    conf = get_config(app='db sessions')
    query = """SELECT pid AS process_id,
           usename AS username,
           datname AS database_name,
           client_addr AS client_address,
           application_name,
           backend_start,
           state,
           state_change
    FROM pg_stat_activity;"""
    click.echo(
        subprocess.check_output(['psql', '-c', query], encoding='utf-8', env=conf.db_env))


@db.command()
def queries():
    print('xxx')
