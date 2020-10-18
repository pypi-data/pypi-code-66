
import ibm_boto3

import ibm_db
from ibm_botocore.client import Config
from ibm_botocore.exceptions import ClientError

from bizai.framework.decorators.validate import validate_input
from bizai.framework.persistence.persistencevolume import DBPersistenceVolume


class DB2PersistenceVolume (DBPersistenceVolume):

    schema_connect = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Schema for connect",
        "type": "object",
        "properties": {
                "DATABASE": {type: "string"},
                "HOSTNAME": {type: "string"},
                "PORT": {type: "integer"},
                "PROTOCOL": {type: "string"},
                "UID": {type: "string"},
                "PASSWORD": {type: "string"},
                "SECURITY": {type: "string"},
        },
        "required": ["DATABASE", "HOSTNAME", "PORT", "PROTOCOL", "UID", "PASSWORD", "SECURITY"]
    }

    def __call__(self, **config):
        print("DB2PersistenceVolume:Calling __call__::{}".format(self._instance))
        if not self._instance:
            self.connect(**config)

        print("DB2PersistenceVolume:Calling __call__::self._instance::", self._instance)
    

    @validate_input(schema=schema_connect)
    def connect(self, **config):
        print("IBM DB2:Calling connect")

        db = config.get("DATABASE")
        host = config.get("HOSTNAME")
        port = config.get("PORT")
        protocol = config.get("PROTOCOL")
        uid = config.get("UID")
        password = config.get("PASSWORD")
        security = config.get("SECURITY")

        SSL_DSN = "DATABASE={};HOSTNAME={};PORT={};PROTOCOL={};UID={};PWD={};Security={};".format(
            db, host, port, protocol, uid, password, security)

        self._instance = ibm_db.connect(SSL_DSN, "", "")

    """save method"""

    def set_autocommit_mode(self, auto_commit_mode):
        if auto_commit_mode == False:
            ibm_db.autocommit(self._instance, ibm_db.SQL_AUTOCOMMIT_OFF)

    """save method"""
    def insert(self):
        pass

    
    """save method"""
    def update(self):
        pass

    """save method"""
    def list(self):
        pass


    """save method"""
    def upsert(self):
        pass
