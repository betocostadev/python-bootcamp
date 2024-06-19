// This is just feed data to be inserted in the users collection
// Inserting a single user:
db.users.insertOne({
    "name": "John Doe",
    "email": "jonh.doe@gmail.com",
    "age": 30,
    "birth_date": "1995-12-01",
    "status": "active",
    "created_at": new Date(),
    "updated_at": new Date(),
})

// Inserting multiple users:
db.users.insertMany([
    {
        "name": "Jane Doe",
        "email": "jane.doe@gmail.com",
        "age": 24,
        "birth_date": "2000-01-01",
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    },
    {
        "name": "Alice Thompson",
        "email": "al.thompson@outlook.com",
        "age": 45,
        "birth_date": "1979-06-15",
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    },
])

