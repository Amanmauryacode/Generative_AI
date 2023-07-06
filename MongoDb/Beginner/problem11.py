from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

customer_count = collection.count_documents({})

print("Number of customers:", customer_count)

client.close()
