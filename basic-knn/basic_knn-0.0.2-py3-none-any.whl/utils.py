import os
import pandas as pd

# show data from the csv file
def show_data(dataframe, row_number : int = 10):
	dataframe.head(row_number)

# drop NaN cells
def drop_nan(dataframe, axis : int, threshold : int):
	try:
	        dropped_dataframe = dataframe.dropna(axis = axis, thresh = threshold)
	except Exception as e:
		print(e)

	return dropped_dataframe

# load files from a file
def load_data(path : str, filename : str):
	if ".csv" not in filename:
		raise Exception("File format must be a '.csv'")

	try:
		filepath = os.path.join(path, filename)
		file = pd.read_csv(filepath)
		data = pd.DataFrame(file)
	except Exception as e:
		print(e)

	return data
