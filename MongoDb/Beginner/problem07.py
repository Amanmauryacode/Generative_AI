from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

order = [('name', -1)]

cursor = collection.find().sort(order)

for document in cursor:
    print(document)

client.close()
