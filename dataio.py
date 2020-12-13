from pymongo import MongoClient
from config import mongo_connect_string


def connect_to_mongo():
    uri = mongo_connect_string
    client = MongoClient(uri)
    db = client.general
    return db


def add_data(collection_name, data):
    db = connect_to_mongo()
    collection = db[collection_name].insert_one(data)


def get_data(collection_name):
    db = connect_to_mongo()
    data = db[collection_name].find()
    return data


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{email}, {name}, {message}')