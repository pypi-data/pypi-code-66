##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2020, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

"""Defines the models for the configuration database.

If any of the models are updated, you (yes, you, the developer) MUST do two
things:

1) Increment SCHEMA_VERSION below

2) Create an Alembic migratio to ensure that the appropriate changes are
   made to the config database to upgrade it to the new version.
"""

from flask_security import UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy

##########################################################################
#
# The schema version is used to track when upgrades are needed to the
# configuration database. Increment this whenever changes are made to the
# model or data, AND ensure the upgrade code is added to setup.py
#
##########################################################################

SCHEMA_VERSION = 27

##########################################################################
#
# And now we return to our regularly scheduled programming:
#
##########################################################################

db = SQLAlchemy()
USER_ID = 'user.id'

# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey(USER_ID)),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Version(db.Model):
    """Version numbers for reference/upgrade purposes"""
    __tablename__ = 'version'
    name = db.Column(db.String(32), primary_key=True)
    value = db.Column(db.Integer(), nullable=False)


class Role(db.Model, RoleMixin):
    """Define a security role"""
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(256), nullable=False)


class User(db.Model, UserMixin):
    """Define a user object"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256))
    active = db.Column(db.Boolean(), nullable=False)
    confirmed_at = db.Column(db.DateTime())
    masterpass_check = db.Column(db.String(256))
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    auth_source = db.Column(db.String(16), unique=True, nullable=False)


class Setting(db.Model):
    """Define a setting object"""
    __tablename__ = 'setting'
    user_id = db.Column(db.Integer, db.ForeignKey(USER_ID), primary_key=True)
    setting = db.Column(db.String(256), primary_key=True)
    value = db.Column(db.String(1024))


class ServerGroup(db.Model):
    """Define a server group for the treeview"""
    __tablename__ = 'servergroup'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(USER_ID), nullable=False)

    name = db.Column(db.String(128), nullable=False)
    __table_args__ = (db.UniqueConstraint('user_id', 'name'),)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
        }


class Server(db.Model):
    """Define a registered Postgres server"""
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(USER_ID),
        nullable=False
    )
    servergroup_id = db.Column(
        db.Integer,
        db.ForeignKey('servergroup.id'),
        nullable=False
    )
    name = db.Column(db.String(128), nullable=False)
    host = db.Column(db.String(128), nullable=True)
    hostaddr = db.Column(db.String(128), nullable=True)
    port = db.Column(
        db.Integer(),
        db.CheckConstraint('port >= 1 AND port <= 65534'),
        nullable=False)
    maintenance_db = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=True)
    save_password = db.Column(
        db.Integer(),
        db.CheckConstraint('save_password >= 0 AND save_password <= 1'),
        nullable=False
    )
    role = db.Column(db.String(64), nullable=True)
    ssl_mode = db.Column(
        db.String(16),
        db.CheckConstraint(
            "ssl_mode IN ('allow', 'prefer', 'require', 'disable', "
            "'verify-ca', 'verify-full')"
        ),
        nullable=False)
    comment = db.Column(db.String(1024), nullable=True)
    discovery_id = db.Column(db.String(128), nullable=True)
    servers = db.relationship(
        'ServerGroup',
        backref=db.backref('server', cascade="all, delete-orphan"),
        lazy='joined'
    )
    db_res = db.Column(db.Text(), nullable=True)
    passfile = db.Column(db.Text(), nullable=True)
    sslcert = db.Column(db.Text(), nullable=True)
    sslkey = db.Column(db.Text(), nullable=True)
    sslrootcert = db.Column(db.Text(), nullable=True)
    sslcrl = db.Column(db.Text(), nullable=True)
    sslcompression = db.Column(
        db.Integer(),
        db.CheckConstraint('sslcompression >= 0 AND sslcompression <= 1'),
        nullable=False
    )
    bgcolor = db.Column(db.Text(10), nullable=True)
    fgcolor = db.Column(db.Text(10), nullable=True)
    service = db.Column(db.Text(), nullable=True)
    connect_timeout = db.Column(db.Integer(), nullable=False)
    use_ssh_tunnel = db.Column(
        db.Integer(),
        db.CheckConstraint('use_ssh_tunnel >= 0 AND use_ssh_tunnel <= 1'),
        nullable=False
    )
    tunnel_host = db.Column(db.String(128), nullable=True)
    tunnel_port = db.Column(
        db.Integer(),
        db.CheckConstraint('port <= 65534'),
        nullable=True)
    tunnel_username = db.Column(db.String(64), nullable=True)
    tunnel_authentication = db.Column(
        db.Integer(),
        db.CheckConstraint('tunnel_authentication >= 0 AND '
                           'tunnel_authentication <= 1'),
        nullable=False
    )
    tunnel_identity_file = db.Column(db.String(64), nullable=True)
    tunnel_password = db.Column(db.String(64), nullable=True)
    shared = db.Column(db.Boolean(), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "servergroup_id": self.servergroup_id,
            "name": self.name,
            "host": self.host,
            "hostaddr": self.hostaddr,
            "port": self.port,
            "maintenance_db": self.maintenance_db,
            "username": self.username,
            "password": self.password,
            "save_password": self.save_password,
            "role": self.role,
            "ssl_mode": self.ssl_mode,
            "comment": self.comment,
            "discovery_id": self.discovery_id,
            "db_res": self.db_res,
            "passfile": self.passfile,
            "sslcert": self.sslcert,
            "sslkey": self.sslkey,
            "sslrootcert": self.sslrootcert,
            "sslcrl": self.sslcrl,
            "sslcompression": self.sslcompression,
            "bgcolor": self.bgcolor,
            "fgcolor": self.fgcolor,
            "service": self.service,
            "connect_timeout": self.connect_timeout,
            "use_ssh_tunnel": self.use_ssh_tunnel,
            "tunnel_host": self.tunnel_host,
            "tunnel_port": self.tunnel_port,
            "tunnel_authentication": self.tunnel_authentication,
            "tunnel_identity_file": self.tunnel_identity_file,
            "tunnel_password": self.tunnel_password
        }


class ModulePreference(db.Model):
    """Define a preferences table for any modules."""
    __tablename__ = 'module_preference'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)


class PreferenceCategory(db.Model):
    """Define a preferences category for each modules."""
    __tablename__ = 'preference_category'
    id = db.Column(db.Integer, primary_key=True)
    mid = db.Column(
        db.Integer,
        db.ForeignKey('module_preference.id'),
        nullable=False
    )
    name = db.Column(db.String(256), nullable=False)


class Preferences(db.Model):
    """Define a particular preference."""
    __tablename__ = 'preferences'
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(
        db.Integer,
        db.ForeignKey('preference_category.id'),
        nullable=False
    )
    name = db.Column(db.String(1024), nullable=False)


class UserPreference(db.Model):
    """Define the preference for a particular user."""
    __tablename__ = 'user_preferences'
    pid = db.Column(
        db.Integer, db.ForeignKey('preferences.id'), primary_key=True
    )
    uid = db.Column(
        db.Integer, db.ForeignKey(USER_ID), primary_key=True
    )
    value = db.Column(db.String(1024), nullable=False)


class DebuggerFunctionArguments(db.Model):
    """Define the debugger input function arguments."""
    __tablename__ = 'debugger_function_arguments'
    server_id = db.Column(db.Integer(), nullable=False, primary_key=True)
    database_id = db.Column(db.Integer(), nullable=False, primary_key=True)
    schema_id = db.Column(db.Integer(), nullable=False, primary_key=True)
    function_id = db.Column(db.Integer(), nullable=False, primary_key=True)
    arg_id = db.Column(db.Integer(), nullable=False, primary_key=True)
    is_null = db.Column(
        db.Integer(),
        db.CheckConstraint('is_null >= 0 AND is_null <= 1'),
        nullable=False
    )
    is_expression = db.Column(
        db.Integer(),
        db.CheckConstraint(
            'is_expression >= 0 AND is_expression <= 1'
        ),
        nullable=False
    )
    use_default = db.Column(
        db.Integer(),
        db.CheckConstraint(
            'use_default >= 0 AND use_default <= 1'
        ),
        nullable=False
    )

    value = db.Column(db.String(), nullable=True)


class Process(db.Model):
    """Define the Process table."""
    __tablename__ = 'process'
    pid = db.Column(db.String(), nullable=False, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(USER_ID),
        nullable=False
    )
    command = db.Column(db.String(), nullable=False)
    desc = db.Column(db.String(), nullable=False)
    arguments = db.Column(db.String(), nullable=True)
    logdir = db.Column(db.String(), nullable=True)
    start_time = db.Column(db.String(), nullable=True)
    end_time = db.Column(db.String(), nullable=True)
    exit_code = db.Column(db.Integer(), nullable=True)
    acknowledge = db.Column(db.String(), nullable=True)
    utility_pid = db.Column(db.Integer, nullable=False)
    process_state = db.Column(db.Integer, nullable=False)


class Keys(db.Model):
    """Define the keys table."""
    __tablename__ = 'keys'
    name = db.Column(db.String(), nullable=False, primary_key=True)
    value = db.Column(db.String(), nullable=False)


class QueryHistoryModel(db.Model):
    """Define the history SQL table."""
    __tablename__ = 'query_history'
    srno = db.Column(db.Integer(), nullable=False, primary_key=True)
    uid = db.Column(
        db.Integer, db.ForeignKey(USER_ID), nullable=False, primary_key=True
    )
    sid = db.Column(
        db.Integer(), db.ForeignKey('server.id'), nullable=False,
        primary_key=True)
    dbname = db.Column(db.String(), nullable=False, primary_key=True)
    query_info = db.Column(db.String(), nullable=False)
    last_updated_flag = db.Column(db.String(), nullable=False)


class Database(db.Model):
    """
    Define a Database.
    """
    __tablename__ = 'database'
    id = db.Column(db.Integer, primary_key=True)
    schema_res = db.Column(db.String(256), nullable=True)
    server = db.Column(
        db.Integer,
        db.ForeignKey('server.id'),
        nullable=False,
        primary_key=True
    )


class SharedServer(db.Model):
    """Define a shared Postgres server"""

    __tablename__ = 'sharedserver'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(USER_ID)
    )
    server_owner = db.Column(
        db.String(128),
        db.ForeignKey('user.username')
    )
    servergroup_id = db.Column(
        db.Integer,
        db.ForeignKey('servergroup.id'),
        nullable=False
    )
    name = db.Column(db.String(128), nullable=False)
    host = db.Column(db.String(128), nullable=True)
    hostaddr = db.Column(db.String(128), nullable=True)
    port = db.Column(
        db.Integer(),
        db.CheckConstraint('port >= 1 AND port <= 65534'),
        nullable=False)
    maintenance_db = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=True)
    save_password = db.Column(
        db.Integer(),
        db.CheckConstraint('save_password >= 0 AND save_password <= 1'),
        nullable=False
    )
    role = db.Column(db.String(64), nullable=True)
    ssl_mode = db.Column(
        db.String(16),
        db.CheckConstraint(
            "ssl_mode IN ('allow', 'prefer', 'require', 'disable', "
            "'verify-ca', 'verify-full')"
        ),
        nullable=False)
    comment = db.Column(db.String(1024), nullable=True)
    discovery_id = db.Column(db.String(128), nullable=True)
    servers = db.relationship(
        'ServerGroup',
        backref=db.backref('sharedserver', cascade="all, delete-orphan"),
        lazy='joined'
    )
    db_res = db.Column(db.Text(), nullable=True)
    passfile = db.Column(db.Text(), nullable=True)
    sslcert = db.Column(db.Text(), nullable=True)
    sslkey = db.Column(db.Text(), nullable=True)
    sslrootcert = db.Column(db.Text(), nullable=True)
    sslcrl = db.Column(db.Text(), nullable=True)
    sslcompression = db.Column(
        db.Integer(),
        db.CheckConstraint('sslcompression >= 0 AND sslcompression <= 1'),
        nullable=False
    )
    bgcolor = db.Column(db.Text(10), nullable=True)
    fgcolor = db.Column(db.Text(10), nullable=True)
    service = db.Column(db.Text(), nullable=True)
    connect_timeout = db.Column(db.Integer(), nullable=False)
    use_ssh_tunnel = db.Column(
        db.Integer(),
        db.CheckConstraint('use_ssh_tunnel >= 0 AND use_ssh_tunnel <= 1'),
        nullable=False
    )
    tunnel_host = db.Column(db.String(128), nullable=True)
    tunnel_port = db.Column(
        db.Integer(),
        db.CheckConstraint('port <= 65534'),
        nullable=True)
    tunnel_username = db.Column(db.String(64), nullable=True)
    tunnel_authentication = db.Column(
        db.Integer(),
        db.CheckConstraint('tunnel_authentication >= 0 AND '
                           'tunnel_authentication <= 1'),
        nullable=False
    )
    tunnel_identity_file = db.Column(db.String(64), nullable=True)
    tunnel_password = db.Column(db.String(64), nullable=True)
    shared = db.Column(db.Boolean(), nullable=False)


class Macros(db.Model):
    """Define a particular macro."""
    __tablename__ = 'macros'
    id = db.Column(db.Integer, primary_key=True)
    alt = db.Column(db.Boolean(), nullable=False)
    control = db.Column(db.Boolean(), nullable=False)
    key = db.Column(db.String(32), nullable=False)
    key_code = db.Column(db.Integer, nullable=False)


class UserMacros(db.Model):
    """Define the macro for a particular user."""
    __tablename__ = 'user_macros'
    mid = db.Column(
        db.Integer, db.ForeignKey('macros.id'), primary_key=True
    )
    uid = db.Column(
        db.Integer, db.ForeignKey(USER_ID), primary_key=True
    )
    name = db.Column(db.String(1024), nullable=False)
    sql = db.Column(db.Text(), nullable=False)
