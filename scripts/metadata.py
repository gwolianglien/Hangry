import os
import pickle
import pandas as pd
from actions.data import get_all_unique_attributes
from extract import extract


def get_metadata():
    filename = 'restaurantset.sav'
    path = '../api/data/'

    if not os.path.exists(path):
        os.makedirs(path)
        extract()

    filepath = path + filename

    try:
        file_obj = open(filepath, 'rb')
        restaurantset = pickle.load(file_obj)

        metadata_objs = []
        for restaurant in restaurantset:
            contexts = ';'.join(restaurant.get('contexts')) if restaurant.get('contexts') else ''
            cuisines = ';'.join(restaurant.get('cuisineset')) if restaurant.get('cuisineset') else ''
            districts = ';'.join(restaurant.get('districtset')) if restaurant.get('districtset') else ''
            metadata_dict = {
                'name': restaurant.get('name'),
                'rating': restaurant.get('rating'),
                'price': restaurant.get('price'),
                'contexts': contexts,
                'cuisines': cuisines,
                'districts': districts
            }
            metadata_objs.append(metadata_dict)

        metadata = pd.DataFrame(metadata_objs)

        metadata_filename = 'metadata.sav'
        metadata_filepath = path + metadata_filename
        metadata_file = open(metadata_filepath, 'wb')
        pickle.dump(metadata, metadata_file)
        metadata_file.close()

        locations = get_all_unique_attributes(metadata, key='districts')
        contexts = get_all_unique_attributes(metadata, key='contexts')
        cuisines = get_all_unique_attributes(metadata, key='cuisines')

        obj = {
            'locationlist': locations,
            'contextlist': contexts,
            'cuisinelist': cuisines,
        }

        interface_filename = 'interface.sav'
        interface_filepath = path + interface_filename

        interface_file = open(interface_filepath, 'wb')
        pickle.dump(obj, interface_file)
        interface_file.close()

    except EnvironmentError:
        raise Exception('Error extracting metadata')


if __name__ == '__main__':
    get_metadata()
