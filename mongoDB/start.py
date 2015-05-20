from pymongo import MongoClient

client = MongoClient()
db = client.test
cursor = db.restaurants.find()
for doc in cursor:
    print doc
