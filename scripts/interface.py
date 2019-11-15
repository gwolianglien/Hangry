import os
import pickle
import pandas as pd
from utilities import store_pickled_file
from access import load_restaurantset_store


def create_interface_store():
    restaurantset = load_restaurantset_store()
    locations, contexts, cuisines = {}, {}, {}
    for restaurant in restaurantset:
        districtset = restaurant.get('districtset')
        for d in districtset:
            locations[d] = 0

        contextset = restaurant.get('contexts')
        for c in contextset:
            contexts[c] = 0

        cuisineset = restaurant.get('cuisineset')
        for c in cuisineset:
            cuisines[c] = 0

    obj = {
        'locationlist': list(set(locations)),
        'contextlist': list(set(contexts)),
        'cuisinelist': list(set(cuisines)),
    }

    interface_filename = 'interface.sav'
    interface_path = os.path.join('..', 'server', 'store')
    store_pickled_file(obj, interface_path, interface_filename)
    return obj


if __name__ == '__main__':
    create_interface_store()
