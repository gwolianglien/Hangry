import xml.etree.ElementTree as ElementTree
from preprocess import create_restaurant_set
import pandas as pd

"""
MetaData
name, rating, price, context, cuisine, district

Reviews
name, review

Dishes
restaurant, dish, review
"""

data_path = 'dataset/infatuation.xml'
root = ElementTree.parse(data_path).getroot()
restaurantset = create_restaurant_set(root)

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
metadata.to_csv('../data/metadata.csv', index=False)
