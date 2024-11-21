-- 3-create_table.sql
-- Script to create the table 'force_name' with specified columns in the given database

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

