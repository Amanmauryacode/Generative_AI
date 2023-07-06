from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

require = {'name': 1, 'email': 1}


cursor = collection.find({}, require)

for document in cursor:
    print(document)

client.close()
