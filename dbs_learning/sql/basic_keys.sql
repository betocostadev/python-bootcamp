-- PRIMARY KEYS AND FOREIGN KEYS
-- Creating the tables created previously using basic_operations.sql to use primary keys and foreign keys

-- Creating the users table with the primary key
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    birth_date DATE
);

-- Creating the destinations table with the primary key

CREATE TABLE destinations (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL
);

-- Creating the reservations table with the primary key

CREATE TABLE reservations (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    destination_id INT NOT NULL,
    reservation_date DATE,
    reservation_status VARCHAR(255) DEFAULT 'PENDING',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (destination_id) REFERENCES destinations(id)
);

-- Modifying the tables to use the primary keys and foreign keys

ALTER TABLE users
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);