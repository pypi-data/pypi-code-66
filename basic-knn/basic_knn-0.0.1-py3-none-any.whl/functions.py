import numpy as np
from classes import Input, Data, Output

# euclidean distance
def euc_dist(x, y, a, b):
	return np.sqrt((x - a) ** 2 + (y - b) ** 2)

# create data - returns list of Data Objects
def create_data(xs : list, ys : list, labels : list):
	try:
		all_data = list()
		for i in range(len(xs)):
			data = Data(xs[i], ys[i], labels[i])
			all_data.append(data)
	except Exception as e:
		print(e)

	return all_data

# create output list - returns list of Output object
def create_output(input_, data):
	try:
		output = list()
		for i in range(len(data)):
			distance = euc_dist(input_.x, input_.y, data[i].x, data[i].y)
			label = data[i].label
			output_data = Output(distance, label)
			output.append(output_data)
	except Exception as e:
		print(e)

	return output