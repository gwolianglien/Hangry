import os
import pickle
import pandas as pd


def load_data():
    data_dir_path = os.path.join('recommendations', 'data')
    restaurantset_filename = 'restaurantset.sav'
    metadata_filename = 'metadata.sav'

    try:
        restaurantset = get_stored_data(os.path.join(data_dir_path, restaurantset_filename))
        metadata = get_stored_data(os.path.join(data_dir_path, metadata_filename))
        return restaurantset, metadata
    except FileNotFoundError:
        raise Exception('Error Loading Restaurant Data')


def get_stored_data(filepath: str) -> object:
    file = open(filepath, 'rb')
    unpickled = pickle.load(file)
    file.close()
    return unpickled


def get_unique_values(series: 'Pandas Series', sort=True) -> dict:
    uniques = list(set(series))
    if sort:
        uniques.sort()
    return { key: 0 for key in uniques }
