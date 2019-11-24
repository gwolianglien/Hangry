import os
import pickle


def load_restaurantset():
    fp = os.path.join('store', 'restaurantset.sav')
    restaurantset = load_pickled_data(fp)
    return restaurantset


def load_interface():
    fp = os.path.join('store', 'interface.sav')
    interface = load_pickled_data(fp)
    return interface


def load_metadata():
    fp = os.path.join('store', 'pandas.sav')
    metadata = load_pickled_data(fp)
    return metadata


def load_pickled_data(filepath):
    try:
        f = open(filepath, 'rb')
        data = pickle.load(f)
        return data
    except FileNotFoundError:
        print('"File not found"')
        return "File not found"
    except:
        print('Error loading data')
        return "Error loading data"
