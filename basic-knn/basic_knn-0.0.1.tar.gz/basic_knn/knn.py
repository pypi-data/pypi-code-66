from classes import Input
from functions import create_data, create_output

class KNNClassifier(object):

	def __init__(self, xs, ys, labels):

		self.train_x = xs
		self.train_y = ys
		self.labels  = labels

		# train data as Data object
		self.data = create_data(self.train_x, self.train_y, self.labels)

	def predict(self, input_):

		if type(input_) != tuple or len(input_) != 2:
			raise Exception("input format is not appropriate")

		# input as an Input object
		self.input = Input(input_[0], input_[1])

		# output data according to input and train data
		self.output = create_output(self.input, self.data)

		# calculated euclidean distance
		self.distance = [self.output[i].dist for i in range(len(self.output))]

		# prediction according to euclidean distance calculation
		min_distance = self.distance.index(min(self.distance))
		prediction   = self.output[min_distance].label

		return prediction