from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['tourist_app']
users_collection = db['users']

# Create a demo user with just username and password
demo_user = {
    "username": "a",
    "password": "a"
}

# Insert the demo user into the 'users' collection
users_collection.insert_one(demo_user)

print("Demo user inserted!")
