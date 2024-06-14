-- Learning SQL: 04 - Advanced queries
-- ADVANCED QUERIES

-- Querying data

-- Joining tables: Join
-- Joining Types are: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN

-- INNER JOIN: Returns the rows that have matching values in both tables
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


-- LEFT JOIN: Returns all rows from the left table, and the matched rows from the right table
-- Get the users that made a reservation and the users that didn't make a reservation
-- Users without reservations will have NULL values in the reservation columns
SELECT * FROM users us
LEFT JOIN reservations res ON us.id = res.user_id;

-- RIGHT JOIN: Returns all rows from the right table, and the matched rows from the left table
-- Get the destinations that have reservations and the destinations that don't have reservations
-- Destinations without reservations will have NULL values in the reservation columns
SELECT * FROM reservations res
RIGHT JOIN destinations dest ON res.destination_id = dest.id;

-- FULL JOIN: Returns all rows when there is a match in one of the tables
-- Get all users and destinations
-- Users without reservations will have NULL values in the reservation columns
-- Destinations without reservations will have NULL values in the reservation columns
SELECT * FROM users us
FULL JOIN reservations res ON us.id = res.user_id
FULL JOIN destinations dest ON res.destination_id = dest.id;

-- UNION: Combines the result of two or more SELECT statements
-- Get all users and destinations
-- Users without reservations will have NULL values in the reservation columns
-- Destinations without reservations will have NULL values in the reservation columns
SELECT * FROM users us
LEFT JOIN reservations res ON us.id = res.user_id
UNION
SELECT * FROM reservations res
RIGHT JOIN destinations dest ON res.destination_id = dest.id;

-- SUBQUERIES: A query inside another query
-- Get the users that made a reservation
SELECT * FROM users
WHERE id IN (SELECT user_id FROM reservations);

-- Get the destinations that don't have reservations
SELECT * FROM destinations
WHERE id NOT IN (SELECT destination_id FROM reservations);

-- Get the users that didn't make a reservation
SELECT * FROM users
WHERE id NOT IN (SELECT user_id FROM reservations);

-- Get the quantity of reservations per user
SELECT us.name AS user_name, (SELECT COUNT(*) FROM reservations res WHERE res.user_id = us.id) AS reservations_count FROM users us;
