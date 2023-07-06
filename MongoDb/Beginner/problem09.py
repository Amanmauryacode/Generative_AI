from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

order = [('id', 1)]

cursor = collection.find().sort(order).limit(3)

for document in cursor:
    print(document)

client.close()
