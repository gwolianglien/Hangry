import os
import pickle
import xml.etree.ElementTree as ElementTree
from utilities import store_pickled_file


def extract_restaurantset_xml():
    try:
        filepath = os.path.join('scraper', 'restaurantset.xml')
        root = ElementTree.parse(filepath).getroot()
        restaurantset = create_restaurant_set(root)

        filename = 'restaurantset.sav'
        path = os.path.join('..', 'server', 'store')
        store_pickled_file(restaurantset, path, filename)
        return restaurantset

    except FileNotFoundError:
        raise Exception('Restaurantset could not be found')
    except EOFError:
        raise Exception('Restaurantset has been corrupted')
    except:
        raise Exception('Error extracting restaurantset')


def create_restaurant_set(root) -> list:
    restaurants = []
    for i in range(len(root)):
        restaurant = create_restaurant_object(root, i)
        restaurants.append(restaurant)
    return restaurants


def create_restaurant_object(root, index) -> object:
    curr_restaurant = root[index]
    restaurant, dishes, contexts = {}, [], [] # restaurant object

    for i in range(len(curr_restaurant)):
        element = curr_restaurant[i]
        if element.tag == 'dish':
            name, value = get_dish_object(curr_restaurant, i)
            if type(value) == str:
                value = value.replace('.', '')
            dishes.append({name: value})
        elif element.tag == 'review':
            name, value = get_reviews(curr_restaurant, i)
            if type(value) == str:
                value = value.replace('.', '')
            restaurant[name] = value
        elif element.tag == 'cuisineset' or element.tag == 'districtset':
            name, value = get_key_multitag_sets(curr_restaurant, i)
            restaurant[name] = value
        elif element.tag == 'context':
            name, value = get_key_tag_set(curr_restaurant, i)
            if type(value) == str:
                value = value.replace('.', '')
            contexts.append(value)
        else:
            name, value = get_key_tag_set(curr_restaurant, i)
            if type(value) == str:
                value = value.replace('.', '')
            restaurant[name] = value

    restaurant['dishes'] = dishes
    restaurant['contexts'] = contexts
    return restaurant


def get_key_tag_set(root, index) -> tuple:
    element = root[index]
    element_name = element.tag
    element_value = element.text
    return element_name, element_value


def get_key_multitag_sets(root, index) -> tuple:
    element = root[index]
    element_values = []
    element_name = element.tag
    for obj in element:
        element_values.append(obj.text)
    return element_name, element_values


def get_reviews(root, index) -> tuple:
    element = root[index]
    name = element.tag
    element_values = [ obj.text for obj in element if obj.text]
    reviews = ' '.join(element_values) if element_values else ''
    return name, reviews


def get_dish_object(root, index) -> object:
    element = root[index]  # expected: dish element
    for obj in element:
        if obj.tag == 'name':
            dish_name = obj.text.replace('.', '')
        elif obj.tag == 'review':
            l = list(obj)
            if not l:
                dish_review = 'No Review'
            else:
                while l[0]:
                    l = list(l[0])
                dish_review = l[0].text.replace('.', '')
    if not dish_name or not dish_review:
        return None
    return dish_name, dish_review


"""
Extract and parse restaurant dataset from XML file and store as an object
"""
if __name__ == '__main__':
    extract_restaurantset_xml()
