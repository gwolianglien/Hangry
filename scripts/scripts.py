from extract import extract_restaurantset_xml
from mongodb import mongodb_store
from dataframe import create_pandas_restaurantset
from interface import create_interface_store


def run(mongodb=False):
    extract_restaurantset_xml()  # parse restaurantset xml file
    print('XML extract complete...')

    if mongodb:
        store()  # store parsed restaurantset into mongodb
        print('MongoDB store complete...')

    create_pandas_restaurantset()
    print('Pandas store complete...')

    create_interface_store()
    print('Interface store complete...')


if __name__ == '__main__':
    run()
