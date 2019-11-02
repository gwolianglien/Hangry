from extract import extract
from mongodb_store import store
from interface import get_interface_data

def run():
    extract()  # parse restaurantset xml file
    store()  # store parsed restaurantset into mongodb
    get_interface_data()
    

if __name__ == '__main__':
    run()
