-- Learning SQL: 06 - Indexes
-- INDEXES

-- Indexes are used to improve the performance of queries by reducing the number of rows that need to be read.

-- Creating an index
-- Creating an index for the users table
CREATE INDEX idx_users_name ON users (name);

-- Creating an index for the reservations table
CREATE INDEX idx_reservations_user_id ON reservations (user_id);

-- Creating an index for the destinations table
CREATE INDEX idx_destinations_name ON destinations (name);

-- Dropping an index
-- Dropping the index for the users table
DROP INDEX idx_users_name ON users;

-- Explaining the query
-- Explaining the query to get the users that made a reservation
EXPLAIN SELECT * FROM users
WHERE id IN (SELECT user_id FROM reservations);

-- After creating the users index we can have a better performance in an operation like below
EXPLAIN SELECT * FROM users
WHERE name = 'John Doe';
