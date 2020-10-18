import pandas as pd

class CsvHandler():
    file_path = ''

    def __init__(self, path): 
        self.file_path = path
        
    def get_metadata(self):
        data_frame = pd.read_csv(self.file_path)
        return {'rows_count': data_frame.shape[0], 'file_path': self.file_path, 'columns': data_frame.columns.tolist()}

    def get_page(self, page_number, page_size):
        data_frame = pd.read_csv(self.file_path, skiprows=(page_number-1)*page_size, nrows=page_size)
        return data_frame.values.tolist()
