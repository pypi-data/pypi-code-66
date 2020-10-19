import json
from .exceptions import *
import os
import copy
import sqlite3


class HandlerFile:
	def __init__(self):
		self.db = sqlite3.connect("main.sqlite")
		self.cursor = self.db.cursor()
		

	def initcol(self, col):
		self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {col}(
				id TEXT,
				data TEXT
			)""")

	def initdoc(self, col, doc):
		if " " in col:
			raise BadName("Invalid character in provided collection name.")
		else:
			if " " in doc:
				raise BadName("Invalid character in provided document name.")
			else:
				self.cursor.execute(f"SELECT * FROM {col}")
				data = self.cursor.fetchall()

				if "_id" not in doc:
					_id = f"doc_{len(data)}"
					doc["_id"] = _id
				else:
					_id = doc["_id"]

				self.cursor.execute(f"SELECT data FROM {col} WHERE id='{_id}'")
				bd = self.cursor.fetchone()

				if not bd:
					sql = f"INSERT INTO {col}(id, data) VALUES(?, ?)"
					val = (_id, str(doc))

					self.cursor.execute(sql, val)
					self.db.commit()
				else:
					raise DupExists("There is already a document with the _id.")

	def deletedata(self, col, id):
		self.cursor.execute(f"DELETE FROM {col} WHERE id='{id}'")
		self.db.commit()

	def deltable(self, col):
		self.cursor.execute(f"DROP TABLE IF EXISTS {col}")
		self.db.commit()

	def updatedoc(self, col, doc, new):
		doc.update(new)

		sql = f"UPDATE {col} SET data=? WHERE id=?"
		val = (str(doc), doc["_id"])
		self.cursor.execute(sql, val)
		self.db.commit()

class Query:
	def __init__(self, col):
		self.col = col
		self.db = sqlite3.connect("main.sqlite")
		self.cursor = self.db.cursor()

	def load_all(self):
		data = []

		self.cursor.execute(f"SELECT * FROM {self.col}")
		bd = self.cursor.fetchall()
		for i in bd:
			j = json.loads(i[1].replace("'", '"'))

			data.append(j)

		return data

	def load_filter(self, query):
		dump = self.load_all()
		for check in query.items():
			key = check[0]
			value = check[1]
			break

		data = []
		ret = []
		for item in dump:
			if key in item:
				if item[key] == value:
					data.append(item)

		return data

	def load_one(self, query):
		dump = self.load_all()
		for check in query.items():
			key = check[0]
			value = check[1]
			break

		for item in dump:
			if key in item:
				if item[key] == value:
					return item
		

class Sorting:
	def __init__(self, ls):
		self.ls = ls

	def by_asc(self, key):
		temp =  copy.copy(self.ls)
		least = None
		new = []
		last = []
		
		for item in temp:
			if key not in item:
				temp.pop(temp.index(item))
		
		while len(temp) > 0:
			for item in temp:
				if least is None:
					least = item
				else:
					if type(least[key]) == type(item[key]):
						if least[key] > item[key]:
							least = item
					else:
						raise BadType("There are conflicting data types. Both 'str' and 'int' present.")

			new.append(least)
			temp.pop(temp.index(least))
			least = None

		return new

	def by_desc(self, key):
		temp =  copy.copy(self.ls)
		least = None
		new = []
		
		for item in temp:
			if key not in item:
				temp.pop(temp.index(item))
		
		while len(temp) > 0:
			for item in temp:
				if least is None:
					least = item
				else:
					if type(least[key]) == type(item[key]):
						if least[key] < item[key]:
							least = item
					else:
						raise BadType("There are conflicting data types. Both 'str' and 'int' present.")

			new.append(least)
			temp.pop(temp.index(least))
			least = None

		return new