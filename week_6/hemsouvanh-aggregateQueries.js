/**
	Title: hemsouvanh-aggregateQueries.js
    Author: Brock Hemsouvanh
    Date: 18 Feb, 2024
    Description: Various queries referencing data from houses.js.
 */

// Show a list of documents in the houses collection
db.houses.find().pretty();

// Show a list of documents in the students collection
db.students.find().pretty();

// Add a document to the students collection
db.students.insertOne({
    "firstName": "Magic",
    "lastName": "McSaviourson",
    "studentId": "s1019",
    "houseId": "h1007"
});

// Query to verify the new document was added to the students collection
db.students.findOne({"studentId": "s1019"});

// Delete the document created in the previous step
db.students.deleteOne({"studentId": "s1019"});

// Query to verify the document was removed from the students collection
db.students.findOne({"studentId": "s1019"});

// Show a list of students by house using the lookup operation
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "houseDetails"
        }
    }
]);

// Show a list of students for house Gryffindor using the lookup and match operations
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "houseDetails"
        }
    },
    {
        $match: {"houseDetails.mascot": "Lion"}
    }
]);

// Show a list of students for the Eagle mascot using the lookup and match operations
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "houseDetails"
        }
    },
    {
        $match: {"houseDetails.mascot": "Eagle"}
    }
]);