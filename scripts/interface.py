import os
import pickle
import pandas as pd
from extract import extract
from restaurantset import get_restaurantset_metadata


def get_interface_data():

    filename = 'metadata.sav'
    path = os.path.join('..', 'server', 'recommendations', 'data')
    if not os.path.exists(path):
        os.makedirs(path)
        extract()  # Create parsed restaurantset object
        get_restaurantset_metadata()
    filepath = os.path.join(path, filename)

    try:
        file_obj = open(filepath, 'rb')
        metadata = pickle.load(file_obj)
    except FileNotFoundError:
        raise Exception('Metadata not found - try running restaurantset script')

    locations = get_all_unique_attributes(metadata, key='districts')
    contexts = get_all_unique_attributes(metadata, key='contexts')
    cuisines = get_all_unique_attributes(metadata, key='cuisines')

    obj = {
        'locationlist': locations,
        'contextlist': contexts,
        'cuisinelist': cuisines,
    }

    interface_filename = 'interface.sav'
    interface_path = os.path.join('..', 'server', 'interface', 'data')
    if not os.path.exists(interface_path):
        os.makedirs(interface_path)
    interface_filepath = os.path.join(interface_path, interface_filename)
    interface_file = open(interface_filepath, 'wb')
    pickle.dump(obj, interface_file)
    interface_file.close()


def get_all_unique_attributes(df, key='districts', delimiter=';', sort=True) -> list:

    # handle if input cannot be found
    if key not in df:
        raise Exception('Metadata key could not be found')

    attributes = list(df[key])
    unique_attributes = []

    for attribute in attributes:
        arr = attribute.split(delimiter)
        unique_attributes.extend(arr)

    unique_attributes = list(set(unique_attributes))

    if sort is True:
        unique_attributes.sort()

    return unique_attributes


if __name__ == '__main__':
    get_interface_data()
