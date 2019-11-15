import os
import pickle
from extract import extract_restaurantset_xml


def load_restaurantset_store(path=os.path.join('..', 'server', 'store', 'restaurantset.sav')):
    if not os.path.exists(path):
        restaurantset = extract_restaurantset_xml()
        return restaurantset
    f = open(path, 'rb')
    restaurantset = pickle.load(f)
    return restaurantset
