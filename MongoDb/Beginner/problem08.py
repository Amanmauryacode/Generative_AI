from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

filter = {'id': '4'}

new_address = 'kanpur'

update_query = {'$set': {'address': new_address}}
collection.update_one(filter, update_query)

client.close()
