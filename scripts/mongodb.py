import os
import pickle
import ssl
import pymongo
from extract import extract_restaurantset_xml
from access import load_restaurantset_store
from default import genericMongoURI, username, password, db_name, collection_name


"""
Store the data into MongoDB
"""
def mongodb_store():
    try:
        restaurantset = load_restaurantset_store()
        connection = connect()
        db_data = connection["RestaurantList"]
        db_restaurant = db_data["Restaurant"]
        for restaurant in restaurantset:
            db_restaurant.insert_one(restaurant)
        print("Data Upload Complete")
    except:
        raise Exception("Server Error")


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


def get_mongo_uri(username, password, db, collection):
    return genericMongoURI.format(username, password, db, collection)


if __name__ == "__main__":
    mongodb_store()
