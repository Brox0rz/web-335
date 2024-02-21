''' Author: Brock Hemsouvanh
    Date: 2024-02-21
    hemsouvanh_usersp2.py Description: Connects to the web335DB database and performs actions and queries.
'''

from pymongo import MongoClient

# Build a connection string to connect to the MongoDB Atlas cluster
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']

# Step 3: Write the Python code to create a new user document
new_user = {
    "firstName": "Fawn",
    "lastName": "Bro",
    "email": "fbro@sure.com",
    "employeeId": "fbro123"
}
result = db.users.insert_one(new_user)
print(f"New user created with _id: {result.inserted_id}")

# Step 4: Write the Python code to display the newly created document
created_user = db.users.find_one({"_id": result.inserted_id})
print("Newly created user document:")
print(created_user)

# Step 5: Write the Python code to update the email address of the document you created in step 3
db.users.update_one({"_id": result.inserted_id}, {"$set": {"email": "fawn.bro@newemail.com"}})

# Step 6: Write the Python code to display the updated document
updated_user = db.users.find_one({"_id": result.inserted_id})
print("Updated user document:")
print(updated_user)

# Step 7: Write the Python code to delete the document you created in step 3
db.users.delete_one({"_id": result.inserted_id})

# Step 8: Write the Python code to prove the document was deleted
deleted_user = db.users.find_one({"_id": result.inserted_id})
print("Document after deletion (should be None):")
print(deleted_user)
