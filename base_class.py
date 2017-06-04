"""
some base class
"""
import pickle


class StoreData():
    """
    store data in a file
    """

    def __init__(self, data_file_name):
        self.data_file = data_file_name

    def save_data(self, data):
        """
        save data to data file
        """
        with open(self.data_file, 'wb') as f:
            pickle.dump(data, f)

    def load_data(self, default_data):
        """
        load data from data file
        """
        try:
            with open(self.data_file, 'rb') as f:
                data = pickle.load(f)
                return data
        except FileNotFoundError:
            self.save_data(default_data)
            return None
