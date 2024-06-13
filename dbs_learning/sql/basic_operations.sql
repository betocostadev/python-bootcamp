-- Learning SQL: 01 - Basic operations
-- Creating tables

CREATE TABLE users (
    id INT,
    name VARCHAR(255) NOT NULL COMMENT 'User name',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'User email',
    address VARCHAR(100) NOT NULL COMMENT 'User address',
    birth_date DATE NOT NULL COMMENT 'User birth date');


CREATE TABLE viagens.destinations (
    id INT,
    name VARCHAR(255) NOT NULL COMMENT 'Destination name',
    description VARCHAR(255) NOT NULL COMMENT 'Destination description');

CREATE TABLE viagens.reservations (
    id INT COMMENT 'Reservation id',
    user_id INT NOT NULL COMMENT 'Reference to user id',
    destination_id INT NOT NULL COMMENT 'Reference to destination id',
    reservation_date DATE COMMENT 'Reservation date',
    reservation_status VARCHAR(255) DEFAULT 'PENDING' COMMENT 'Reservation status - Confirmed, Pending, Cancelled');

-- Inserting data

INSERT INTO users (id, name, email, address, birth_date) VALUES (1, 'Beto Marques', 'beto@gmail.com', 'Rua Bunda Lele, 101, São Paulo, São Paulo', '1986-04-01');
INSERT INTO users (id, name, email, address, birth_date) VALUES (2, 'John Doe', 'john.doe@outlook.com', 'Street Bunglaros, 220, New York, New York', '1988-02-10');
INSERT INTO users (id, name, email, address, birth_date) VALUES (3, 'Maria Silva', 'mari@gmail.com', 'Rua das Flores, 100, Rio de Janeiro, Rio de Janeiro', '1990-10-15');
INSERT INTO users (id, name, email, address, birth_date) VALUES (4, 'Juliana Silva', 'jusil@gmail.com', 'Rua das Flores, 100, Rio de Janeiro, Rio de Janeiro', '1991-12-03');

INSERT INTO destinations (id, name, description) VALUES (1, 'Praia da Rosa', 'Great beach, so much fun!');
INSERT INTO destinations (id, name, description) VALUES (2, 'Serra do Mar', 'Great place to relax and enjoy the nature');
INSERT INTO destinations (id, name, description) VALUES (3, 'Cataratas do Iguaçu', 'Amazing waterfalls, you will love it!');
INSERT INTO destinations (id, name, description) VALUES (4, 'Pantanal', 'Great place to see the wildlife');

INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (1, 1, 1, '2024-12-01', 'CONFIRMED');
INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (2, 2, 2, '2024-10-05', 'PENDING');
INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (3, 3, 3, '2024-08-01', 'CANCELLED');
INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (4, 4, 4, '2024-10-14', 'CONFIRMED');

-- Querying data

SELECT * FROM users;
SELECT * FROM destinations;
SELECT * FROM destinations WHERE id = 1;
SELECT * FROM users WHERE birth_date > '1986-01-01' AND name LIKE 'Beto Marques';
SELECT * FROM users WHERE id = 1 OR name LIKE '%John%';
SELECT name FROM users WHERE id = 1 OR name LIKE '%John%';
SELECT * FROM `reservations` WHERE reservation_date > '2024-11-30';
SELECT * FROM `reservations` WHERE reservation_date > '2024-11-30' AND reservation_status = 'CONFIRMED';

-- Updating data

UPDATE users SET name = 'Beto Marques Costa' WHERE id = 1;
UPDATE users SET address = 'Rua Bunda Lele, 101, São Paulo, São Paulo' WHERE id = 1;
UPDATE reservations SET reservation_status = 'CONFIRMED' WHERE id = 2;
UPDATE reservations SET reservation_date = '2024-09-10' WHERE id = 2;

-- Deleting data

DELETE FROM users WHERE id = 4;

-- Dropping tables

DROP TABLE users;
DROP TABLE destinations;
DROP TABLE reservations;

-- Altering tables

ALTER TABLE users ADD COLUMN phone VARCHAR(20) COMMENT 'User phone number';
ALTER TABLE users MODIFY COLUMN email VARCHAR(100) NOT NULL UNIQUE COMMENT 'User email';
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users MODIFY COLUMN address VARCHAR(255) NOT NULL COMMENT 'User address';
ALTER TABLE users RENAME users_two;

-- Creating a new table based on another table

CREATE TABLE users_copy AS SELECT * FROM users;

-- Another way is to create the table first, then insert using SELECT
INSERT INTO users_copy (id, name, email, address, birth_date, phone) SELECT id, name, email, address, birth_date FROM users;
