import unittest
import pytest
import os
import copy

import pymongo
import alfred3

from alfred3_dbtools import mongotools


# class Testthepy:

#     @pytest.fixture
#     def mongodb_connector_db(self):
#         _host = os.environ.get("MONGODB_TESTHOST")
#         _port = int(os.environ.get("MONGODB_TESTPORT"))
#         _user1 = os.environ.get("MONGODB_TESTUSER")
#         _pw1 = os.environ.get("MONGODB_TESTPW")
#         _db = os.environ.get("MONGODB_TESTDB")
#         _col = os.environ.get("MONGODB_TESTCOL")
#         _user2 = os.environ.get("MONGODB_TESTUSER2")
#         _pw2 = os.environ.get("MONGODB_TESTPW2")
#         _auth_source = os.environ.get("MONGODB_TEST2AUTH")

#         connector = mongotools.MongoDBConnector(
#             host=_host, port=None, username=_user1, password=_pw1, database=_db
#         )

#         return connector

#     @pytest.fixture
#     def mongodb_connector_col(self):
#         _host = os.environ.get("MONGODB_TESTHOST")
#         _port = int(os.environ.get("MONGODB_TESTPORT"))
#         _user1 = os.environ.get("MONGODB_TESTUSER")
#         _pw1 = os.environ.get("MONGODB_TESTPW")
#         _db = os.environ.get("MONGODB_TESTDB")
#         _col = os.environ.get("MONGODB_TESTCOL")
#         _user2 = os.environ.get("MONGODB_TESTUSER2")
#         _pw2 = os.environ.get("MONGODB_TESTPW2")
#         _auth_source = os.environ.get("MONGODB_TEST2AUTH")

#         connector = mongotools.MongoDBConnector(
#             host=_host, port=None, username=_user1, password=_pw1, database=_db, collection=_col
#         )

#         return connector

#     def test_connect(self, mongodb_connector):
#         con = mongodb_connector
#         con.connect()

#         assert con.connected

#     def test_default(self, mongodb_connector):
#         assert mongodb_connector.connected == False


class TestMongoDBConnector(unittest.TestCase):
    def setUp(self):
        self._host = os.environ.get("MONGODB_TESTHOST")
        self._port = int(os.environ.get("MONGODB_TESTPORT"))
        self._user1 = os.environ.get("MONGODB_TESTUSER")
        self._pw1 = os.environ.get("MONGODB_TESTPW")
        self._db = os.environ.get("MONGODB_TESTDB")
        self._col = os.environ.get("MONGODB_TESTCOL")
        self._user2 = os.environ.get("MONGODB_TESTUSER2")
        self._pw2 = os.environ.get("MONGODB_TESTPW2")
        self._auth_source = os.environ.get("MONGODB_TEST2AUTH")

    def test_minimal_connect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=None,
            username=self._user1,
            password=self._pw1,
            database=self._db,
        )
        con.connect()
        self.assertTrue(con.connected)
        self.assertIsInstance(con.db, pymongo.database.Database)

    def test_auth_source_connect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=None,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            auth_source=self._auth_source,
        )
        con.connect()
        self.assertTrue(con.connected)
        self.assertIsInstance(con.db, pymongo.database.Database)

    def test_collection_connect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=None,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        con.connect()
        self.assertTrue(con.connected)
        self.assertIsInstance(con.db, pymongo.collection.Collection)

    def test_autoconnect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=None,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        self.assertFalse(con.connected)
        col = con.db
        self.assertTrue(con.connected)
        print(col)
        self.assertIsInstance(col, pymongo.collection.Collection)

    def test_disconnect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=None,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        con.connect()
        self.assertIsInstance(con.db, pymongo.collection.Collection)
        con.disconnect()
        self.assertFalse(con.connected)

    def test_insert_find_remove(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=None,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        col = con.db
        test_document = {"test": "test"}

        col.insert_one(test_document)
        query = col.find_one(test_document)
        self.assertIsNotNone(query)

        col.delete_one(test_document)
        delquery = col.find_one(test_document)
        self.assertIsNone(delquery)


if __name__ == "__main__":
    unittest.main()
