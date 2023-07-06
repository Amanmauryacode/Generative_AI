from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

cursor = collection.find()

for document in cursor:
    print(document)

client.close()
