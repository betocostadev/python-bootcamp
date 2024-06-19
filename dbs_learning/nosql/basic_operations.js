// Learning NoSQL: 01 - Basic operations
// This file will be based on MongoDB commands
// Creating tables

// use {{ database_name }}
// If the database doens't exists, it will be created

db.users.insertOne({})
// This command will create the users collection with an empty entry

// Creating a collection
db.createCollection("destinations")

// Inserting data
db.destinations.insertOne({
    name: "Paris",
    country: "France"
})

// Inserting multiple data
db.destinations.insertMany([
    {
        name: "Paris",
        country: "France"
    },
    {
        name: "New York",
        country: "USA"
    },
    {
        name: "Tokyo",
        country: "Japan"
    }
])