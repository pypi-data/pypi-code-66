
from channeling.config import ChannelingConfig

import json
import os
import sqlite3
import time

conf = ChannelingConfig()

class Database():

    type = None

    def __init__(self):
        self.type = conf.database_type
        self.connection = None
        self.cursor = None
        conf.logger.debug(json.dumps({
            'timestamp': str(time.time()),
            'type': 'db',
            'content': 'Initialized database object: {}'.format(self.type)
            }))

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        if self.type == "sqlite3":
            conn = sqlite3.connect(os.path.expanduser(conf.database_path))
            return conn
        raise "Missing or unknown database type."

    def __enter__(self):
        conf.logger.debug(json.dumps({
            'timestamp': str(time.time()),
            'type': 'db',
            'content': 'Creating connection.'
            }))
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, tb):
        conf.logger.debug(json.dumps({
            'timestamp': str(time.time()),
            'type': 'db',
            'content': 'Commiting and closing connection.'
            }))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type is not None:
            return False
        return True

