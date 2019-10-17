import os
import pickle
import xml.etree.ElementTree as ElementTree
from actions.preprocess import create_restaurant_set


"""
Extract and parse restaurant dataset from XML file and store as an object
"""
def main():
    data_path = './dataset/infatuation.xml'
    try:
        root = ElementTree.parse(data_path).getroot()
        restaurantset = create_restaurant_set(root)

        filename = 'infatuation_restaurantset.sav'
        path = '../api/data/'

        if not os.path.exists(path):
            os.makedirs(path)

        filepath = path + filename

        file_obj = open(filepath, 'wb')
        pickle.dump(restaurantset, file_obj)
        file_obj.close()
    except:
        raise Exception('Error extracting restaurant dataset')


if __name__ == '__main__':
    main()
