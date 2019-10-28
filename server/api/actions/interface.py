import os
import pickle
import pandas as pd


def load_data():
    try:
        interface_filepath = os.path.join('..', 'data', 'interface.sav')
        interface = get_stored_data(interface_filepath)

        restaurantset_filepath = os.path.join('..', 'data', 'restaurantset.sav')
        restaurantset = get_stored_data(restaurantset_filepath)

        metadata_filepath = os.path.join('..', 'data', 'metadata.sav')
        metadata = get_stored_data(metadata_filepath)

        return restaurantset, interface, metadata
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
