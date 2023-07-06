from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

filter = {'id': '2'}

collection.delete_one(filter)

client.close()
