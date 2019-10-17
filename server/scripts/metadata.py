import pickle
import pandas as pd
from actions.data import get_all_unique_attributes

"""
MetaData
name, rating, price, context, cuisine, district

Reviews
name, review

Dishes
restaurant, dish, review
"""


def main():
    filename = 'infatuation_restaurantset.sav'
    path = '../api/data/'

    if not os.path.exists(path):
        os.makedirs(path)

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

        locations = get_all_unique_attributes(metadata, key='districts')
        vibes = get_all_unique_attributes(metadata, key='contexts')
        cuisines = get_all_unique_attributes(metadata, key='cuisines')





    except AssertionError:
        raise Exception('Error extracting metadata')
