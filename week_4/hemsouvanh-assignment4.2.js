// This query displays all documents in the users collection
db.users.find().pretty()

// This query finds the user with the email address jbach@me.com
db.users.findOne({ "email": "jbach@me.com" })

// This query finds a user with the last name of Mozart
db.users.findOne({ "lastName": "Mozart" })

// This query finds a user with the first name of Richard
db.users.findOne({ "firstName": "Richard" })

// This query finds a user with the employeeId of 1010
db.users.findOne({ "employeeId": "1010" })
