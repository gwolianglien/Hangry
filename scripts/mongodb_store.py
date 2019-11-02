import pickle
from actions.db import connect
from extract import extract

"""
Store the data into MongoDB
"""
def store():

    filename = 'restaurantset.sav'
    path = os.path.join('..', 'server', 'recommendations', 'data')
    if not os.path.exists(path):
        os.makedirs(path)
        extract()  # Create parsed restaurantset object
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


def get_mongo_uri(username, password, db, collection):
    return genericMongoURI.format(username, password, db, collection)


def connect():
    try:
        my_mongoURI = get_mongo_uri(username, password, db_name, collection_name)
        client = pymongo.MongoClient(
            my_mongoURI,
            ssl=True,
            ssl_cert_reqs=ssl.CERT_NONE
        )
        print("MongoDB Connected...")
        return client
    except pymongo.errors.ConnectionFailure:
        print("Server Not Available")


if __name__ == "__main__":
    store()
