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