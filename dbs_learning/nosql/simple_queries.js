// Learning NoSQL: 02 - Basic operations
// This file will be based on MongoDB commands
// Simple queries

// Fetching a user by city address
db.users.find({ "address.city": "New York" })

// Using logical operators
// $and, $or, $not, $nor

// Fetching a user by city address and status
db.users.find({ $and: [{ "address.city": "New York" }, { status: "active" }] })

// Fetching a user by city address or status
db.users.find({ $or: [{ "address.city": "New York" }, { status: "inactive" }] })

// Fetching a user by city address and not status
db.users.find({ $and: [{ "address.city": "São Paulo" }, { status: { $not: { $eq: "inactive" } } }] })

// Fetching a user by city address and not status
db.users.find({ $and: [{ "address.city": "Curitiba" }, { status: { $not: { $eq: "active" } } }] })

// Fetch all users with age greater than 30 and status active
db.users.find({ $and: [{ age: { $gt: 30 } }, { status: "active" }] })

// Fetch a user by name and age
db.users.find({ $and: [{ name: "Alice Thompson" }, { age: 45 }] })

// Fetch all users with age greater than 20 and less than 38
db.users.find({ $and: [{ age: { $gt: 20 } }, { age: { $lt: 38 } }] })

// Fetch all users with age not equal to 24
db.users.find({ age: { $ne: 24 } })

// Fetch all users with email ending by @gmail.com
db.users.find({ email: { $regex: "@gmail.com$" } })

// Fetch all users with State equal to NY or CA, and age greater than or equal to 28
db.users.find({ $and: [{ $or: [{ "address.state": "NY" }, { "address.state": "CA" }] }, { age: { $gte: 28 } }] })

// Fetch only the name of all users
db.users.find({}, { name: 1 })

// Fetch only the name and email of all users
db.users.find({}, { name: 1, email: 1 })

// Fetch users ordered by age ascending and only user name and age
db.users.find({}, { name: 1, age: 1 }).sort({ age: 1 })

// Pagination
// Limiting the number of results
db.users.find({}).limit(2)

// Skipping the first results
db.users.find({}).skip(2)

// Limiting and skipping
db.users.find({}).limit(2).skip(2)

// Sorting
// Sorting by name ascending
db.users.find({}).sort({ name: 1 }).limit(3)

// Sorting by name descending
db.users.find({}).sort({ name: -1 })