import pymongo
import ssl
from config import genericMongoURI, username, password, db_name, collection_name


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
