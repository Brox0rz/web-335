''' Author: Brock Hemsouvanh
    Date: 2024-02-18
    hemsouvanh_usersp1.py Description: Connects to the web335DB database and performs queries.
'''

from pymongo import MongoClient

# Build a connection string to connect to the MongoDB Atlas cluster
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']

# Display all documents in the user's collection
print("All documents in the user's collection:")
for user in db.users.find():
    print(user)

# Display a document where the employeeId is '1011'
print("\nDocument where the employeeId is '1011':")
print(db.users.find_one({"employeeId": "1011"}))

# Display a document where the lastName is 'Mozart'
print("\nDocument where the lastName is 'Mozart':")
print(db.users.find_one({"lastName": "Mozart"}))
