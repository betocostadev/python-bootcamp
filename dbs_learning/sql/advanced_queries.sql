-- Learning SQL: 05 - Advanced queries
-- ADVANCED QUERIES

-- Querying data

-- Joining tables: Join
-- Joining Types are: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN

-- Selecting the users that made a reservation
-- us here is being used as an alias for the users table
SELECT * FROM users us
INNER JOIN reservations res ON us.id = res.user_id;

-- Selecting the users that made a reservation and the destination
SELECT * FROM users us
INNER JOIN reservations res ON us.id = res.user_id
INNER JOIN destinations dest ON res.destination_id = dest.id;

-- Selecting the users that made a reservation and the destination with the user name and destination name
SELECT us.name AS user_name, dest.name AS destination_name FROM users us
INNER JOIN reservations res ON us.id = res.user_id
INNER JOIN destinations dest ON res.destination_id = dest.id;

