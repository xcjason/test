from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.test
# cursor = db.restaurants.find({'borough':'Manhattan', 'name' : 'Fish Bar'})
cursor = db.restaurants.find({'borough': 'Manhattan', 'cuisine': 'Bakery'})
pp = pprint.PrettyPrinter()
for doc in cursor:
    pp.pprint(doc)
