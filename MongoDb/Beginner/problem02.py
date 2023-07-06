from pymongo import MongoClient

client = MongoClient('')
db = client['db1']
collection = db['Customers']

customers_data = [
    {
        'id': '1',
        'name': 'Aman',
        'email': 'aman@gnail.com',
        'address': 'varanasi',
        'phone_number': '123456789'
    },
    
    {
        'id': '2',
        'name': 'Anuj',
        'email': 'Anuj@gnail.com',
        'address': 'varanasi',
        'phone_number': '123456789'
    },
    
    {
        'id': '3',
        'name': 'Rahul',
        'email': 'Rahul@gnail.com',
        'address': 'dehradun',
        'phone_number': '123456789'
    },
    
    {
        'id': '4',
        'name': 'rounak',
        'email': 'rounak@gnail.com',
        'address': 'jaipur',
        'phone_number': '123456789'
    },
    
    {
        'id': '5',
        'name': 'shubham',
        'email': 'shubham@gnail.com',
        'address': 'pune',
        'phone_number': '123456789'
    }
    
]

collection.insert_many(customers_data)

client.close()