from pymongo import MongoClient
import re

client = MongoClient('')
db = client['db1']
collection = db['Customers']

pattern = re.compile('^A', re.IGNORECASE)

filter = {'name': {'$regex': pattern}}

cursor = collection.find(filter)

for document in cursor:
    print(document)

client.close()
