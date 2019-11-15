import os
import pickle
import pandas as pd
from utilities import store_pickled_file
from access import load_restaurantset_store


def create_pandas_restaurantset():
    restaurantset = load_restaurantset_store()
    objects = []
    for restaurant in restaurantset:
        contexts = ';'.join(restaurant.get('contexts')) if restaurant.get('contexts') else ''
        cuisines = ';'.join(restaurant.get('cuisineset')) if restaurant.get('cuisineset') else ''
        districts = ';'.join(restaurant.get('districtset')) if restaurant.get('districtset') else ''
        obj = {
            'name': restaurant.get('name'),
            'rating': restaurant.get('rating'),
            'price': restaurant.get('price'),
            'contexts': contexts,
            'cuisines': cuisines,
            'districts': districts
        }
        objects.append(obj)
    df = pd.DataFrame(objects)
    name = 'pandas.sav'
    filepath = os.path.join('..', 'server', 'store')
    store_pickled_file(df, filepath, name)
    return df


if __name__ == '__main__':
    create_pandas_restaurantset()
