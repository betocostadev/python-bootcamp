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

// Fetching data
// Fetching all users
db.users.find({})
// Fetching a single user
db.users.findOne({ name: "Alice Thompson" })
// Fetching all users with a specific status
db.users.find({ status: "active" })
// Fetching all users with a specific status and age
db.users.find({ status: "active", age: 30 })
// Fetching all users with a specific status and age range
db.users.find({ status: "active", age: { $gte: 30, $lte: 40 } })
// Find a user and increment the age by 1
db.users.findOneAndUpdate(
    { name: "Alice Thompson" },
    { $inc: { age: 1 } }
)
// Find a user and decrement the age by 1
db.users.findOneAndUpdate(
    { name: "Alice Thompson" },
    { $inc: { age: -1 } }
)


// Updating data
// Updating a single user
db.users.updateOne(
    { name: "Bob Brown" },
    { $set: { status: "inactive", updated_at: new Date() } }
)

// Updating multiple users
db.users.updateMany(
    { status: "active" },
    { $set: { status: "inactive", updated_at: new Date() } }
)

// Find and update a single user
db.users.findOneAndUpdate(
    { name: "Alice Thompson" },
    { $set: { status: "inactive" } }
)

// Find and update multiple users
db.users.findAndModify(
    { status: "active" },
    { $set: { status: "inactive" } }
)

db.users.findAndModify(
    { status: "active" },
    { $set: { travelling: 1 } }
)

// Deleting data
// Deleting a single user
db.users.deleteOne({ name: "Beto Costa" })

// Deleting multiple users
db.users.deleteMany({ status: "inactive" })

// Deleting all users
db.users.deleteMany({})

// Find and delete a single user
db.users.findOneAndDelete({ name: "Alice Thompson" })