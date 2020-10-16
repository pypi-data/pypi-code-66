from pymongo import MongoClient

client = MongoClient(host="localhost", username="user_admin", password="admin")

print(client)


client.test.test.insert_one({"test": "test"})

print(client.test.test.find_one())


from alfred3_dbtools import mongotools

dbconnector = mongotools.MongoDBConnector(host="localhost", port=None, username="user_admin", password="admin", database="test", collection="test")

print(dbconnector.db.find_one())

