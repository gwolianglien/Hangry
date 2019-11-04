import os
import pickle


def load_data():
    data_dir_path = os.path.join('interface', 'data')
    interface_filename = 'interface.sav'
    try:
        interface = get_stored_data(os.path.join(data_dir_path, interface_filename))
        return interface
    except FileNotFoundError:
        raise Exception('Error Loading Restaurant Data')


def get_stored_data(filepath: str) -> object:
    file = open(filepath, 'rb')
    unpickled = pickle.load(file)
    return unpickled


def get_unique_values(series: 'Pandas Series', sort=True) -> dict:
    uniques = list(set(series))
    if sort:
        uniques.sort()
    return { key: 0 for key in uniques }
