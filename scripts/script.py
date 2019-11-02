from extract import extract
from mongodb_store import store
from interface import get_interface_data

def run():
    extract()  # parse restaurantset xml file
    print('Extract complete...')
    store()  # store parsed restaurantset into mongodb
    print('Store complete...')
    get_interface_data()
    print('Interface complete...')


if __name__ == '__main__':
    run()
