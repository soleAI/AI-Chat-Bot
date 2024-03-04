
from pymongo import MongoClient
import os
URI = os.getenv("PRODUCTION_DB_URI") or 'mongodb://localhost:27017' 
client = MongoClient(URI)

db = client.sole_ai_db

user_collection = db['users']
