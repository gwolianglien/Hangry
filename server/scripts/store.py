import pickle
from actions.db import connect


"""
Store the data into MongoDB
"""
def main():

    filename = 'infatuation_restaurantset.sav'
    path = '../api/data/'
    if not os.path.exists(path):
        os.makedirs(path)
    filepath = path + filename

    try:
        file_obj = open(filepath, 'rb')
        restaurantset = pickle.load(file_obj)
        connection = connect()
        db_data = connection["RestaurantList"]
        db_restaurant = db_data["Restaurant"]
        for restaurant in restaurantset:
            db_restaurant.insert_one(restaurant)
        print("Data Upload Complete")
    except:
        raise Exception("Server Error")


if __name__ == "__main__":
    main()
