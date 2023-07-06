from pymongo import MongoClient


client = MongoClient('')
db = client['db1']
collection = db['Customers']

filter = {'id': '3'}

customer = collection.find_one(filter)

print(customer)

client.close()
