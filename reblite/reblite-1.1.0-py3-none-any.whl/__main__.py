from .db import *
from .exceptions import *
import json
import os

class Client:
	client = HandlerFile()

	def get_col(self, col):
		""" """
		self.client.initcol(col)
		return Col(col)

class Col(Client):
	def __init__(self, name):
		self.name = name

	def insert_one(self, doc):
		""" """
		self.client.initdoc(self.name, doc)

	def insert_many(self, docs):
		""" """
		for doc in docs:
			self.client.initdoc(self.name, doc)

	def update_one(self, query, docs):
		""" """
		if "_id" in docs:
			raise DenyEdit("Cannot edit _id.")
		gt = Query(self.name).load_one(query)
		if gt is None:
			raise NotFound("There was no document found with the provided query.")
		self.client.updatedoc(self.name, gt, docs)

	def update_many(self, query, docs):
		""" """
		if "_id" in docs:
			raise DenyEdit("Cannot edit _id.")
		gt_ = Query(self.name).load_filter(query)
		for gt in gt_:
			self.client.updatedoc(self.name, gt, docs)

	def update_all(self, docs):
		""" """
		for doc in docs:
			if "_id" in docs:
				raise DenyEdit("Cannot edit _id.")
		gt_ = Query(self.name).load_all()
		for gt in gt_:
			self.client.updatedoc(self.name, gt, docs)


	def find_all(self):
		""" """
		return Query(self.name).load_all()

	def find_many(self, query):
		""" """
		return Query(self.name).load_filter(query)

	def find_one(self, query):
		""" """
		return Query(self.name).load_one(query)

	def delete_one(self, query):
		""" """
		data = Query(self.name).load_one(query)
		if data is None:
			raise NotFound("There was no document found with the provided query.")
		self.client.deletedata(self.name, data["_id"])

	def delete_many(self, query):
		""" """
		data_ = Query(self.name).load_filter(query)
		for data in data_:	
			self.client.deletedata(self.name, data["_id"])

	def delete_all(self):
		""" """
		data_ = Query(self.name).load_all()
		for data in data_:	
			self.client.deletedata(self.name, data["_id"])

	def drop(self):
		""" Deletes a collection """
		self.client.deltable(self.name)

class Sort:
	def __init__(self, ls):
		self.ls = ls
		self.sorting = Sorting(self.ls)

	def by_asc(self, key):
		""" Sorts the list of dictionaries according to key in ascending order. """
		return self.sorting.by_asc(key)

	def by_desc(self, key):
		""" Sorts the list of dictionaries according to key in descending order. """
		return self.sorting.by_desc(key)