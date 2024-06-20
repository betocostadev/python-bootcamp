// This is just seed data to be inserted in the users collection
// Inserting a single user:
db.users.insertOne({
    "name": "John Doe",
    "email": "jonh.doe@gmail.com",
    "age": 30,
    "birth_date": "1995-12-01",
    "address": {
        "street": "1234 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    },
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
        "address": {
            "street": "1234 Main St",
            "city": "New York",
            "state": "NY",
            "zip": "10001"
        },
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    },
    {
        "name": "Alice Thompson",
        "email": "al.thompson@outlook.com",
        "age": 45,
        "birth_date": "1979-06-15",
        "address": {
            "street": "1335 Birch St",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94107"
        },
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    },
    {
        "name": "Bob Brown",
        "email": "bbob@icloud.com",
        "age": 32,
        "birth_date": "1992-03-30",
        "address": {
            "street": "200 Seaport Blvd",
            "city": "Boston",
            "state": "MA",
            "zip": "02210"
        },
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    },
    {
        "name": "Beto Costa",
        "email": "roberto.costa@icloud.com",
        "age": 38,
        "birth_date": "1986-09-22",
        "address": {
            "street": "Rua Sebas 90",
            "city": "São Paulo",
            "state": "SP",
            "zip": "04552-060"
        },
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    },
    {
        "name": "Charlie Brown",
        "email": "charlie@gmail.com",
        "age": 28,
        "birth_date": "1996-08-12",
        "address": {
            "street": "4000 Warner Blvd",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "91522"
        },
        "status": "active",
        "created_at": new Date(),
        "updated_at": new Date(),
    }
])