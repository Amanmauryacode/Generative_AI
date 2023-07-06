from pymongo import MongoClient
import re

client = MongoClient('')
db = client['db1']
collection = db['Customers']

name_pattern = re.compile('^B', re.IGNORECASE)

filter = {'id': {'$gt': '2'}, 'name': {'$regex': name_pattern}}

cursor = collection.find(filter)

for document in cursor:
    print(document)

client.close()
