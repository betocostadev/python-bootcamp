-- Learning SQL: 03 - Normalization
-- NORMALIZATION
--
-- We will fix the user address that is using street, number, neighborhood, city and state in the same column.

ALTER TABLE users
ADD COLUMN street VARCHAR(100) NOT NULL COMMENT 'User street',
ADD COLUMN number VARCHAR(10) NOT NULL COMMENT 'User number',
ADD COLUMN city VARCHAR(50) NOT NULL COMMENT 'User city',
ADD COLUMN state VARCHAR(50) NOT NULL COMMENT 'User state';

-- Executing a script to update the address column
UPDATE users
SET street = TRIM(SUBSTRING_INDEX(address, ',', 1)),
    number = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(address, ',', 2), ',', -1)),
    city = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(address, ',', -2), ',', 1)),
    state = TRIM(SUBSTRING_INDEX(address, ',', -1));

-- Dropping the address column
ALTER TABLE users
DROP COLUMN address;