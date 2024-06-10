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

INSERT INTO users (id, name, email, address, birth_date) VALUES (1, 'Beto Marques', 'beto@gmail.com', 'Rua Bunda Lele, 10 - Santa Maria São Paulo/SP', '1986-04-01');
INSERT INTO users (id, name, email, address, birth_date) VALUES (2, 'John Doe', 'john.doe@outlook.com', 'Street Bunglaros, 220 - Brookling New York/NY', '1988-02-10');
INSERT INTO users (id, name, email, address, birth_date) VALUES (3, 'Maria Silva', 'mari@gmail.com', 'Rua das Flores, 100 - Centro Rio de Janeiro/RJ', '1990-10-15');

INSERT INTO destinations (id, name, description) VALUES (1, 'Praia da Rosa', 'Great beach, so much fun!');
INSERT INTO destinations (id, name, description) VALUES (2, 'Serra do Mar', 'Great place to relax and enjoy the nature');
INSERT INTO destinations (id, name, description) VALUES (3, 'Cataratas do Iguaçu', 'Amazing waterfalls, you will love it!');

INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (1, 1, 1, '2024-12-01', 'CONFIRMED');
INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (2, 2, 2, '2024-12-01', 'PENDING');
INSERT INTO reservations (id, user_id, destination_id, reservation_date, reservation_status) VALUES (3, 3, 3, '2024-12-01', 'CANCELLED');


-- Querying data

SELECT * FROM users;
SELECT * FROM destinations;
SELECT * FROM destinations WHERE id = 1;
SELECT * FROM users WHERE birth_date > '1986-01-01' AND name LIKE 'Beto Marques';
SELECT * FROM `reservations` WHERE reservation_date > '2024-11-30';