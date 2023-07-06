from pymongo import MongoClient

client = MongoClient('')
db = client['db1']

customers_collection = db['Customers']

customers_collection.create_index("id", unique=True)
customers_collection.create_index("name")
customers_collection.create_index("email")
customers_collection.create_index("address")
customers_collection.create_index("phone_number")
