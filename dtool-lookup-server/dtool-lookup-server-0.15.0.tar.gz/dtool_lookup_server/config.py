import os

import dtool_lookup_server

_HERE = os.path.abspath(os.path.dirname(__file__))


def _get_file_content(key, default=""):
    file_path = os.environ.get(key, "")
    if os.path.isfile(file_path):
        content = open(file_path).read()
    else:
        content = ""
    return content


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///{}'.format(os.path.join(_HERE, "..", 'app.db'))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = os.environ.get(
        'MONGO_URI',
        'mongodb://localhost:27017/dtool_info'
    )
    JWT_ALGORITHM = "RS256"
    JWT_TOKEN_LOCATION = "headers"
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"

    # Logic to give "JWT_PUBLIC_KEY" priority over "JWT_PUBLIC_KEY_FILE".
    # This is used when making use of JWT tokens generated by another service.
    # Hence there is no need for the JWT_PRIVATE_KEY_FILE.
    if os.environ.get("JWT_PUBLIC_KEY"):
        JWT_PUBLIC_KEY = os.environ.get("JWT_PUBLIC_KEY")
    else:
        JWT_PRIVATE_KEY = _get_file_content("JWT_PRIVATE_KEY_FILE")
        JWT_PUBLIC_KEY = _get_file_content("JWT_PUBLIC_KEY_FILE")

    JSONIFY_PRETTYPRINT_REGULAR = True

    @classmethod
    def to_dict(cls):
        """Convert server configuration into dict."""
        exclusions = [
            'JWT_PRIVATE_KEY',
            'MONGO_URI',
            'SECRET_KEY',
            'SQLALCHEMY_DATABASE_URI',
        ]  # config keys to exclude
        d = {'version': dtool_lookup_server.__version__}
        for k, v in cls.__dict__.items():
            # select only capitalized fields
            if k.upper() == k and k not in exclusions:
                d[k.lower()] = v
        return d
