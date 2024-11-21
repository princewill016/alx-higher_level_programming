-- 5-create_table_unique_id.sql
-- Script to create the table 'unique_id' with specified columns and unique constraint on 'id'

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

