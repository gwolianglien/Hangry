import xml.etree.ElementTree as ElementTree
from preprocess import create_restaurant_set
from db import connect

def main():
    try:
        data_path = 'dataset/infatuation.xml'
        root = ElementTree.parse(data_path).getroot()
        restaurantset = create_restaurant_set(root)
        connection = connect()
        db_data = connection["Data"]
        db_restaurant = db_data["RestaurantSet"]
        for restaurant in restaurantset:
            db_restaurant.insert_one(restaurant)
        print("Data Upload Complete")
    except:
        raise Exception("Server Error")


if __name__ == "__main+__":
    main()

main()