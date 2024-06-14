-- Learning SQL: 05 - Aggregate functions
-- AGGREGATE FUNCTIONS

-- Aggregate functions are functions that perform a calculation on a set of values and return a single value.

-- Count the total of users
SELECT COUNT(*) AS total_users FROM users;

-- Count the total of users that have a reservation
SELECT COUNT(*) FROM users
WHERE id IN (SELECT user_id FROM reservations);

-- Another way, using JOIN
SELECT COUNT(*) FROM users us
INNER JOIN reservations res ON us.id = res.user_id;

-- Get the oldest user
SELECT MAX(TIMESTAMPDIFF(YEAR, birth_date, CURDATE())) AS max_age FROM users;

-- Get users above 18 years old
SELECT * FROM users
WHERE TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) > 18;

-- GROUPING
-- Get the quantity of reservations for each destination
SELECT dest.name AS destination_name, COUNT(*) AS reservations_count FROM reservations res
INNER JOIN destinations dest ON res.destination_id = dest.id
GROUP BY dest.name;

-- Get the destination with the most reservations
SELECT dest.name AS destination_name, COUNT(*) AS reservations_count FROM reservations res
INNER JOIN destinations dest ON res.destination_id = dest.id
GROUP BY dest.name
ORDER BY COUNT(*) DESC
LIMIT 1;

