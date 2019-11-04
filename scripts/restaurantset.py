import os
import pickle
import pandas as pd
from extract import extract


def get_restaurantset_metadata():

    filename = 'restaurantset.sav'
    path = os.path.join('..', 'server', 'recommendations', 'data')
    if not os.path.exists(path):
        os.makedirs(path)
        extract()  # Create parsed restaurantset object

    filepath = os.path.join(path, filename)

    try:
        file_obj = open(filepath, 'rb')
        restaurantset = pickle.load(file_obj)
    except FileNotFoundError:
        raise Exception('Restaurantset not found - try running extract script')

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
    metadata_filepath = os.path.join(path, metadata_filename)

    metadata_file = open(metadata_filepath, 'wb')
    pickle.dump(metadata, metadata_file)
    metadata_file.close()


if __name__ == '__main__':
    get_restaurantset_metadata()
