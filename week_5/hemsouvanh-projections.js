/**
	Title: hemsouvanh-projections.js
    Author: Brock Hemsouvanh
    Date: 11 Feb 2024
    Description: MongoDB Shell commands to change emails in the users collection from users.js.
 */

// This query adds a new user to the users collection
db.users.insertOne({
  "firstName": "Wolfgang",
  "lastName": "Mozart",
  "email": "wmozart@me.com",
  "employeeId": "1011",
});

// This query updates Mozart's email address
db.users.updateOne(
  { "lastName": "Mozart" },
  { $set: { "email": "mozart@me.com" } }
);

// This query verifies that Mozart's email address was updated
db.users.findOne({ "lastName": "Mozart" }, { "email": 1 });

// This query lists all documents in the users collection with only firstName, lastName, and email fields
db.users.find({}, { "firstName": 1, "lastName": 1, "email": 1 }).pretty();