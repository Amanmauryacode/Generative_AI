from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

filter = {'$or': [{'phone_number': {'$exists': False}}, {'phone_number': None}]}

cursor = collection.find(filter)

for document in cursor:
    print(document)

client.close()
