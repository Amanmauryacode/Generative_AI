from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

sort_order = [('id', 1)]

cursor = collection.find().sort(sort_order).skip(2)

for document in cursor:
    print(document)

client.close()
