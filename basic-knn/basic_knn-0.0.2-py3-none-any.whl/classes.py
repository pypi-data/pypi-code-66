import numpy as np

class Input(object):

	def __init__(self, x, y):
		self.x = np.array([x]).astype(np.float32)
		self.y = np.array([y]).astype(np.float32)

	def __repr__(self):
		return f"<class: Input, (x = {self.x}, y = {self.y})>"

class Data(object):

	def __init__(self, x, y, label):
		self.x = np.array([x]).astype(np.float32)
		self.y = np.array([y]).astype(np.float32)
		self.label = label

	def __repr__(self):
		return f"<class: Data>"

class Output(object):

	def __init__(self, distance, label):
		self.dist = np.array([distance]).astype(np.float32)
		self.label = label

	def __repr__(self):
		return f"<class: Output>"