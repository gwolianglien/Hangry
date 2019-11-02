import os


def load_data():
    data_dir_path = os.path.join('..', 'data')
    interface_filename = 'interface.sav'
    restaurant_filename = 'restaurant.sav'
    metadata_filename = 'metadata.sav'

    try:
        interface = get_stored_data(os.path.join(data_dir_path, interface_filename))
        restaurantset = get_stored_data(os.path.join(data_dir_path, restaurant_filename))
        metadata = get_stored_data(os.path.join(data_dir_path, metadata_filename))
        return restaurantset, interface, metadata
    except FileNotFoundError:
        raise Exception('Error Loading Restaurant Data')
