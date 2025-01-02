from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['tourist_app']
users_collection = db['users']

"""# Create a demo user with just username and password
demo_user = {
    "username": "a",
    "password": "a"
}

# Insert the demo user into the 'users' collection
users_collection.insert_one(demo_user)

print("Demo user inserted!")"""


collection = db["destinations"]

# Add a new field "category" and set its value to "fort" for all documents
update_result = collection.update_many({}, {"$set": {"category": "Fort"}})

# Print the result
print(f"Matched documents: {update_result.matched_count}")
print(f"Modified documents: {update_result.modified_count}")

