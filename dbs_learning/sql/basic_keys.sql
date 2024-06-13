-- Learning SQL: 02 - Primary keys and foreign keys
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

-- Modifying the users table to use the primary key
ALTER TABLE users
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Modifying the destinations table to use the primary key
ALTER TABLE destinations
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Modifying the reservations table to use the primary key and foreign keys
ALTER TABLE reservations
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id),
ADD FOREIGN KEY (user_id) REFERENCES users(id),
ADD FOREIGN KEY (destination_id) REFERENCES destinations(id);

-- Another way by adding the constraints separately
ALTER TABLE reservations
ADD CONSTRAINT fk_reservations_destinations
FOREIGN KEY (destination_id) REFERENCES destinations (id);

ALTER TABLE reservations
ADD CONSTRAINT fk_reservations_users
FOREIGN KEY (user_id) REFERENCES users (id);

-- Or also adding a cascade delete to the foreign key
ALTER TABLE reservations
ADD CONSTRAINT fk_reservations_users
FOREIGN KEY (user_id) REFERENCES users (id)
ON DELETE CASCADE;

-- Changing the reservations table and adding a command to delete the reservation if the user is deleted
ALTER TABLE reservations
ADD FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
-- Doing the same for the destination
ALTER TABLE reservations
ADD FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE;

-- Inserting data

INSERT INTO users (name, email, address, birth_date) VALUES ('Jane Doe', 'jane_doe@icloud.com', 'Street Bunglaros, 220, New York, New York', '1989-03-15');
INSERT INTO reservations (user_id, destination_id, reservation_date, reservation_status) VALUES (5, 2, '2024-10-05', 'PENDING');
INSERT INTO reservations (user_id, destination_id, reservation_date, reservation_status) VALUES (2, 2, '2024-10-05', 'PENDING');
INSERT INTO destinations (name, description) VALUES ('Ubatuba', 'Lots of beaches to have a lot of fun!');
INSERT INTO destinations (name, description) VALUES ('Monte Verde', 'Great place to relax and enjoy the nature');
INSERT INTO reservations (user_id, destination_id, reservation_date, reservation_status) VALUES (6, 7, '2024-07-15', 'CANCELLED');

-- Dropping a constraint
ALTER TABLE reservations
DROP CONSTRAINT fk_reservations_users;

-- Dropping tables

DROP TABLE users;

