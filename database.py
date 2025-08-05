# database.py

from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

def get_db_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

def insert_data(data: dict):
    collection = get_db_collection()
    result = collection.insert_one(data)
    return result.inserted_id
