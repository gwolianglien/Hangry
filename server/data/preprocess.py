"""
return {
    restaurant: {
        name: str,
        rating: double,
        price: int,
        review: str,
        dishes = [
            {
                name: str,
                review: str,
            }
        ],
        context: [str],
        cuisine = [str],
        district = [str]
    }
}
"""


def get_key_tag_set(root, index):
    """
    :type root: XML Element Root
    :type index: int
    :rtype: Tuple
    """
    element = root[index]
    element_name = element.tag
    element_value = element.text
    return element_name, element_value


def get_key_multitag_sets(root, index):
    """
    :type root: XML Element Root
    :type index: int
    :rtype: Tuple
    """
    element = root[index]
    element_values = []
    
    element_name = element.tag
    for obj in element:
        element_values.append(obj.text)
    return element_name, element_values


def get_reviews(root, index):
    """
    :type root: XML Element Root
    :type index: int
    :rtype: Tuple
    """
    element = root[index]
    element_values = []
    
    name = element.tag
    element_values = []
    for obj in element:
        if obj.text:
            element_values.append(obj.text)
    reviews = ' '.join(element_values) if element_values else ''
    
    return name, reviews
    
    
def get_dish_object(root, index):
    """
    :type root: XML Element Root
    :rtype: Object
    """
    
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
        else:
            # handle error
            pass
        
    if dish_name is None:
        raise Exception('No Dish Name')
    if dish_review is None:
        raise Exception('No Dish Review')
        
    return dish_name, dish_review


def create_restaurant_object(root, index):
    """
    :type root: XML Element Root
    :rtype: Object
    """
    
    curr_restaurant = root[index]
    
    restaurant = {} # restaurant object
    dishes = []
    contexts = []
    
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


def create_restaurant_set(root):
    """
    :type root: XML Element Root
    :rtype: List
    """
    restaurants = []
    for i in range(len(root)):
        restaurant = create_restaurant_object(root, i)
        restaurants.append(restaurant)
    return restaurants
    
